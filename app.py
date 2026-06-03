import streamlit as st
from resume_parser import parse_resume
from vector_store import store_resume, search_resume
from analyzer import analyze_resume
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Smart Resume Optimizer",
    page_icon="📄",
    layout="wide"
)

# Header
st.title("📄 Smart Resume Optimizer")
st.markdown("Upload your resume and paste a job description to get AI-powered optimization suggestions!")
st.divider()

# Two column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Choose your resume file",
        type=["pdf", "docx"],
        help="Supported formats: PDF, DOCX"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")

with col2:
    st.subheader("📋 Paste Job Description")
    job_description = st.text_area(
        "Paste the full job description here",
        height=200,
        placeholder="Copy and paste the job description you are applying for..."
    )

st.divider()

# Analyze button
if st.button("🚀 Analyze My Resume", type="primary", use_container_width=True):
    
    # Validation
    if not uploaded_file:
        st.error("⚠️ Please upload your resume first!")
    elif not job_description.strip():
        st.error("⚠️ Please paste a job description!")
    else:
        
        # Step 1: Parse resume
        with st.spinner("📄 Reading your resume..."):
            resume_text = parse_resume(uploaded_file)
            
            if not resume_text:
                st.error("❌ Could not read the file. Please try a different format.")
                st.stop()
        
        # Step 2: Store in ChromaDB
        with st.spinner("🧠 Processing and storing in vector database..."):
            collection, chunks = store_resume(resume_text)
        
        # Step 3: Search relevant chunks
        with st.spinner("🔍 Finding relevant resume sections..."):
            relevant_chunks = search_resume(job_description, collection)
        
        # Step 4: Analyze with Groq
        with st.spinner("🤖 AI is analyzing your resume..."):
            analysis = analyze_resume(relevant_chunks, job_description)
        
        # Step 5: Display results
        st.divider()
        st.subheader("📊 Analysis Results")
        
        # Display the full analysis
        st.markdown(analysis)
        
        st.divider()
        
        # Download button for results
        st.download_button(
            label="📥 Download Analysis Report",
            data=analysis,
            file_name="resume_analysis.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        st.success("✅ Analysis complete! Review the suggestions above to optimize your resume.")