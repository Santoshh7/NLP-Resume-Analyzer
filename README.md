# NLP-Resume-Analyzer
This project screens multiple resumes using NLP by comparing them to a given job description. It uses keyword matching and sentence embeddings to compute relevance scores and displays results with a ranking table and bar chart visualization.
A smart resume screening tool built using NLP and machine learning. It evaluates resumes against a given job description and ranks them based on skill match and semantic similarity.

---
🔗 [Live Demo on Streamlit](https://nlp-resume-analyzer-qjjxatrddetn96uqjne8vj.streamlit.app/)

## 🚀 Features

- Upload multiple PDF resumes
- Paste a custom job description
- Extracts text from resumes using `pdfplumber`
- Computes similarity using `sentence-transformers`
- Matches job-relevant keywords (e.g., Python, SQL, Pandas, etc.)
- Combines keyword match + semantic similarity into a final score
- **Interactive ranking table**
- **Bar chart visualization** for resume scores
- Easy-to-use Streamlit interface

---

 📊 Visualizations

The app shows:
- A ranking table with scores and matched skills  
- A horizontal bar graph comparing final scores of all candidates  

Additional visualizations like **pie charts**, **line graphs**, or **skill heatmaps** can be easily added for deeper insights.

---

🛠️ Tech Stack

- Python
- Pandas, NumPy
- pdfplumber (PDF parsing)
- sentence-transformers (NLP embeddings)
- scikit-learn (similarity)
- Matplotlib (visualization)
- Streamlit (web interface)

