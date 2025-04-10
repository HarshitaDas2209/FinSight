from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load data
df = pd.read_csv("/home/zeal/programming/genz_ai/retail/retail.csv")

# Embeddings model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Chroma DB setup
db_location = "./chroma_langchain_db"
add_docs = not os.path.exists(db_location)

if add_docs : 
    docs = []
    ids = []

    for i, row in df.iterrows():
        # Combine the relevant columns into one text chunk
        metric = row.get("Metric", "")
        desc = row.get("Description", "")
        factor = row.get("External Factor", "")
        impact = row.get("Impact on Business", "")
        
        # Compose the full text
        content = f"Metric: {metric}. Description: {desc}. External Factor: {factor}. Impact: {impact}"
        
        doc = Document(
            page_content=content,
            metadata={"value": row.get("Value", "")},
            id=str(i)
        )
        docs.append(doc)
        ids.append(str(i))

vector_store = Chroma(
    collection_name="retail_data",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_docs:
    vector_store.add_documents(documents=docs, ids=ids)

# Retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 10},
    search_type="similarity",
    search_score_type="cosine",
    search_distance_metric="cosine"
)
