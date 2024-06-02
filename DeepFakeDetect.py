import os
import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def download_image(url, folder_path, file_name):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Always use .jpg as the extension
            sanitized_filename = f"{file_name}.jpg"
            file_path = os.path.join(folder_path, sanitized_filename)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded image: {file_path}")
            return file_path
        else:
            print(f"Failed to download image: {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while downloading image: {url} - Error: {e}")
    return None

def scrape_images_from_website(url, folder_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers, verify=False)  # Setting verify=False to ignore SSL certificates
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return []

    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content[:500]}")  # Print first 500 characters of the response content for debugging

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {url}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')
    image_urls = [urljoin(url, img['src']) for img in image_tags if 'src' in img.attrs]
    image_urls = [img_url for img_url in image_urls if img_url.startswith(('http://', 'https://'))]

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    downloaded_images = []
    for idx, img_url in enumerate(image_urls, start=1):
        file_name = f"{idx:02}"  # Create a file name like 01, 02, etc.
        print(f"Attempting to download image from URL: {img_url}")
        downloaded_image = download_image(img_url, folder_path, file_name)
        if downloaded_image:
            downloaded_images.append(downloaded_image)
    return downloaded_images

def check_deepfake(image_path, api_key):
    url = "https://api.aiornot.com/v1/reports/image"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    files = {
        "object": open(image_path, "rb")
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json()
    print(f"Failed to check deepfake for image: {image_path} - Status code: {response.status_code}")
    return None

def scrape_and_check_images(url, folder_path, api_key):
    downloaded_images = scrape_images_from_website(url, folder_path)
    results = []
    for image_path in downloaded_images:
        result = check_deepfake(image_path, api_key)
        if result:
            results.append({
                "image_path": image_path,
                "result": result
            })
    return results

# Example usage:
url = ""  # Replace with the target URL
folder_path = ""  # Replace with your desired folder path
api_key = ""  # Replace with your actual API key
results = scrape_and_check_images(url, folder_path, api_key)
for res in results:
    print(f"Image: {res['image_path']}, Result: {res['result']}")
