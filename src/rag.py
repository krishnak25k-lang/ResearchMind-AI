from src.embedding import create_embeddings
from src.vector_store import search_chunks
from src.llm import generate_answer


# ============================================================
# RESEARCHMIND RAG
# ============================================================

def ask_researchmind(
    question,
    selected_papers=None
):
    """
    Ask ResearchMind AI a question.

    If selected_papers is provided,
    retrieval is restricted to those papers.
    """

    # --------------------------------------------------------
    # VALIDATE QUESTION
    # --------------------------------------------------------

    if not question:

        return (
            "Please enter a research question.",
            []
        )

    question = question.strip()

    if not question:

        return (
            "Please enter a research question.",
            []
        )

    # --------------------------------------------------------
    # CREATE QUESTION EMBEDDING
    # --------------------------------------------------------

    query_embedding = create_embeddings(
        [question]
    )[0]

    # --------------------------------------------------------
    # SEARCH CHROMADB
    # --------------------------------------------------------

    results = search_chunks(
        query_embedding,
        n_results=5,
        selected_papers=selected_papers
    )

    # --------------------------------------------------------
    # GET DOCUMENTS
    # --------------------------------------------------------

    documents = results.get(
        "documents",
        []
    )

    metadatas = results.get(
        "metadatas",
        []
    )

    distances = results.get(
        "distances",
        []
    )

    # ChromaDB returns nested lists
    if documents:
        documents = documents[0]
    else:
        documents = []

    if metadatas:
        metadatas = metadatas[0]
    else:
        metadatas = []

    if distances:
        distances = distances[0]
    else:
        distances = []

    # --------------------------------------------------------
    # NO RESULTS
    # --------------------------------------------------------

    if not documents:

        if selected_papers:

            return (
                "No relevant information was found "
                "in the selected research papers.",
                []
            )

        return (
            "No relevant information was found "
            "in the indexed research papers.",
            []
        )

    # --------------------------------------------------------
    # BUILD CONTEXT
    # --------------------------------------------------------

    context_parts = []

    sources = []

    for index, document in enumerate(
        documents
    ):

        metadata = {}

        if index < len(metadatas):

            metadata = (
                metadatas[index]
                or {}
            )

        paper = metadata.get(
            "paper",
            "Unknown Paper"
        )

        page = metadata.get(
            "page",
            "Unknown"
        )

        context_parts.append(
            f"""
SOURCE:
Paper: {paper}
Page: {page}

CONTENT:
{document}
"""
        )

        sources.append(
            {
                "paper": paper,
                "page": page
            }
        )

    # --------------------------------------------------------
    # FINAL CONTEXT
    # --------------------------------------------------------

    context = "\n\n".join(
        context_parts
    )

    # --------------------------------------------------------
    # GENERATE ANSWER
    # --------------------------------------------------------

    answer = generate_answer(
        question,
        context
    )

    return (
        answer,
        sources
    )