from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_rag_index(documents):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(documents, embeddings)
    print(f"Created RAG index for {len(documents)} documents.")
    return vector_store

if __name__ == "__main__":
    create_rag_index(["AI is transforming software engineering.", "Agentic systems use tools."])