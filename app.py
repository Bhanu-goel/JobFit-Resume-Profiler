from job_descriptions import JOB_DESCRIPTIONS
from analyze import analyze_resume
import streamlit as st
import PyPDF2
import spacy

#function to build the user interface
def build_ui():
    st.title('JOBFIT RESUME PROFILER')
    st.write("Analyze your resume based on domain-specific job descriptions")
    
    #Resume upload
    uploaded_file = st.file_uploader('Upload your Resume (PDF or Text)',type=['pdf','txt'])
    
    #Job Domain Selection
    domain = st.selectbox("Choose your Job Domain",['IT',"Data Scientist",'Finance','Healthcare'])
    
    if uploaded_file is not None:
        st.success('Resume uploaded Successfully')
        
        #read file content
        resume_content = read_resume(uploaded_file)
        st.write("Resume Content Preview: ")
        #preview first 500 characters
        st.text(resume_content[:500]) 
        
        #call the function to analyze resume
        if st.button("Analyze Resume"):
            analyze_resume(resume_content,domain)
            
#read resume
def read_resume(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_pdf_text(uploaded_file)
    else:
        return str(uploaded_file.read(),"utf-8")

#function to extract text from pdf
def extract_pdf_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

#NLP model 
#loading english nlp model
nlp = spacy.load("en_core_web_sm")

if __name__ == "__main__":
    build_ui()