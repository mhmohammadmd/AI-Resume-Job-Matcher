from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import read_text_file
from preprocessing import clean_text

def compute_match(resume_path, jd_path):
    # Read files
    resume_text = read_text_file(resume_path)
    jd_text = read_text_file(jd_path)

    # Preprocess
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    # Cosine Similarity
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    match_score = round(similarity[0][0] * 100, 2)

    return match_score

if __name__ == "__main__":
    resume_file = "../data/resumes/resume1.txt"
    jd_file = "../data/job_descriptions/jd1.txt"
    score = compute_match(resume_file, jd_file)
    print(f"Resume-JD Match Score: {score}%")
