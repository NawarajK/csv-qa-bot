# CSV Q&A Bot

This project is a Question & Answering bot that can answer questions based on the data in a CSV file.

## Progress

*   **Step 1: Project Setup:** Initialized the project, created the basic file structure, and installed dependencies.
*   **Step 2: Basic Streamlit App:** Created a basic Streamlit application to serve as the foundation for the bot.
*   **Step 3: CSV File Upload:** Added a file uploader to allow users to upload their CSV files.
*   **Step 4: Question Input:** Added a text input field for users to ask questions.
*   **Step 5: OpenAI Integration:** Integrated the OpenAI API with `langchain` to answer questions based on the CSV data.
*   **Step 6: Secure API Key Management:** Implemented a secure method for managing the OpenAI API key using environment variables and a `.env` file.
*   **Step 7: "Thinking" Indicator:** Added a spinner to show when the AI is processing a question, improving user feedback.
*   **Step 8: Error Handling:** Implemented `try...except` blocks to gracefully handle potential errors during file upload and AI processing, making the app more robust.
*   **Step 9: Code Refactoring and UI Intro:** Reorganized the code into functions for better readability and maintainability, and added an introductory message to the app's UI.
*   **Step 10: Conversation History:** Implemented session state to keep track of and display the conversation history.

## Features

*   Load a CSV file.
*   Ask questions in natural language about the data in the CSV.
*   Get answers from the bot.

## Security

The OpenAI API key is loaded from a `.env` file for local development. This file is included in the `.gitignore` file to ensure that your secret key is never committed to version control.

For deployed apps on Streamlit Community Cloud, the key should be stored in the app's Secrets.

## Getting Started (Local Development)

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.x
*   pip
*   OpenAI API Key

### Installation

1.  Clone the repository.
2.  Navigate to the project directory:
    ```sh
    cd csv-qa-bot
    ```
3.  Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```
4.  **Set up your API Key:**
    *   In the project folder, create a new file named `.env`.
    *   Copy the content from `.env.example` and paste it into your new `.env` file.
    *   Replace `"YOUR_API_KEY_HERE"` with your actual OpenAI API key.

### Usage

1.  Run the application:
    ```sh
    streamlit run app.py
    ```
2.  Upload your CSV file.
3.  Ask a question in the text input field.

## Deployment

This application can be deployed for free on the Streamlit Community Cloud.

### 1. Create a GitHub Repository

Your app needs to be in a public GitHub repository.

1.  Go to [GitHub](https://github.com/) and create a new public repository.
2.  Follow the instructions below to push your local project to this new repository.

### 2. Push Your Code to GitHub

Open a terminal or command prompt on your computer and navigate to your project folder:

```sh
cd C:\Users\Nawaraj karki\python_Project_Beginner\HelloWorld!\csv-qa-bot
```

Then, run the following Git commands:

```sh
# Add all your files to be tracked by Git
git add .

# Create a snapshot of your project
git commit -m "Ready for deployment"

# Link your local project to your GitHub repository
# Replace YOUR_USERNAME and YOUR_REPOSITORY_NAME with your actual GitHub details
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

# Push your code to GitHub
git push -u origin main
```

### 3. Deploy on Streamlit Community Cloud

1.  Go to the [Streamlit Community Cloud](https://streamlit.io/cloud) and sign up or log in.
2.  Click the "**New app**" button.
3.  Choose the GitHub repository you just created.
4.  The "Main file path" should be `app.py`.
5.  Before deploying, go to the "**Advanced settings**" and add your OpenAI API key in the "**Secrets**" section.
    *   **Secret name:** `OPENAI_API_KEY`
    *   **Secret value:** Paste your actual OpenAI API key here.
6.  Click "**Save**" and then click the "**Deploy!**" button.

Streamlit will then build your application and give you a public URL.
