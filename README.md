# AI-Resume-Job-Matcher

An AI/ML-powered project that **automatically matches resumes with job descriptions**, detects **skill gaps**, and visualizes the results for recruiters or job seekers.  

---

## **Features**

- ✅ **Resume-JD Match Score**: Calculates similarity between resume and job description using **TF-IDF** and **Cosine Similarity**  
- ✅ **Skill Gap Detection**: Identifies missing skills required for a job  
- ✅ **Visualization**: Bar chart showing matched vs missing skills for quick insights  
- ✅ **Expandable**: Add more resumes and job descriptions easily  

---

## **Project Structure**


📂 **AI-Resume-Job-Matcher**  
├── 📂 **data**  
│   ├── 📂 **resumes/** – Store resume text files here  
│   └── 📂 **job_descriptions/** – Store job description text files here  
├── 📂 **src**  
│   ├── 📄 **matcher.py** – Calculates resume-JD match score  
│   ├── 📄 **skill_gap.py** – Detects missing skills  
│   ├── 📄 **visualize.py** – Generates skill gap visualization  
│   ├── 📄 **preprocessing.py** – Text cleaning functions  
│   └── 📄 **utils.py** – File reading utilities  
├── 📄 **README.md** – Project overview  
└── 📄 **requirements.txt** – Python dependencies  

---
##**Technologies Used**
1. Python 3.11
2. Pandas, NumPy
3. Scikit-learn (TF-IDF, Cosine Similarity)
4. Matplotlib (Visualization)

#**Demo Screenshot**
<img width="786" height="667" alt="image" src="https://github.com/user-attachments/assets/b87a940b-a5c8-4c59-9da4-5d06eb884e7e" />

#**Future Improvements**
1. Use NLP Named Entity Recognition to extract skills dynamically
2. Build web interface using Streamlit or Flask
3. Support multiple resumes & JDs batch matching



