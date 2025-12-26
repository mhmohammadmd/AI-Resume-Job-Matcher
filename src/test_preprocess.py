from utils import read_text_file
from preprocessing import clean_text

resume = read_text_file("../data/resumes/resume1.txt")
jd = read_text_file("../data/job_descriptions/jd1.txt")

print("Cleaned Resume:")
print(clean_text(resume))
print("\nCleaned Job Description:")
print(clean_text(jd))
