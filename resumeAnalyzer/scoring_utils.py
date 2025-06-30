from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
skills = ['python', 'sql', 'pandas', 'numpy', 'machine learning']

def embed_texts(texts):
    return model.encode(texts)

def compute_cosine_scores(resume_embeddings, job_embedding):
    return cosine_similarity(resume_embeddings, job_embedding).flatten()

def match_skills(text):
    return [skill for skill in skills if skill.lower() in text.lower()]

def score_resumes(df, job_description):
    resume_embeddings = embed_texts(df['text'].tolist())
    job_embedding = embed_texts([job_description])
    df['cosine_score'] = compute_cosine_scores(resume_embeddings, job_embedding)
    df['matched_skills'] = df['text'].apply(match_skills)
    df['num_matches'] = df['matched_skills'].apply(len)
    df['keyword_score'] = df['num_matches'] / len(skills)
    df['cosine_score_norm'] = (df['cosine_score'] - df['cosine_score'].min()) / (df['cosine_score'].max() - df['cosine_score'].min())
    df['final_score'] = 0.7 * df['cosine_score_norm'] + 0.3 * df['keyword_score']
    return df.sort_values('final_score', ascending=False)
