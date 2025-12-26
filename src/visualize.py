import os
import matplotlib.pyplot as plt
from skill_gap import find_missing_skills

# Determine the repo root dynamically
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to data
resume_file = os.path.join(repo_root, "data/resumes/resume1.txt")
jd_file = os.path.join(repo_root, "data/job_descriptions/jd1.txt")

# Compute skill gap
resume_skills, jd_skills, missing_skills = find_missing_skills(resume_file, jd_file)
match_percentage = round((len(resume_skills) / len(jd_skills)) * 100, 2)

# Plot bar chart
skills = ["Matched Skills", "Missing Skills"]
counts = [len(resume_skills), len(missing_skills)]
plt.bar(skills, counts, color=["green", "red"])
plt.title(f"Resume-JD Skill Match: {match_percentage}%")
plt.ylabel("Number of Skills")

# Ensure screenshots folder exists
screenshots_dir = os.path.join(repo_root, "screenshots")
os.makedirs(screenshots_dir, exist_ok=True)

# Save chart
plt.savefig(os.path.join(screenshots_dir, "skill_gap_demo.png"))
plt.show()

print(f"Chart saved to {os.path.join(screenshots_dir, 'skill_gap_demo.png')}")

