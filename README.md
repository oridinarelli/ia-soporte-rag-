# IA Soporte RAG

Proyecto final de IA Engineering.

## Descripción

Este proyecto implementa un sistema de soporte técnico basado en Retrieval-Augmented Generation (RAG) utilizando LangChain y LangGraph.

El sistema recupera información desde una base vectorial (ChromaDB), la reordena mediante un proceso de ranking y utiliza Gemini para generar respuestas fundamentadas en el contexto recuperado.

---

# Arquitectura

El sistema está compuesto por los siguientes módulos:

retrieval/
- Recuperación de documentos mediante ChromaDB y embeddings de Gemini.

ranking/
- Re-ranking de documentos recuperados para priorizar los más relevantes.

orquestacion/
- Pipeline construido con LangChain.
- Construcción del PromptTemplate.
- Consulta al modelo Gemini.

agente/
- Agente desarrollado con LangGraph.
- Manejo de estados.
- Razonamiento iterativo.
- Memoria conversacional.

adaptadores_mcp/
- Adaptador MCP para conexión segura con APIs externas.

observabilidad/
- Configuración de LangSmith.
- Simulación de envío de métricas a Arize Phoenix.

despliegue/
- Docker.
- Kubernetes.
- Función Serverless.

---

# Flujo del sistema

Usuario

↓

Retriever (ChromaDB)

↓

Re-ranking

↓

PromptTemplate

↓

Gemini

↓

LangGraph

↓

Respuesta

---

# Tecnologías utilizadas

- Python
- LangChain
- LangGraph
- Google Gemini
- ChromaDB
- MCP
- Docker
- Kubernetes
- LangSmith
- Arize Phoenix

---

# Variables de entorno

Crear un archivo `.env` con:

GOOGLE_API_KEY=xxxxxxxxxxxxxxxx

Opcionalmente:

LANGCHAIN_API_KEY=xxxxxxxx
LANGCHAIN_PROJECT=ia-soporte-rag

---

# Ejecución

Construcción de la base vectorial

```bash
python -m retrieval.build_vector_db
```

Ejecución del pipeline

```bash
python -m orquestacion.langchain_pipeline
```

Ejecución del agente

```bash
python -m agente.graph
```

---

# Despliegue

El proyecto incluye:

- Dockerfile
- deployment.yaml
- service.yaml
- lambda_handler.py

Estos archivos permiten desplegar la aplicación en Docker, Kubernetes o una plataforma Serverless.

---

# Observabilidad

El proyecto incorpora:

- LangSmith para trazabilidad.
- Arize Phoenix para monitoreo de métricas.
- Registro de latencia.
- Registro de confianza.
- Registro de iteraciones.
- Estimación de costo por inferencia.

---

# Autor

Proyecto desarrollado como trabajo final del curso IA Engineering.

---

# Checklist de evaluación

- [x] Estructura modular del repositorio
- [x] Retrieval con base vectorial ChromaDB
- [x] Re-ranking de documentos
- [x] Orquestación con LangChain
- [x] Agente cíclico con LangGraph
- [x] Adaptador MCP seguro
- [x] Observabilidad con LangSmith y Arize Phoenix
- [x] Scripts de despliegue Docker, Kubernetes y Serverless
- [x] Documentación de arquitectura y ejecución