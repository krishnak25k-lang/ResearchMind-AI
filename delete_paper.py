import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_collection(
    name="research_papers"
)

paper_name = "git statusMarlion Technologies 7.pdf"

collection.delete(
    where={
        "paper": paper_name
    }
)

print(f"{paper_name} deleted from ChromaDB")