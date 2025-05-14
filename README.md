# ATS Resume Expert

This is a Streamlit application that helps you analyze your resume against a job description using the Google Gemini AI model. It can provide an evaluation of your resume from an HR perspective and estimate a percentage match based on ATS (Applicant Tracking System) criteria.

## Features

* **Job Description Input:** Easily paste the job description into a text area.
* **Resume Upload:** Upload your resume in PDF format.
* **Resume Evaluation:** Get a professional HR evaluation highlighting the strengths and weaknesses of your resume in relation to the job description.
* **Percentage Match & Insights:** Receive an estimated percentage match, identify missing keywords, and get final thoughts from an ATS perspective.
* **Gemini Model Selection:** Choose from the available Google Gemini models (text-based) via a sidebar dropdown.
* **Clear User Interface:** Utilizes Streamlit's layout features (columns, tabs, sidebar) for a better user experience.
* **Instructions Tab:** Provides a guide on how to use the application effectively.

## Prerequisites

* **Python 3.6+**
* **pip** (Python package installer)
* **Google Cloud Account and Gemini API Key:** You need to obtain a Google Gemini API key. Ensure the key has access to a text-based model (e.g., `gemini-pro`).
* **`.env` File:** You will need to create a `.env` file to securely store your API key.

## Setup

1.  **Clone the Repository (if you have one):**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Create a `.env` file:**
    In the root directory of your project, create a file named `.env` and add your Google Gemini API key:
    ```
    GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
    ```
    Replace `YOUR_GOOGLE_API_KEY` with your actual API key.

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    If you don't have a `requirements.txt` file yet, create one with the following content:
    ```
    streamlit
    python-dotenv
    PyPDF2
    google-generativeai
    ```
    Then run the `pip install -r requirements.txt` command.

## Running the Application

1.  Navigate to the root directory of your project in your terminal.
2.  Run the Streamlit application:
    ```bash
    streamlit run your_script_name.py
    ```
    Replace `your_script_name.py` with the name of your Python file (e.g., `app.py`).

3.  The application will open in your web browser.

## Usage

1.  **Enter Job Description:** Paste the job description into the "Job Description" text area.
2.  **Upload Resume:** Click "Browse files" and select your resume in PDF format.
3.  **Evaluate Resume:** Click the "Evaluate Resume" button for an HR-style analysis.
4.  **Percentage Match & Insights:** Click the "Percentage Match & Insights" button for an ATS-focused evaluation.
5.  **Model Selection (Sidebar):** Choose your preferred Gemini model from the dropdown in the left sidebar.
6.  Refer to the "Instructions" tab within the application for more detailed guidance.

## Deployment to GitHub Pages (Optional - for static hosting)

Deploying a Streamlit app with backend logic (like API calls) directly to GitHub Pages can be tricky as it's designed for static content. However, you can host the code on GitHub for sharing. For a live, running application, you would typically need a platform that supports Python applications (e.g., Streamlit Community Cloud, Heroku, Google Cloud Run, etc.).

If you still want to include information for potential static hosting or sharing the code:

1.  **Ensure your code is in a GitHub repository.**
2.  **(For static content only - this won't run the Streamlit app live):** You might need to configure your repository for GitHub Pages in the repository settings. This usually works best for static HTML, CSS, and JavaScript. Streamlit apps require a running Python environment.

**For actual deployment, consider platforms like:**

* **Streamlit Community Cloud:** Free and specifically designed for Streamlit apps.
* **Heroku:** A platform as a service (PaaS) that can host Python applications.
* **Google Cloud Run:** A fully managed serverless platform for containerized applications.
* **AWS App Runner:** A fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs at scale.

Refer to the documentation of these platforms for specific deployment instructions.

## Contributing

If you'd like to contribute to this project, feel free to open issues or submit pull requests.

## License

[Your License (e.g., MIT License)](LICENSE) - Add a `LICENSE` file to your repository with the appropriate license.

## Acknowledgements

* [Streamlit](https://streamlit.io/) for the easy-to-use framework.
* [Google Gemini API](https://ai.google.dev/) for the powerful AI model.
* [PyPDF2](https://pypdf2.readthedocs.io/en/stable/) for PDF processing.
* [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
