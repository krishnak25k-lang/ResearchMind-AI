from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = [
    "The researchers developed a deep learning model for image classification.",
    "A neural network was proposed to classify images.",
    "The weather is very hot today."
]


embeddings = model.encode(sentences)


similarity = cosine_similarity(embeddings)


print("Similarity Matrix:")
print(similarity)