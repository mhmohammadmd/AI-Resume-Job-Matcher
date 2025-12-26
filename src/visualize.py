import matplotlib.pyplot as plt
from skill_gap import find_missing_skills

resume_file = "../data/resumes/resume1.txt"
jd_file = "../data/job_descriptions/jd1.txt"

resume_skills, jd_skills, missing_skills = find_missing_skills(resume_file, jd_file)

match_percentage = round((len(resume_skills)/len(jd_skills))*100, 2)

# Plot bar chart
skills = ["Matched Skills", "Missing Skills"]
counts = [len(resume_skills), len(missing_skills)]

plt.bar(skills, counts, color=["green", "red"])
plt.title(f"Resume-JD Skill Match: {match_percentage}%")
plt.ylabel("Number of Skills")
plt.savefig("../screenshots/skill_gap_demo.png")
plt.show()
