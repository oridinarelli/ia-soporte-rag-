# Arquitectura técnica - IA Soporte RAG

## 1. Objetivo del sistema

Este proyecto implementa un asistente técnico empresarial basado en RAG, capaz de responder consultas utilizando documentación interna como fuente de contexto.

El objetivo es evitar respuestas inventadas, mejorar la precisión y organizar el sistema en componentes mantenibles y escalables.

---

## 2. Arquitectura general

```text
Usuario
  ↓
API FastAPI
  ↓
Agente LangGraph
  ↓
Pipeline LangChain
  ↓
Retriever ChromaDB
  ↓
Re-ranking
  ↓
PromptTemplate
  ↓
Gemini
  ↓
Respuesta final