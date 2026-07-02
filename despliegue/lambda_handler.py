from agente.graph import construir_grafo


def lambda_handler(event, context):
    pregunta = event.get(
        "pregunta",
        "¿Cómo soluciono el error 500 en facturación?"
    )

    agente = construir_grafo()

    estado_inicial = {
        "pregunta": pregunta,
        "contexto": "",
        "respuesta": "",
        "iteraciones": 0,
        "confianza": 0.0,
        "historial": []
    }

    resultado = agente.invoke(estado_inicial)

    return {
        "statusCode": 200,
        "body": {
            "respuesta": resultado["respuesta"],
            "confianza": resultado["confianza"],
            "iteraciones": resultado["iteraciones"]
        }
    }