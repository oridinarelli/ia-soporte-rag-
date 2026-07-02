from fastapi import FastAPI
from pydantic import BaseModel

from agente.graph import construir_grafo

app = FastAPI(
    title="IA Soporte RAG",
    version="1.0.0"
)


class PreguntaRequest(BaseModel):
    pregunta: str


@app.get("/")
def home():
    return {
        "mensaje": "API IA Soporte RAG funcionando"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/preguntar")
def preguntar(request: PreguntaRequest):

    agente = construir_grafo()

    estado_inicial = {
        "pregunta": request.pregunta,
        "contexto": "",
        "respuesta": "",
        "iteraciones": 0,
        "confianza": 0.0,
        "historial": []
    }

    resultado = agente.invoke(estado_inicial)

    return {
        "respuesta": resultado["respuesta"],
        "confianza": resultado["confianza"],
        "iteraciones": resultado["iteraciones"]
    }