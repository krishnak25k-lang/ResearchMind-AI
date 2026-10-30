from src.pdf_loader import extract_text_from_pdf
from src.chunker import split_text_into_chunks
from src.embedding import create_embeddings
from src.vector_store import add_chunks


def index_uploaded_paper(pdf_path, paper_name):

    print(f"Processing: {paper_name}")

    # =========================================
    # 1. Extract PDF text
    # =========================================

    pages = extract_text_from_pdf(pdf_path)

    if not pages:
        raise ValueError(
            "No text could be extracted from the PDF."
        )

    # =========================================
    # 2. Create chunks
    # =========================================

    chunks_data = []

    chunk_counter = 0

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        if not text.strip():
            continue

        chunks = split_text_into_chunks(text)

        for chunk_text in chunks:

            chunk_id = (
                f"{paper_name}_"
                f"page_{page_number}_"
                f"chunk_{chunk_counter}"
            )

            chunks_data.append({
                "chunk_id": chunk_id,
                "text": chunk_text,
                "paper": paper_name,
                "page": page_number
            })

            chunk_counter += 1

    if not chunks_data:
        raise ValueError(
            "No usable text chunks were created."
        )

    # =========================================
    # 3. Extract text for embeddings
    # =========================================

    texts = [
        chunk["text"]
        for chunk in chunks_data
    ]

    # =========================================
    # 4. Generate embeddings
    # =========================================

    embeddings = create_embeddings(texts)

    # =========================================
    # 5. Store chunks + embeddings
    # =========================================

    add_chunks(
        chunks_data,
        embeddings
    )

    # =========================================
    # 6. Return result
    # =========================================

    return {
        "paper": paper_name,
        "pages": len(pages),
        "chunks": len(chunks_data)
    }