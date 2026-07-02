from typing import TypedDict, List


class AgentState(TypedDict):
    pregunta: str
    contexto: str
    respuesta: str
    iteraciones: int
    confianza: float
    historial: List[str]