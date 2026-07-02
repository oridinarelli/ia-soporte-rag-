import os
import uuid
import requests


API_URL = os.getenv("CLIENTES_API_URL", "https://api.empresa.com/clientes")
TOKEN = os.getenv("CLIENTES_API_TOKEN")


def validar_uuid(cliente_id):
    try:
        uuid.UUID(cliente_id)
        return True
    except ValueError:
        return False


def sanitizar_respuesta(data):
    campos_permitidos = ["nombre", "email", "estado"]

    return {
        campo: data.get(campo)
        for campo in campos_permitidos
        if campo in data
    }


def consultar_cliente(cliente_id):
    if not validar_uuid(cliente_id):
        return {
            "error": "cliente_id inválido"
        }

    if not TOKEN:
        return {
            "error": "Token de autenticación no configurado"
        }

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            f"{API_URL}/{cliente_id}",
            headers=headers,
            timeout=5
        )

        if response.status_code != 200:
            return {
                "error": "No fue posible consultar el cliente"
            }

        data = response.json()
        return sanitizar_respuesta(data)

    except requests.exceptions.RequestException:
        return {
            "error": "Error de conexión con la API de clientes"
        }

    except ValueError:
        return {
            "error": "Respuesta inválida de la API"
        }