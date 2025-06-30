from resume_parser import load_resumes_from_folder
from scoring_utils import score_resumes
from visualize import plot_scores

job_description = """Paste your job description here"""

df = load_resumes_from_folder('resumes/')
df = score_resumes(df, job_description)

print(df[['name', 'final_score', 'matched_skills']])
plot_scores(df)
