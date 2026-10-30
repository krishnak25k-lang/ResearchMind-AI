from src.embedding import create_embeddings
from src.vector_store import search_chunks
from src.llm import generate_answer


# --------------------------------
# 1. User question
# --------------------------------

question = input("\nAsk a question about the research paper: ")


# --------------------------------
# 2. Convert question to embedding
# --------------------------------

query_embedding = create_embeddings(
    [question]
)


# --------------------------------
# 3. Search ChromaDB
# --------------------------------

results = search_chunks(
    query_embedding,
    n_results=3
)


# --------------------------------
# 4. Get retrieved documents
# --------------------------------

documents = results["documents"][0]


# --------------------------------
# 5. Combine retrieved chunks
# --------------------------------

context = "\n\n".join(documents)


# --------------------------------
# 6. Send context + question to AI
# --------------------------------

answer = generate_answer(
    question,
    context
)


# --------------------------------
# 7. Display result
# --------------------------------

print("\n")
print("=" * 70)
print("RESEARCHMIND AI")
print("=" * 70)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)

print("\n")
print("=" * 70)
print("RETRIEVED RESEARCH")
print("=" * 70)

for i, document in enumerate(documents, start=1):

    print(f"\n--- Source Chunk {i} ---")
    print(document)