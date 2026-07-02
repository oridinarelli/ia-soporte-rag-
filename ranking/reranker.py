def rerankear_documentos(pregunta, documentos, top_k=3):
    """
    Re-ranker simple basado en coincidencia de palabras.
    En producción se reemplazaría por un modelo de re-ranking.
    """

    palabras_pregunta = set(pregunta.lower().split())

    documentos_puntuados = []

    for doc in documentos:
        texto = doc.page_content.lower()
        score = sum(1 for palabra in palabras_pregunta if palabra in texto)

        documentos_puntuados.append(
            {
                "documento": doc,
                "score": score
            }
        )

    documentos_ordenados = sorted(
        documentos_puntuados,
        key=lambda item: item["score"],
        reverse=True
    )

    return [
        item["documento"]
        for item in documentos_ordenados[:top_k]
    ]