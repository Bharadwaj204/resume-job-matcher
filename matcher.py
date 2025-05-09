import pickle
from utils.text_extract import extract_text_from_pdf
from utils.nlp_utils import preprocess_text, extract_skills_from_text
from sklearn.metrics.pairwise import cosine_similarity
from utils.skills_db import SKILLS_DB

# Load pre-trained TF-IDF vectorizer
def load_tfidf_vectorizer():
    with open("tfidf_vectorizer.pkl", "rb") as f:
        return pickle.load(f)

def extract_skills_from_jd(jd_text):
    return extract_skills_from_text(jd_text)

def normalize_skills(skills):
    normalized = set()
    for skill in skills:
        skill = skill.lower()
        for main_skill, variations in SKILLS_DB.items():
            if skill in variations or skill == main_skill:
                normalized.add(main_skill)
                break
        else:
            normalized.add(skill)
    return list(normalized)

def analyze_resume_match(resume_pdf_path, job_description_path):
    # Load trained vectorizer
    vectorizer = load_tfidf_vectorizer()

    # Extract raw text
    resume_text = extract_text_from_pdf(resume_pdf_path)
    with open(job_description_path, 'r') as file:
        jd_text = file.read()

    # Preprocess both texts
    resume_clean = preprocess_text(resume_text)
    jd_clean = preprocess_text(jd_text)

    # Extract and normalize skills
    jd_skills = normalize_skills(extract_skills_from_text(jd_text))
    resume_skills = normalize_skills(extract_skills_from_text(resume_text))

    # Calculate skill match percentage
    matching_skills = set(jd_skills) & set(resume_skills)
    missing_skills = set(jd_skills) - set(resume_skills)
    skill_match_percentage = len(matching_skills) / len(jd_skills) if jd_skills else 0

    # Add skills multiple times to give them higher weight
    jd_weighted = jd_clean + " " + " ".join(jd_skills) * 3

    # Transform both into vectors
    tfidf_matrix = vectorizer.transform([resume_clean, jd_weighted])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    # Combine scores (70% cosine similarity, 30% skill match)
    final_score = (0.7 * cosine_sim[0][0]) + (0.3 * skill_match_percentage)

    return final_score, {
        "resume_preprocessed": resume_clean,
        "jd_preprocessed": jd_clean,
        "jd_skills": jd_skills,
        "resume_skills": resume_skills,
        "matching_skills": list(matching_skills),
        "missing_skills": list(missing_skills),
        "skill_match_percentage": skill_match_percentage,
        "tfidf_shape": tfidf_matrix.shape
    }
