# 💼 Resume Analyzer & Job Matcher


## 📌 Project Overview
This project is an intelligent resume analysis and job matching tool that helps both job seekers and recruiters. It uses Natural Language Processing (NLP) and machine learning techniques to analyze resumes and match them with job descriptions, providing detailed feedback and match scores.

## 🎯 Key Features
- **Resume Analysis**: Upload and analyze PDF resumes
- **Job Description Matching**: Compare resumes against job descriptions
- **Skill Extraction**: Automatically identify skills from both resumes and job descriptions
- **Match Scoring**: Calculate similarity scores using TF-IDF and cosine similarity
- **Detailed Feedback**: Get comprehensive feedback on matching and missing skills
- **User-Friendly Interface**: Simple and intuitive web interface built with Streamlit

## 🛠️ Technical Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Key Libraries**:
  - `streamlit`: Web interface
  - `pandas`: Data manipulation
  - `scikit-learn`: Machine learning and text processing
  - `PyPDF2`: PDF text extraction
  - `nltk`: Natural Language Processing
  - `python-docx`: Document processing

## 📋 Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Basic understanding of Python and web applications

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Bharadwaj204/resume-job-matcher.git
cd resume-job-matcher
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Running the Project**
 ```bash
   python train_vectorizer.py
```
## 💻 Usage

1. **Start the application**
```bash
streamlit run app.py
```

2. **Using the Application**
   - Open your web browser and go to `http://localhost:8501`
   - Upload your resume (PDF format)
   - Add job descriptions (text format)
   - View the matching results and feedback

## 🔍 How It Works

### 1. Text Extraction
- Extracts text from uploaded PDF resumes
- Processes job descriptions from text input

### 2. Text Processing
- Removes stopwords and punctuation
- Performs lemmatization
- Normalizes text for better matching

### 3. Skill Analysis
- Extracts skills from both resume and job description
- Normalizes skills to standard forms
- Identifies matching and missing skills

### 4. Matching Algorithm
- Uses TF-IDF vectorization
- Applies cosine similarity for matching
- Combines text similarity with skill matching

### 5. Results Display
- Shows overall match score
- Lists matching and missing skills
- Provides skill match percentage
- Offers improvement suggestions

## 📊 Output Format
The system provides:
- Overall match score (percentage)
- Matching skills list
- Missing skills list
- Skill match percentage
- Color-coded feedback:
  - 🟢 Green: Strong match (>70%)
  - 🟡 Yellow: Moderate match (50-70%)
  - 🔴 Red: Low match (<50%)

## 📈 Future Improvements
1. Support for more file formats (DOCX, RTF)
2. Enhanced skill detection
3. Resume writing suggestions
4. Multiple language support
5. Batch processing capability
6. API integration options
7. Advanced analytics dashboard

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details

## 👥 Authors
- [Bharadwaj204](https://github.com/Bharadwaj204)
- Contributors

## 🙏 Acknowledgments
- Thanks to all contributors
- Inspired by the need for better resume matching tools
- Built with open-source technologies

## 📞 Support
For support, please:
1. Check the documentation
2. Open an issue
3. Contact the maintainers
