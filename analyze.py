from sklearn.feature_extraction.text import CountVectorizer
from job_descriptions import get_job_description
from nlp_model import extract_keywords
import streamlit as st

def analyze_resume(resume_content,domain):
    job_description = get_job_description(domain)
    
    resume_keywords = extract_keywords(resume_content)
    job_keywords = extract_keywords(job_description)
    
    score = calculate_match_score(resume_keywords,job_keywords)
    
    #display result
    st.write(f"resume match score for {domain} : {score}%")
    provide_feedback(resume_keywords,job_keywords)
    
def calculate_match_score(resume_keywords,job_keywords):
    vectorizer = CountVectorizer().fit_transform([",".join(resume_keywords),",".join(job_keywords)])
    vector = vectorizer.toarray()
    
    cosine_similarity = (vector[0] @ vector[1]) / (sum(vector[0])*sum(vector[1]))
    return round(cosine_similarity*100,2)

def provide_feedback(resume_keywords,job_keywords):
    missing_keywords = set(job_keywords) - set(resume_keywords)
    if missing_keywords:
        st.write("Consider adding these keywords to your resume:")
        st.write(",".join(missing_keywords))
    else:
        st.write("Your resume covers all important keywords.")