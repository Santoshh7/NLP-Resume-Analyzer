import os
import pdfplumber
import pandas as pd

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def load_resumes_from_folder(folder_path='resumes/'):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(os.path.join(folder_path, filename))
            data.append({'name': filename.replace('.pdf', ''), 'text': text})
    return pd.DataFrame(data)
