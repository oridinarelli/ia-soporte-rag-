import json
import logging


logger = logging.getLogger("observabilidad")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(handler)


def registrar_metrica(nombre, valor):
    evento = {
        "backend": "Arize Phoenix compatible",
        "tipo": "metrica",
        "nombre": nombre,
        "valor": valor
    }

    logger.info(json.dumps(evento))


def registrar_inferencia(latencia_ms, confianza, iteraciones, costo_estimado):
    evento = {
        "backend": "Arize Phoenix compatible",
        "tipo": "inferencia",
        "latencia_ms": latencia_ms,
        "confianza": confianza,
        "iteraciones": iteraciones,
        "costo_estimado_usd": costo_estimado
    }

    logger.info(json.dumps(evento))