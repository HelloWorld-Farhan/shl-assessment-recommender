import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

class CatalogRetriever:
    def __init__(self, catalog_path="shl_product_catalog.json", model_name="all-MiniLM-L6-v2"):
        self.catalog_path = catalog_path
        self.model = SentenceTransformer(model_name)
        self.items = []
        self.index = None
        self._load_and_index()

    def _load_and_index(self):
        if not os.path.exists(self.catalog_path):
            print(f"Catalog file {self.catalog_path} not found.")
            return

        with open(self.catalog_path, 'r', encoding='utf-8') as f:
            self.items = json.load(f, strict=False)

        # Create search texts by combining relevant fields
        search_texts = []
        for item in self.items:
            # Combine name, description, levels, languages, keys
            name = item.get("name", "")
            desc = item.get("description", "")
            levels = item.get("job_levels_raw", "")
            langs = item.get("languages_raw", "")
            keys = ", ".join(item.get("keys", []))
            
            text = f"Name: {name}. Description: {desc}. Job Levels: {levels}. Languages: {langs}. Category/Keys: {keys}"
            search_texts.append(text)

        # Embed all texts
        print("Generating embeddings for catalog...")
        embeddings = self.model.encode(search_texts, convert_to_numpy=True)
        
        # Create FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
        print("Indexing complete.")

    def search(self, query: str, top_k: int = 15):
        if not self.index:
            return []
        
        query_vector = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vector, top_k)
        
        results = []
        for idx in indices[0]:
            if idx < len(self.items):
                results.append(self.items[idx])
        return results

# Singleton instance
retriever = None
def get_retriever():
    global retriever
    if retriever is None:
        retriever = CatalogRetriever()
    return retriever
