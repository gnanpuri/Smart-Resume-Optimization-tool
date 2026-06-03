import os
from groq import Groq
from dotenv import load_dotenv

# Load .env file FIRST before anything else
load_dotenv()

# Check if key is loaded
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

# Initialize Groq client
client = Groq(api_key=api_key)

def analyze_resume(resume_chunks, job_description):
    """Send resume chunks + job description to Groq for analysis"""
    
    # Combine resume chunks into one text
    resume_text = "\n".join(resume_chunks)
    
    # Build the prompt
    prompt = f"""
You are an expert resume coach and HR specialist.

Here is the candidate's resume:
{resume_text}

Here is the job description they are applying for:
{job_description}

Please analyze and provide:

1. MATCH SCORE: Give a percentage (0-100%) of how well the resume matches the job description. Be realistic.

2. STRONG POINTS: List 3-5 things the candidate does well that match the job requirements.

3. MISSING KEYWORDS: List important keywords/skills from the job description that are missing from the resume.

4. IMPROVEMENT SUGGESTIONS: For each weak or missing area, suggest a specific improved bullet point the candidate can add or replace in their resume.

5. OVERALL ADVICE: Give 2-3 sentences of overall advice for this application.

Be specific, constructive and helpful.
"""

    # Send to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume coach and HR specialist who helps candidates optimize their resumes for specific job descriptions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=2000
    )
    
    return response.choices[0].message.content