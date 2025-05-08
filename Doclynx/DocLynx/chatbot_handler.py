import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import subprocess
import json

# Load the FAISS index and data
index = faiss.read_index("faiss_index/index.faiss")
df = pd.read_csv("standards_dataset.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_response(query):
    # Convert query to embedding
    query_vector = model.encode([query])
    
    # Search for relevant documents
    top_k = 3
    _, indices = index.search(np.array(query_vector).astype("float32"), top_k)
    relevant = df.iloc[indices[0]]
    
    # Prepare context for LLM
    context = "\n".join(
        f"{row['standard']} - Clause {row['clause']}: {row['summary']}" 
        for _, row in relevant.iterrows()
    )

    prompt = f"Use the following standard references to answer the query.\n\n{context}\n\nQuery: {query}\nAnswer:"

    # Send prompt to Ollama
    result = subprocess.run(
        ["ollama", "run", "phi", prompt],
        stdout=subprocess.PIPE,
        text=True
    )

    return result.stdout.strip()