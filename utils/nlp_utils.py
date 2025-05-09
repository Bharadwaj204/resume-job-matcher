import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess text by removing special characters, converting to lowercase,
    and removing extra spaces
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(filtered_tokens)

def extract_skills_from_text(text):
    """
    Extract skills from text using basic pattern matching
    """
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Common skill indicators
    skill_indicators = ['proficient in', 'skilled in', 'experience with', 'knowledge of', 'expertise in']
    
    skills = set()
    
    # Extract skills after skill indicators
    for i, word in enumerate(words):
        for indicator in skill_indicators:
            if ' '.join(words[i:i+len(indicator.split())]) == indicator:
                # Get the next word as a potential skill
                if i + len(indicator.split()) < len(words):
                    skill = words[i + len(indicator.split())]
                    skills.add(skill)
    
    # Add standalone technical terms
    technical_terms = ['python', 'java', 'javascript', 'sql', 'html', 'css', 'react', 'node', 'aws', 'docker']
    for term in technical_terms:
        if term in words:
            skills.add(term)
    
    return list(skills)
