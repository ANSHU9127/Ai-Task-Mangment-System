from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.IndexFlatL2(384)
documents = []

def add_doc(text):
    chunks = [text[i:i+200] for i in range(0, len(text), 200)]

    for chunk in chunks:
        emb = model.encode([chunk])
        index.add(np.array(emb))
        documents.append(chunk)

def search_doc(query):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=3)
    return [documents[i] for i in I[0]]