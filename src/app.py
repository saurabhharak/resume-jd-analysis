import streamlit as st
import os
import glob
from main import main
import re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUME_FOLDER = os.path.join(BASE_DIR, "data", "resumes")
JD_PATH = os.path.join(BASE_DIR, "data", "job_description.txt")
REPORTS_FOLDER = os.path.join(BASE_DIR, "reports")

os.makedirs(RESUME_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)

st.title("📄 Resume & Job Description Processor")

st.subheader("📤 Upload Resume Files (PDFs)")
uploaded_resumes = st.file_uploader("Upload one or multiple resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_resumes:
    for resume in uploaded_resumes:
        resume_path = os.path.join(RESUME_FOLDER, resume.name)
        with open(resume_path, "wb") as f:
            f.write(resume.read())
    st.success(f"✅ {len(uploaded_resumes)} resume(s) uploaded successfully!")

st.subheader("📑 Enter Job Description")
jd_text = st.text_area("Paste or type the job description here:", height=200)

if jd_text:
    with open(JD_PATH, "w", encoding="utf-8") as f:
        f.write(jd_text)
    st.success("✅ Job description saved successfully!")

if st.button("🚀 Start Resume Processing"):

    if not glob.glob(os.path.join(RESUME_FOLDER, "*.pdf")):
        st.error("⚠️ No resumes found! Please upload resume files first.")
    elif not jd_text.strip():
        st.error("⚠️ Job description is empty! Please enter a job description.")
    else:
        st.success("✅ Resumes and Job Description are ready! Processing started...")

        with st.spinner("🔄 Running Resume Processing... Please wait."):
            try:
                main()  
                st.success("✅ Processing complete! Loading reports...")
                st.rerun()  
            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")

    st.page_link("pages/reports_viewer.py", label="📄 Open Resume Match Reports", icon="📑", new_tab=True)
