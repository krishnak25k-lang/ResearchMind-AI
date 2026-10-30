from src.pdf_loader import extract_text_from_pdf

pdf_path = "data/papers/paper1.pdf" 

text = extract_text_from_pdf(pdf_path)

print(text[:5000])