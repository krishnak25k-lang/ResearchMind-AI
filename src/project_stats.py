import os
import json


PAPERS_FOLDER = "data/papers"


def get_project_statistics():

    # ---------------------------------------
    # Count PDF files
    # ---------------------------------------

    papers = []

    if os.path.exists(PAPERS_FOLDER):

        for file in os.listdir(PAPERS_FOLDER):

            if file.lower().endswith(".pdf"):
                papers.append(file)

    paper_count = len(papers)

    # ---------------------------------------
    # Count chunks
    # ---------------------------------------

    chunk_count = 0

    chroma_folder = "chroma_db"

    if os.path.exists(chroma_folder):

        # We don't directly depend on
        # ChromaDB internals here.
        # Chunk count will be shown as
        # available from indexing metadata
        # if you later add it.

        pass

    return {
        "papers": paper_count,
        "chunks": chunk_count,
        "papers_list": papers
    }