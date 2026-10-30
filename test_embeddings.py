from src.pdf_loader import extract_text_from_pdf
from src.chunker import split_text_into_chunks
from src.embedding import create_embeddings


# --------------------------------
# 1. Load PDF
# --------------------------------

pdf_path = "data/papers/paper1.pdf"

text = extract_text_from_pdf(pdf_path)


# --------------------------------
# 2. Create chunks
# --------------------------------

chunks = split_text_into_chunks(
    text,
    chunk_size=1000,
    chunk_overlap=200
)


# --------------------------------
# 3. Create embeddings
# --------------------------------

embeddings = create_embeddings(chunks)


# --------------------------------
# 4. Display results
# --------------------------------

print("Number of chunks:", len(chunks))

print("Embedding shape:", embeddings.shape)

print("\nFirst chunk:")
print(chunks[0])

print("\nFirst embedding:")
print(embeddings[0])