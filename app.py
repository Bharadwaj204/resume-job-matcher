import streamlit as st
import pandas as pd
from matcher import analyze_resume_match, extract_skills_from_jd
import tempfile
import os

# Streamlit UI
st.title("📄 Resume and Job Description Matcher")

# File upload section
st.write("### 📝 Upload Files")
col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type="pdf")
with col2:
    uploaded_job_descriptions = st.file_uploader("Upload Job Descriptions (Text)", type="txt", accept_multiple_files=True)

if uploaded_resume and uploaded_job_descriptions:
    # Create temporary directory for files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save uploaded files
        resume_path = os.path.join(temp_dir, uploaded_resume.name)
        with open(resume_path, "wb") as f:
            f.write(uploaded_resume.getbuffer())

        jd_paths = []
        for jd in uploaded_job_descriptions:
            temp_path = os.path.join(temp_dir, jd.name)
            with open(temp_path, "wb") as f:
                f.write(jd.getbuffer())
            jd_paths.append(temp_path)

        # Create results matrix
        results = []
        for jd_path, jd_name in zip(jd_paths, [jd.name for jd in uploaded_job_descriptions]):
            similarity_score, details = analyze_resume_match(resume_path, jd_path)
            results.append({
                'Job Description': jd_name,
                'Match Score': f"{similarity_score:.2%}",
                'Skills Match': f"{details['skill_match_percentage']:.2%}",
                'Matching Skills': len(details['matching_skills']),
                'Missing Skills': len(details['missing_skills'])
            })

        # Create and display results table
        df = pd.DataFrame(results)
        st.write("### 📊 Job Matches Overview")
        st.dataframe(df)

        # Sort results by match score
        df['Match Score'] = df['Match Score'].str.rstrip('%').astype('float') / 100
        df = df.sort_values('Match Score', ascending=False)
        
        # Display top matches
        st.write("### 🏆 Top Matches")
        for idx, row in df.head(3).iterrows():
            st.write(f"#### {row['Job Description']} - {row['Match Score']:.2%} Match")
            
            similarity_score, details = analyze_resume_match(resume_path, jd_paths[idx])
            
            if similarity_score > 0.7:
                st.success("✅ Strong match! Your resume aligns well with the job requirements.")
            elif similarity_score > 0.5:
                st.warning("⚠️ Moderate match. Some skills and experience match the requirements.")
            else:
                st.error("❌ Low match. Your resume may need significant improvements to match the job requirements.")

            # Display skills analysis
            st.write("##### 💼 Skills Analysis")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Matching Skills:**")
                for skill in details['matching_skills']:
                    st.success(f"✓ {skill}")
            
            with col2:
                st.write("**Missing Skills:**")
                for skill in details['missing_skills']:
                    st.error(f"✗ {skill}")

            # Display skill match percentage
            st.write(f"##### 📊 Skill Match: `{details['skill_match_percentage']:.2%}`")

            # Display preprocessed texts
            st.write("##### 📝 Preprocessed Text")
            st.write("**Resume:**")
            st.code(details['resume_preprocessed'])
            st.write("**Job Description:**")
            st.code(details['jd_preprocessed'])
            
            st.markdown("---")  # Add a separator between job matches
