from sentence_transformers import CrossEncoder

# El modelo se carga solo cuando realmente se necesita
modelo = None


def obtener_modelo():
    global modelo

    if modelo is None:
        modelo = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    return modelo


def rerankear_documentos(pregunta, documentos, top_k=3):
    """
    Re-ranking utilizando un modelo CrossEncoder.
    """

    if not documentos:
        return []

    pares = [
        (pregunta, doc.page_content)
        for doc in documentos
    ]

    modelo_reranker = obtener_modelo()

    scores = modelo_reranker.predict(pares)

    documentos_ordenados = sorted(
        zip(documentos, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, _ in documentos_ordenados[:top_k]
    ]