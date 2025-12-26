from utils import read_text_file
from preprocessing import clean_text

def extract_skills(text):
    """
    Extract skills from text by splitting words.
    In real projects, you can use a predefined skill set.
    """
    skills_list = ["python", "machine learning", "data science", "nlp",
                   "scikit-learn", "pandas", "numpy", "matplotlib", "tensorflow"]
    text = clean_text(text)
    found_skills = [skill for skill in skills_list if skill in text]
    return found_skills

def find_missing_skills(resume_path, jd_path):
    resume_text = read_text_file(resume_path)
    jd_text = read_text_file(jd_path)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing_skills = [skill for skill in jd_skills if skill not in resume_skills]
    return resume_skills, jd_skills, missing_skills

if __name__ == "__main__":
    resume_file = "../data/resumes/resume1.txt"
    jd_file = "../data/job_descriptions/jd1.txt"

    resume_skills, jd_skills, missing_skills = find_missing_skills(resume_file, jd_file)

    print(f"Resume Skills: {resume_skills}")
    print(f"Job Required Skills: {jd_skills}")
    print(f"Missing Skills: {missing_skills}")
