from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Carga las variables del archivo .env
load_dotenv()

DATA_PATH = "data/documentos_soporte.txt"
DB_PATH = "retrieval/chroma_db"


def cargar_documentos():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        texto = file.read()

    chunks = [chunk.strip() for chunk in texto.split("\n\n") if chunk.strip()]

    return [
        Document(
            page_content=chunk,
            metadata={"source": DATA_PATH}
        )
        for chunk in chunks
    ]


def construir_vector_db():
    documentos = cargar_documentos()

    # Embeddings reales de Gemini
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    Chroma.from_documents(
        documents=documentos,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("Base vectorial creada correctamente.")


if __name__ == "__main__":
    construir_vector_db()