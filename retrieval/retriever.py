from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

DB_PATH = "retrieval/chroma_db"


def obtener_retriever(k=4):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )


def recuperar_documentos(pregunta, k=4):
    retriever = obtener_retriever(k)
    return retriever.invoke(pregunta)