import PyPDF2
import os
def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
    abs_path = os.path.join(base_dir, pdf_path)
    text = ""
    with open(abs_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()


def load_text_file(file_path):
    """Loads text from a file using an absolute path."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
    abs_path = os.path.join(base_dir, file_path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")

    with open(abs_path, "r", encoding="utf-8") as file:
        return file.read().strip()
