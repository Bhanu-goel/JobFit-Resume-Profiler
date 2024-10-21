import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
import nltk
from nltk.corpus import stopwords
from app import get_job_description

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

nlp = spacy.load('en_core_web_sm')

def extract_keywords_ats(job_description):
    job_description = job_description.lower().strip()
    
    doc = nlp(job_description)
    
    entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PERSON', 'GPE', 'LOC', 'PRODUCT', 'NORP']]
    
    rake = Rake(stopwords=stop_words)
    rake.extract_keywords_from_text(job_description)
    rake_keywords = rake.get_ranked_phrases_with_scores()
    
    filtered_rake_keywords = [(score,phrase) for score,phrase in rake_keywords if len(phrase.split()) > 1]
    
    
    # vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1,2))
    # x = vectorizer.fit_transform([job_description])
    # tfidf_scores = x.toarray()[0]
    
    # tfidf_keywords = sorted(zip(vectorizer.get_feature_names_out(),tfidf_scores),key = lambda x:x[1],reverse = True)
    
    # ats_keywords = set(entities + filtered_rake_keywords + [keyword for keyword in tfidf_keywords[:10]])
    
    return filtered_rake_keywords

domain = 'Data Scientist'
job_desc = get_job_description(domain)
keywords = extract_keywords_ats(job_desc)

# Print the results
print("Optimized ATS Keywords:")
for score,phrase in keywords:
    print(f"phrase : {phrase} - score :  {score}")
    
ats_score = sum([score for score,phrase in keywords])
print(f"ATS Score : {ats_score}")
