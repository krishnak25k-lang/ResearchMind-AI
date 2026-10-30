from src.embedding import create_embeddings
from src.vector_store import search_chunks


question = input(
    "\nAsk a question about the research papers: "
)


query_embedding = create_embeddings(
    [question]
)


results = search_chunks(
    query_embedding,
    n_results=3
)


documents = results["documents"][0]

metadatas = results["metadatas"][0]


print("\n")
print("=" * 70)
print("RESEARCH SOURCES")
print("=" * 70)


for i, (document, metadata) in enumerate(
    zip(documents, metadatas),
    start=1
):

    print(f"\nRESULT {i}")

    print(
        f"📄 Paper: {metadata['paper']}"
    )

    print(
        f"📑 Page: {metadata['page']}"
    )

    print("\nContent:")

    print(document)