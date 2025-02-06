from data_preprocessing import extract_text_from_pdf, load_text_file
from llm_analysis import process_job_description , extract_resume_info
from scoring import calculate_match_score_recommendations
import os
import glob

def main():
    print("Executing main.py...")
    jd_text = load_text_file("data/job_description.txt")

    if not jd_text.strip():
        print("Error: Job description file is empty!")
        return

    jd_info = process_job_description(jd_text)
    if not jd_info:
        print("Error: Failed to extract job description data from LLM!")
        return

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_folder = os.path.join(base_dir, "data", "resumes")
    reports_folder = os.path.join(base_dir, "reports")

    os.makedirs(reports_folder, exist_ok=True)
    resume_files = glob.glob(os.path.join(resume_folder, "*.pdf"))

    if not resume_files:
        print("Error: No resume files found in the folder!")
        return

    for resume_file in resume_files:
        resume_text = extract_text_from_pdf(resume_file)
        candidate_info = extract_resume_info(resume_text)
        match_score = calculate_match_score_recommendations(candidate_info, jd_info)

        resume_name = os.path.basename(resume_file).replace(".pdf", "")
        report_filename = f"{resume_name}.md"
        report_path = os.path.join(reports_folder, report_filename)

        with open(report_path, "w",encoding="utf-8") as f:
            f.write(match_score)

        print(f"Processed: {resume_name} -> Saved to: {report_path}")

