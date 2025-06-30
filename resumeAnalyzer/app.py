import streamlit as st
import pdfplumber
import pandas as pd
from scoring_utils import score_resumes
import matplotlib.pyplot as plt

def extract_text(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

st.title("NLP Resume Screener")
job_desc = st.text_area("Paste the Job Description")
uploaded_files = st.file_uploader("Upload PDF Resumes", type="pdf", accept_multiple_files=True)

if st.button("Run Screening") and job_desc and uploaded_files:
    data = []
    for file in uploaded_files:
        text = extract_text(file)
        data.append({'name': file.name.replace('.pdf', ''), 'text': text})

    df = pd.DataFrame(data)
    df = score_resumes(df, job_desc)

    st.subheader("Ranking")
    st.dataframe(df[['name', 'final_score', 'matched_skills']])

    # Plotting bar chart
    import matplotlib.pyplot as plt
    st.subheader("Score Visualization")
    fig, ax = plt.subplots()
    ax.barh(df['name'], df['final_score'], color='skyblue')
    ax.set_xlabel("Final Score")
    ax.set_title("Resume Match Score")
    ax.invert_yaxis()
    st.pyplot(fig)
    import matplotlib.pyplot as plt

    st.subheader("Score Visualization")

    fig, ax = plt.subplots()
    ax.plot(df['name'], df['final_score'], marker='o', linestyle='-', color='skyblue')
    ax.set_xlabel("Resume Name")
    ax.set_ylabel("Final Score")
    ax.set_title("Resume Match Score (Line Chart)")
    ax.grid(True)
    st.pyplot(fig)

else:
    st.warning("Please enter a job description and upload at least one resume PDF.")