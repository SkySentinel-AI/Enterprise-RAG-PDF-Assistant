from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embeddings):
    vector_db = FAISS.from_documents(chunks, embeddings)

    # Save the vector database
    vector_db.save_local("vector_db")

    return vector_db


def load_vector_store(embeddings):
    return FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )