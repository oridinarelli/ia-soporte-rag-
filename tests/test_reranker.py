from langchain_core.documents import Document

from ranking.reranker import rerankear_documentos


def test_reranker_prioriza_documento_relevante():
    pregunta = "error 500 facturación"

    documentos = [
        Document(page_content="Manual para configurar VPN empresarial."),
        Document(page_content="Solución para error 500 en facturación."),
        Document(page_content="Guía de recuperación de contraseña.")
    ]

    resultado = rerankear_documentos(
        pregunta=pregunta,
        documentos=documentos,
        top_k=1
    )

    assert len(resultado) == 1
    assert "error 500" in resultado[0].page_content.lower()