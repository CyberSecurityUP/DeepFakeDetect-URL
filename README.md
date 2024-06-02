# Image Scraper and Deepfake Checker

This project is an image scraping tool that downloads images from a webpage and checks if they are deepfakes using the [aiornot](https://docs.aiornot.com/) API.

## Features

- Scrapes images from a specified URL.
- Downloads images and saves them in the specified directory with sequential names (01.jpg, 02.jpg, etc.).
- Checks each downloaded image for deepfakes using the aiornot API.

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/CyberSecurityUP/DeepFakeDetect-URL
   cd DeepFakeDetect-URL
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Replace the `url` variable with the URL of the site you want to scrape.
2. Replace `folder_path` with the path where you want to save the downloaded images.
3. Replace `api_key` with your aiornot API key.
4. Run the script:

   ```sh
   python script.py
   ```

### Example Usage

```python
url = "URL_DEEPFAKE"
folder_path = "YOUR_FOLDER_DESTINATION"
api_key = "YOUR_API_KEY"

results = scrape_and_check_images(url, folder_path, api_key)
for res in results:
    print(f"Image: {res['image_path']}, Result: {res['result']}")
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project.
2. Create a new branch: `git checkout -b my-new-feature`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, contact [your email].
```

### Explanations:

- **Title and Description**: Provides an overview of the project.
- **Features**: Lists the main features of the project.
- **Requirements**: Details the necessary dependencies.
- **Installation**: Steps to clone the repository and install dependencies.
- **Usage**: Instructions on how to set up and run the script.
- **Example Usage**: Code snippet showing how to use the script.
- **Contributing**: Guidelines on how to contribute to the project.
- **License**: Information about the project's license.
- **Contact**: Contact information for support or suggestions.

Feel free to adjust the sections as needed to fit the specifics of your project.
