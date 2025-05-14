import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def list_available_models():
    models = [model.name for model in genai.list_models()]
    return models

def get_gemini_response(input_text, prompt, model_name):
    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content([input_text, prompt])
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

def input_pdf_to_text(uploaded_file):
    if uploaded_file is not None:
        try:
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert", layout="wide")
st.title("ATS Resume Expert")

with st.sidebar:
    st.header("Configuration")
    available_models = list_available_models()
    default_model = next((model for model in available_models if 'gemini-pro' in model.lower() and 'vision' not in model.lower()), None)
    if not default_model and available_models:
        default_model = available_models[0]
    selected_model = st.selectbox("Select Gemini Model", available_models, index=available_models.index(default_model) if default_model else 0)
    st.info(f"Selected Model: **{selected_model}**")

tab1, tab2 = st.tabs(["Analyze Resume", "Instructions"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        job_description = st.text_area("Job Description:", key="input", height=300)
        uploaded_file = st.file_uploader("Upload your resume (PDF):", type=["pdf"])
        if uploaded_file:
            st.success("PDF Uploaded Successfully")

    with col2:
        st.subheader("Analysis")
        response_area = st.empty()
        col_buttons = st.columns(2)
        with col_buttons[0]:
            submit_evaluate = st.button("Evaluate Resume")
        with col_buttons[1]:
            submit_percentage = st.button("Percentage Match & Insights")

        input_prompt_evaluate = """
        You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description.
        Please share your professional evaluation on whether the candidate's profile aligns with the role.
        Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
        """

        input_prompt_percentage = """
        You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
        your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
        the job description. First the output should come as percentage, then keywords missing, and lastly final thoughts.
        """

        if submit_evaluate:
            if uploaded_file and job_description:
                with st.spinner("Evaluating Resume..."):
                    pdf_text = input_pdf_to_text(uploaded_file)
                    if pdf_text:
                        response = get_gemini_response(job_description, input_prompt_evaluate + "\n\nResume Text:\n" + pdf_text, selected_model)
                        response_area.markdown("### Evaluation:")
                        response_area.write(response)
            elif not uploaded_file:
                st.warning("Please upload the resume.")
            elif not job_description:
                st.warning("Please enter the job description.")

        elif submit_percentage:
            if uploaded_file and job_description:
                with st.spinner("Calculating Percentage Match & Insights..."):
                    pdf_text = input_pdf_to_text(uploaded_file)
                    if pdf_text:
                        response = get_gemini_response(job_description, input_prompt_percentage + "\n\nResume Text:\n" + pdf_text, selected_model)
                        response_area.markdown("### Percentage Match & Insights:")
                        response_area.write(response)
            elif not uploaded_file:
                st.warning("Please upload the resume.")
            elif not job_description:
                st.warning("Please enter the job description.")

with tab2:
    st.header("How to Use")
    st.markdown("""
    1.  **Enter the Job Description:** Carefully paste the full job description into the text area on the left.
    2.  **Upload Your Resume:** Click on the "Browse files" button and select your resume in PDF format.
    3.  **Evaluate Resume:** Click the "Evaluate Resume" button for a professional HR perspective on how well your resume aligns with the job description, including strengths and weaknesses.
    4.  **Percentage Match & Insights:** Click the "Percentage Match & Insights" button to get an estimated percentage match, identify missing keywords, and receive final thoughts from an ATS perspective.
    5.  **Configuration (Sidebar):** In the left sidebar, you can see the available Gemini models and select a different one if needed. The selected model is displayed at the bottom of the sidebar.

    **Tips for Best Results:**
    * Ensure the job description is complete and accurate.
    * Upload your resume in a clear, text-readable PDF format.
    * Review the generated feedback to understand areas for improvement.
    """)