from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vector_store
from utils.retriever import get_retriever
from utils.qa_chain import get_llm, get_qa_chain

print("Loading PDF...")

documents = load_pdf("data/EMPLOYEE HANDBOOK.pdf")

print("Splitting PDF...")

chunks = split_documents(documents)

print("Loading Embedding Model...")

embeddings = get_embeddings()

print("Creating Vector Database...")

vector_db = create_vector_store(chunks, embeddings)

print("Creating Retriever...")

retriever = get_retriever(vector_db)

print("Connecting Gemini...")

llm = get_llm()

print("Building QA Chain...")

qa_chain = get_qa_chain(llm, retriever)

print("\n✅ RAG Chatbot Ready!\n")

while True:
    question = input("Ask a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    response = qa_chain.invoke({"query": question})
    print("\nAnswer:\n")
    print(response["result"])
    print("-" * 60)