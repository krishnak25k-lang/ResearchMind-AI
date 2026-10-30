import chromadb


# ============================================================
# CHROMADB CLIENT
# ============================================================

client = chromadb.PersistentClient(
    path="data/chroma_db"
)


# ============================================================
# COLLECTION
# ============================================================

collection = client.get_or_create_collection(
    name="research_papers"
)


# ============================================================
# ADD CHUNKS
# ============================================================

def add_chunks(chunks, embeddings):

    ids = []
    documents = []
    metadatas = []

    for chunk in chunks:

        ids.append(
            chunk["chunk_id"]
        )

        documents.append(
            chunk["text"]
        )

        metadatas.append(
            {
                "paper": chunk["paper"],
                "page": chunk["page"]
            }
        )

    if not ids:
        return

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


# ============================================================
# SEARCH ALL PAPERS
# ============================================================

def search_chunks(
    query_embedding,
    n_results=5,
    selected_papers=None
):

    query_kwargs = {
        "query_embeddings": query_embedding.tolist(),
        "n_results": n_results,
        "include": [
            "documents",
            "metadatas",
            "distances"
        ]
    }

    # --------------------------------------------------------
    # FILTER SELECTED PAPERS
    # --------------------------------------------------------

    if selected_papers:

        query_kwargs["where"] = {
            "paper": {
                "$in": selected_papers
            }
        }

    results = collection.query(
        **query_kwargs
    )

    return results


# ============================================================
# GET ALL METADATA
# ============================================================

def get_all_metadata():

    results = collection.get(
        include=[
            "metadatas"
        ]
    )

    return results


# ============================================================
# GET ALL PAPER NAMES
# ============================================================

def get_all_papers():

    results = collection.get(
        include=[
            "metadatas"
        ]
    )

    metadatas = results.get(
        "metadatas",
        []
    )

    papers = set()

    for metadata in metadatas:

        if not metadata:
            continue

        paper = metadata.get(
            "paper"
        )

        if paper:
            papers.add(
                paper
            )

    return sorted(
        papers
    )


# ============================================================
# GET CHUNK COUNT
# ============================================================

def get_collection_count():

    return collection.count()