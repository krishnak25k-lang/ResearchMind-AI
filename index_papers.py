import os

from src.pdf_loader import extract_pages_from_pdf
from src.chunker import create_chunks_from_pages
from src.embedding import create_embeddings
from src.vector_store import add_chunks


PAPERS_FOLDER = "data/papers"


all_chunks = []


for filename in os.listdir(PAPERS_FOLDER):

    if not filename.lower().endswith(".pdf"):
        continue

    pdf_path = os.path.join(
        PAPERS_FOLDER,
        filename
    )

    print(f"\nProcessing: {filename}")

    pages = extract_pages_from_pdf(
        pdf_path
    )

    chunks = create_chunks_from_pages(
        pages,
        filename
    )

    all_chunks.extend(chunks)


print("\nTotal chunks:", len(all_chunks))


texts = [
    chunk["text"]
    for chunk in all_chunks
]


embeddings = create_embeddings(
    texts
)


add_chunks(
    all_chunks,
    embeddings
)


print("\nAll research papers indexed successfully!")