# IA Soporte RAG

Proyecto final del curso **IA Engineering**.

## Descripción

Sistema de soporte técnico empresarial basado en **RAG**, con recuperación semántica, re-ranking, orquestación con LangChain, agente con LangGraph, API FastAPI, adaptador MCP seguro, observabilidad, pruebas automatizadas y CI/CD.

---

## Arquitectura

```text
Usuario
  ↓
FastAPI
  ↓
LangGraph
  ↓
LangChain Pipeline
  ↓
Retriever ChromaDB
  ↓
Re-ranking CrossEncoder
  ↓
PromptTemplate
  ↓
Gemini
  ↓
Respuesta final
```

---

## Componentes

- `retrieval/`: construcción y consulta de base vectorial ChromaDB con embeddings de Gemini.
- `ranking/`: re-ranking con modelo CrossEncoder.
- `orquestacion/`: pipeline LangChain, prompt, Gemini y cálculo dinámico de confianza.
- `agente/`: flujo LangGraph con estados, iteraciones y memoria conversacional.
- `adaptadores_mcp/`: adaptador seguro para API externa con validación UUID, Bearer Token y sanitización.
- `observabilidad/`: trazabilidad con LangSmith y logging estructurado compatible con Arize Phoenix.
- `api/`: API REST con FastAPI.
- `despliegue/`: Docker, Kubernetes y función serverless.
- `tests/`: pruebas con pytest.
- `.github/workflows/`: pipeline CI/CD.

---

## API

Ejecutar:

```bash
uvicorn api.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Endpoints:

```text
GET /health
POST /preguntar
```

Ejemplo:

```json
{
  "pregunta": "¿Cómo soluciono el error 500 en facturación?"
}
```

---

## Instalación

```bash
pip install -r requirements.txt
```

Crear `.env`:

```env
GOOGLE_API_KEY=tu_api_key
LANGCHAIN_API_KEY=opcional
LANGCHAIN_PROJECT=ia-soporte-rag
```

---

## Ejecución

Construir base vectorial:

```bash
python -m retrieval.build_vector_db
```

Ejecutar pipeline:

```bash
python -m orquestacion.langchain_pipeline
```

Ejecutar agente:

```bash
python -m agente.graph
```

Ejecutar API:

```bash
uvicorn api.main:app --reload
```

---

## Tests

```bash
pytest
```

---

## CI/CD

El proyecto incluye GitHub Actions para ejecutar pruebas automáticamente en cada push o pull request.

Archivo:

```text
.github/workflows/ci.yml
```

---

## Despliegue

El contenedor usa FastAPI como punto de entrada:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

Kubernetes incluye:

- `livenessProbe`
- `readinessProbe`
- variables sensibles mediante Secret
- puerto 8000

Archivos:

```text
Dockerfile
despliegue/deployment.yaml
despliegue/service.yaml
despliegue/lambda_handler.py
```

---

## Observabilidad

Se registran métricas mediante logging estructurado:

- latencia
- confianza dinámica
- iteraciones
- costo estimado

LangSmith queda preparado para trazabilidad de cadenas y prompts.  
Arize Phoenix queda representado mediante logs estructurados compatibles con métricas de inferencia.

---

## Seguridad

El adaptador MCP implementa:

- validación de UUID
- Bearer Token
- sanitización de campos
- manejo de errores
- principio de mínimo privilegio
- uso esperado de HTTPS/TLS

---

## Cambios realizados tras la revisión

- Se reemplazó el punto de entrada por una API FastAPI.
- Se agregaron `livenessProbe` y `readinessProbe` en Kubernetes.
- Se eliminó la confianza hardcodeada y ahora se calcula dinámicamente.
- Se reemplazó el re-ranking simulado por un modelo CrossEncoder.
- Se integró `MemoriaConversacional` dentro del flujo de LangGraph.
- Se reemplazaron `print()` de métricas por logging estructurado.
- Se agregaron pruebas con `pytest`.
- Se configuró CI/CD con GitHub Actions.
- Se completó `docs/arquitectura.md`.

---

## Checklist

- [x] RAG con ChromaDB
- [x] Embeddings Gemini
- [x] Re-ranking CrossEncoder
- [x] LangChain
- [x] LangGraph
- [x] Memoria conversacional
- [x] Adaptador MCP seguro
- [x] FastAPI
- [x] Healthchecks Kubernetes
- [x] Observabilidad
- [x] Tests
- [x] CI/CD
- [x] Documentación técnica

---

## Nota sobre Gemini

El proyecto utiliza Google Gemini. Para ejecutarlo es necesario configurar una API Key válida. Las cuentas gratuitas pueden tener límites de cuota diarios.

---

## Autor

Proyecto desarrollado como trabajo final del curso **IA Engineering**.