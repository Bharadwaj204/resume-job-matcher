from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

def train_tfidf_vectorizer():
    """
    Train and save a TF-IDF vectorizer
    """
    # Initialize the vectorizer
    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words='english',
        ngram_range=(1, 2)
    )
    
    # Sample texts for training (you can add more)
    sample_texts = [
        "python developer with experience in web development",
        "java developer with spring framework experience",
        "frontend developer with react and javascript",
        "backend developer with node.js and express",
        "full stack developer with python and javascript",
        "data scientist with machine learning experience",
        "devops engineer with aws and docker",
        "software engineer with java and spring boot",
        "web developer with html css and javascript",
        "mobile developer with react native"
    ]
    
    # Fit the vectorizer
    vectorizer.fit(sample_texts)
    
    # Save the vectorizer
    with open("tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    
    print("TF-IDF vectorizer trained and saved successfully!")

if __name__ == "__main__":
    train_tfidf_vectorizer()
