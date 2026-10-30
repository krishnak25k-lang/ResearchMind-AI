from src.pdf_loader import extract_pages_from_pdf
from src.chunker import create_chunks_from_pages
from src.embedding import create_embeddings
from src.vector_store import add_chunks


# --------------------------------
# PDF
# --------------------------------

pdf_path = "data/papers/paper1.pdf"

paper_name = "paper1.pdf"


# --------------------------------
# Extract pages
# --------------------------------

pages = extract_pages_from_pdf(
    pdf_path
)

print("Pages extracted:", len(pages))


# --------------------------------
# Create chunks
# --------------------------------

chunks = create_chunks_from_pages(
    pages,
    paper_name
)

print("Total chunks:", len(chunks))


# --------------------------------
# Extract text for embeddings
# --------------------------------

texts = [
    chunk["text"]
    for chunk in chunks
]


# --------------------------------
# Create embeddings
# --------------------------------

embeddings = create_embeddings(
    texts
)

print(
    "Embedding shape:",
    embeddings.shape
)


# --------------------------------
# Store in ChromaDB
# --------------------------------

add_chunks(
    chunks,
    embeddings
)


print("\nSuccessfully stored paper!")