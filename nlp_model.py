from job_descriptions import get_job_description
import spacy

#NLP model 
#loading english nlp model
nlp = spacy.load("en_core_web_sm")

#function to extract keyword from job description
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return keywords

#testing
domain = 'IT'
job_description = get_job_description(domain)
job_keywords = extract_keywords(job_description)

# print(domain)
# print(job_description)
# print(job_keywords)

