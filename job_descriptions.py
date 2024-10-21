# Job descriptions for different domains
JOB_DESCRIPTIONS = {
"Data Scientist":"""We are looking for a Data Scientist with experience in machine learning, data analysis, and statistical modeling. 
The ideal candidate will have a strong background in Python and SQL, and familiarity with data visualization tools like Tableau.
Excellent communication skills and a problem-solving mindset are essential for this role.""",
"IT": "We are looking for a software developer with skills in Python, Java, and cloud technologies...",
"Healthcare": "We seek a healthcare professional with experience in patient care, hospital management...",
"Finance": "A financial analyst is needed with experience in accounting, investments, and risk management...",
"Marketing": "We are hiring a marketing manager experienced in digital marketing, SEO, and brand strategy...",
"Engineering": "We need a mechanical engineer with CAD experience, problem-solving skills,and project management..."
}

#get the job description based on domain
def get_job_description(domain):
    return JOB_DESCRIPTIONS.get(domain,"")