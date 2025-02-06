import streamlit as st
import os
import glob
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  
REPORTS_FOLDER = BASE_DIR / "reports"


if not REPORTS_FOLDER.exists():
    st.error(f"⚠️ Reports folder does not exist: {REPORTS_FOLDER}")
else:

    md_files = sorted(REPORTS_FOLDER.glob("*.md"))  

    if not md_files:
        st.warning("⚠️ No report files found in the 'reports' folder.")
    else:

        md_filenames = [md_file.name for md_file in md_files]

     
        selected_md_filename = st.selectbox("📑 Select Report:", md_filenames)

  
        selected_md_file = REPORTS_FOLDER / selected_md_filename

        st.subheader(f"📑 Viewing: {selected_md_filename}")

        with open(selected_md_file, "r", encoding="utf-8") as file:
            markdown_content = file.read()
        
        cleaned_markdown = markdown_content.replace("```", "")  
        st.markdown(cleaned_markdown, unsafe_allow_html=True)
