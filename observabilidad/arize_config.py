def registrar_metrica(nombre, valor):
    """
    Simulación de envío de métricas a Arize Phoenix.
    En producción se integraría el SDK oficial.
    """
    print({
        "herramienta": "Arize Phoenix",
        "metrica": nombre,
        "valor": valor
    })


def registrar_inferencia(latencia_ms, confianza, iteraciones, costo_estimado):
    registrar_metrica("latencia_ms", latencia_ms)
    registrar_metrica("confianza", confianza)
    registrar_metrica("iteraciones", iteraciones)
    registrar_metrica("costo_estimado_usd", costo_estimado)