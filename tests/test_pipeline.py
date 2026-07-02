from orquestacion.langchain_pipeline import calcular_confianza


def test_calcular_confianza_sin_documentos():
    resultado = calcular_confianza(
        pregunta="error 500 facturación",
        documentos=[]
    )

    assert resultado == 0.0