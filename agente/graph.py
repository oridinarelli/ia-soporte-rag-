import time

from langgraph.graph import StateGraph, END

from agente.state import AgentState
from agente.memory import MemoriaConversacional
from orquestacion.langchain_pipeline import ejecutar_pipeline
from observabilidad.langsmith_config import configurar_langsmith
from observabilidad.arize_config import registrar_inferencia


MAX_ITERACIONES = 3
UMBRAL_CONFIANZA = 0.75

memoria = MemoriaConversacional()


def ejecutar_rag(state: AgentState):
    pregunta = state["pregunta"]

    historial_previo = memoria.obtener_historial()

    pregunta_con_memoria = f"""
Historial conversacional:
{historial_previo}

Pregunta actual:
{pregunta}
"""

    resultado_pipeline = ejecutar_pipeline(pregunta_con_memoria)

    memoria.agregar(f"Pregunta: {pregunta}")
    memoria.agregar(f"Respuesta: {resultado_pipeline['respuesta']}")

    historial_actualizado = memoria.obtener_historial()

    return {
        **state,
        "contexto": resultado_pipeline["contexto"],
        "respuesta": resultado_pipeline["respuesta"],
        "confianza": resultado_pipeline["confianza"],
        "iteraciones": state["iteraciones"] + 1,
        "historial": historial_actualizado
    }


def evaluar_estado(state: AgentState):
    if state["confianza"] >= UMBRAL_CONFIANZA:
        return "finalizar"

    if state["iteraciones"] >= MAX_ITERACIONES:
        return "finalizar"

    return "reintentar"


def construir_grafo():
    graph = StateGraph(AgentState)

    graph.add_node("ejecutar_rag", ejecutar_rag)

    graph.set_entry_point("ejecutar_rag")

    graph.add_conditional_edges(
        "ejecutar_rag",
        evaluar_estado,
        {
            "reintentar": "ejecutar_rag",
            "finalizar": END
        }
    )

    return graph.compile()


if __name__ == "__main__":
    configurar_langsmith()

    inicio = time.time()

    agente = construir_grafo()

    estado_inicial = {
        "pregunta": "¿Cómo soluciono el error 500 en facturación?",
        "contexto": "",
        "respuesta": "",
        "iteraciones": 0,
        "confianza": 0.0,
        "historial": []
    }

    resultado = agente.invoke(estado_inicial)

    fin = time.time()
    latencia_ms = round((fin - inicio) * 1000, 2)

    costo_estimado = 0.01

    registrar_inferencia(
        latencia_ms=latencia_ms,
        confianza=resultado["confianza"],
        iteraciones=resultado["iteraciones"],
        costo_estimado=costo_estimado
    )

    print("\nRespuesta final:")
    print(resultado["respuesta"])

    print("\nIteraciones:")
    print(resultado["iteraciones"])

    print("\nConfianza:")
    print(resultado["confianza"])

    print("\nHistorial:")
    for item in resultado["historial"]:
        print("-", item)

    print("\nLatencia ms:")
    print(latencia_ms)