from app import get_job_description
import streamlit as st
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
import nltk

nltk.download('stopwords')
nltk.download('punkt_tab')

nlp = spacy.load("en_core_web_sm")

def extract_keywords(job_description):
    #using rake for keyword extraction
    rake = Rake()
    rake.extract_keywords_from_text(job_description)
    rake_keywords = rake.get_ranked_phrases_with_scores()
    
    #get keyword and score from rake
    rake_keywords_list = [(score,phase) for score,phase in rake_keywords]
    
    #using tfidf for keyword extraction
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([job_description])
    tfidf_scores = X.toarray()[0]
    
    #get feature names and their corresponding scores
    tfidf_keywords = sorted(zip(vectorizer.get_feature_names_out(),tfidf_scores), key = lambda x:x[1],reverse=True)
    
    #combine rake and tfidf results
    combined_keywords = {
        "RAKE" : rake_keywords_list,
        'TF-IDF' : tfidf_keywords[:10]
    }    
    
    return combined_keywords

#testing
domain = 'Data Scientist'
job_description = get_job_description(domain)
job_keywords = extract_keywords(job_description)

print(domain)
print(job_description)

# Print the results
print("Keywords extracted using RAKE:")
for score, phrase in job_keywords["RAKE"]:
    print(f"{phrase} (Score: {score})")

print("\nTop TF-IDF Keywords:")
for phrase, score in job_keywords["TF-IDF"]:
    print(f"{phrase} (Score: {score})")