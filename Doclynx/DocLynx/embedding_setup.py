import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

df = pd.read_csv("standards_dataset.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = df["summary"].tolist()
vectors = model.encode(texts)

# Create FAISS index
dimension = vectors[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors).astype("float32"))

# Save index
os.makedirs("faiss_index", exist_ok=True)
faiss.write_index(index, "faiss_index/index.faiss")
print("✅ FAISS index created and saved.")
