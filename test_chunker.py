from src.pdf_loader import extract_text_from_pdf
from src.chunker import split_text_into_chunks


# PDF location
pdf_path = "data/papers/paper1.pdf"


# Step 1: Extract text
text = extract_text_from_pdf(pdf_path)


# Step 2: Create chunks
chunks = split_text_into_chunks(
    text,
    chunk_size=2000,
    chunk_overlap=300
)


# Display information
print("Total characters:", len(text))
print("Total chunks:", len(chunks))


# Display first 5 chunks
for i, chunk in enumerate(chunks[:5], start=1):

    print("\n")
    print("=" * 60)
    print(f"CHUNK {i}")
    print("=" * 60)

    print(chunk)