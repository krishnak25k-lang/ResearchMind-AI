from src.pdf_loader import extract_text_from_pdf
from src.chunker import split_text_into_chunks
from src.embedding import create_embeddings
from src.vector_store import add_chunks


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


print("Number of chunks:", len(chunks))


# --------------------------------
# 3. Create embeddings
# --------------------------------

embeddings = create_embeddings(chunks)

print("Embedding shape:", embeddings.shape)


# --------------------------------
# 4. Store in ChromaDB
# --------------------------------

add_chunks(
    chunks,
    embeddings
)


print("Successfully stored chunks in ChromaDB!")