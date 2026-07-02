from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from retrieval.retriever import recuperar_documentos
from ranking.reranker import rerankear_documentos


load_dotenv()


prompt_template = PromptTemplate.from_template("""
Eres un asistente técnico empresarial.

Tu tarea es responder preguntas usando únicamente el contexto proporcionado.

Reglas:
- No inventes información.
- Si el contexto no alcanza para responder, indica: "No tengo contexto suficiente para responder."
- Responde de forma clara, breve y útil.
- No menciones información que no esté en el contexto.

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta:
""")


def formatear_contexto(documentos):
    return "\n".join(doc.page_content for doc in documentos)


def obtener_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )


def ejecutar_pipeline(pregunta):
    documentos = recuperar_documentos(pregunta, k=5)

    documentos_ordenados = rerankear_documentos(
        pregunta=pregunta,
        documentos=documentos,
        top_k=3
    )

    contexto = formatear_contexto(documentos_ordenados)

    if not contexto.strip():
        return {
            "respuesta": "ERROR: No se encontró contexto relevante.",
            "contexto": "",
            "documentos": [],
            "confianza": 0.0
        }

    prompt = prompt_template.format(
        contexto=contexto,
        pregunta=pregunta
    )

    llm = obtener_llm()
    respuesta = llm.invoke(prompt)

    return {
        "respuesta": respuesta.content,
        "contexto": contexto,
        "documentos": documentos_ordenados,
        "confianza": 0.85
    }


if __name__ == "__main__":
    pregunta = "¿Cómo soluciono el error 500 en facturación?"

    resultado = ejecutar_pipeline(pregunta)

    print("\nRespuesta:")
    print(resultado["respuesta"])

    print("\nContexto utilizado:")
    print(resultado["contexto"])

    print("\nConfianza estimada:")
    print(resultado["confianza"])