from src.paper_indexer import index_uploaded_paper


pdf_path = "data/papers/paper1.pdf"

result = index_uploaded_paper(
    pdf_path,
    "paper1.pdf"
)


print("\n================================")
print("PAPER INDEXING COMPLETE")
print("================================")

print(
    f"Paper: {result['paper']}"
)

print(
    f"Pages: {result['pages']}"
)

print(
    f"Chunks: {result['chunks']}"
)