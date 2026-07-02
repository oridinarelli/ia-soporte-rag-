from adaptadores_mcp.cliente_api import validar_uuid, sanitizar_respuesta


def test_validar_uuid_correcto():
    cliente_id = "550e8400-e29b-41d4-a716-446655440000"

    assert validar_uuid(cliente_id) is True


def test_validar_uuid_incorrecto():
    cliente_id = "12345"

    assert validar_uuid(cliente_id) is False


def test_sanitizar_respuesta():
    data = {
        "nombre": "Ana Pérez",
        "email": "ana@empresa.com",
        "estado": "activo",
        "dni": "12345678",
        "saldo": 50000
    }

    resultado = sanitizar_respuesta(data)

    assert resultado == {
        "nombre": "Ana Pérez",
        "email": "ana@empresa.com",
        "estado": "activo"
    }