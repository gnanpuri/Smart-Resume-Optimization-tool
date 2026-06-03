import docx
import PyPDF2

def extract_text_from_docx(file):
    """Extract text from a Word document"""
    doc = docx.Document(file)
    full_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            full_text.append(paragraph.text)
    return "\n".join(full_text)

def extract_text_from_pdf(file):
    """Extract text from a PDF file"""
    pdf_reader = PyPDF2.PdfReader(file)
    full_text = []
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            full_text.append(text)
    return "\n".join(full_text)

def parse_resume(uploaded_file):
    """Detect file type and extract text accordingly"""
    filename = uploaded_file.name.lower()
    
    if filename.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    elif filename.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    else:
        return None