# BizCardX 📇

This repository showcases an end-to-end web application for extracting, managing, and maintaining business card information. Developed entirely by me, this project utilizes Google Generative AI (Gemini) for Optical Character Recognition (OCR) and provides a comprehensive interface for real-time data handling through a Streamlit application.

## Project Overview

The primary objective of this project is to facilitate the extraction of business card details from uploaded images and manage these details effectively. The application processes business card images using the Google Generative AI (Gemini) API to extract relevant information and performs various database operations including saving, viewing, editing, and deleting records.

## Key Features

- **End-to-End Development**: Fully developed from image processing and data extraction to database management and web interface.
- **Google Generative AI Integration**: Utilizes the Gemini API for advanced OCR to extract detailed information from business card images.
- **Database Management**: Enables saving, viewing, editing, and deleting business card information in an SQLite database.
- **Interactive Web Application**: Streamlit-based app providing a user-friendly interface for business card management.

## Why Google Generative AI (Gemini)?

Google Generative AI (Gemini) was selected for its robust OCR capabilities, allowing for accurate extraction of text from images. This tool was essential in achieving high accuracy in extracting and processing business card details, ensuring reliable and actionable information.

## Repository Contents

- **`ocr.py`**: Contains functions for interacting with Google Generative AI (Gemini) to extract information from business card images.
- **`db.py`**: Manages database operations including creating tables, inserting, updating, deleting, and retrieving records.
- **`app.py`**: The Streamlit application script for uploading images, displaying extracted data, and managing records.
- **`helper.py`**: Includes utility functions for encoding and decoding images.
- **`.env`**: Stores the API key for Google Generative AI (Gemini).
- **`requirements.txt`**: Lists the Python packages necessary to run the project.
- **`.gitignore`**: Specifies files and directories to be excluded from version control.

## Installation and Setup

To set up this project locally, follow these instructions:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Dinakara-Prabhu-A/Business-Card-OCR-Streamlit-Gemini.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Business-Card-OCR-Streamlit-Gemini
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
    - Create a `.env` file in the root directory.
    - Add your Google Generative AI API key to the `.env` file:
      ```plaintext
      API_KEY=your_google_generative_ai_api_key
      ```

5. **Run the Streamlit web application**:
    ```bash
    streamlit run app.py
    ```

## Usage Instructions

1. **Upload a Business Card**: Click the upload button to choose and upload an image of a business card. The image will be processed using the Gemini API.
2. **Extract and Save**: The extracted details will be displayed. Click "Save to Database" to store the information along with the image.
3. **View Records**: Use the "View" option to select a card holder's name and see their details.
4. **Edit Records**: To update a record, select it, make changes, and click "Update" to save the modifications.
5. **Delete Records**: Select a record and click "Delete" to remove it from the database.
6. **Refresh View**: Click the "Refresh" button to update the view with the latest records.
   

## Contribution Guidelines

I welcome feedback and suggestions! If you encounter any issues or have ideas for improvement, please feel free to open an issue or submit a pull request.

## Acknowledgements

- **Google Generative AI (Gemini)**: For providing advanced OCR capabilities for this project.
- **Open-Source Tools and Libraries**: This project was built using Python, Streamlit, and other essential libraries.

## Contact

For questions or feedback, please contact Dinakara Prabhu at [dinakaraprabhu1107@gmail.com](mailto:dinakaraprabhu1107@gmail.com).
