# Documentación Oficial de TypeSafe AI & Modelo Jev

Repositorio local completo y fuente autoritativa de la documentación oficial de **TypeSafe AI** y su modelo insignia **Jev** (primer modelo de la categoría *System One*), descargado directamente desde [docs.typesafe.ai](https://docs.typesafe.ai) y [api.typesafe.ai](https://api.typesafe.ai).

---

## 📌 Visión General del Sistema: ¿Qué es Jev y System One?

A diferencia de los modelos de lenguaje tradicionales (LLMs / *System Two*) diseñados para redactar texto libre para humanos, **Jev** es un modelo **System One**:
- **Diseñado para software**: Recibe estado estructurado/lenguaje natural y preguntas tipadas; devuelve respuestas estructuradas y probabilidades calibradas listas para ser consumidas directamente por código.
- **Sin alucinación ni relleno conversacional**: No genera párrafos explicativos ni divagaciones sintácticas. El código mantiene el control del flujo y la lógica determinista; el modelo provee juicio semántico de alta velocidad.
- **Probabilidades calibradas y Confianza (*Confidence*)**: Cada respuesta entrega una distribución de probabilidad real y una métrica ortogonal de certeza/confianza para bifurcación segura en código.

---

## 🗂️ Estructura del Repositorio de Documentación Local

```
docs/documentacion-oficial/
├── README.md                      # Este índice maestro y guía consolidada
├── llms.txt                       # Índice canónico optimizado para agentes y LLMs
├── llms-full.txt                  # Documentación oficial completa en un solo archivo (895 KB)
├── openapi.json                   # Especificación técnica oficial OpenAPI 3.1.0 de la API
│
├── introduction.md                # Introducción oficial a TypeSafe AI y Jev
├── introduction/
│   ├── quickstart.md              # Guía de inicio rápido y primer endpoint
│   └── machine-learning-primer.md # Fundamentos de calibración probabilística vs generación
│
├── concepts/                      # Conceptos Arquitectónicos Centrales
│   ├── system-one.md              # Filosofía y arquitectura de System One
│   ├── state.md                   # Cómo diseñar y optimizar el contexto/estado
│   ├── how-to-build-with-system-one.md # Principios de diseño para código + TypeSafe
│   └── use-case-map.md            # Mapeo de casos de uso por industria
├── confidence.md                  # El eje de certeza: cómo interpretar y actuar por umbrales
│
├── primitives.md                  # Introducción a las preguntas tipadas
├── primitives/                    # Las 3 Primitivas Fundamentales
│   ├── choice.md                  # Elección entre N opciones (distribución de probabilidades)
│   ├── score.md                   # Escala ordinal descriptiva (puntuación calibrada)
│   ├── noul.md                    # Juicio booleano Sí/No con probabilidad P(Yes)
│   └── advanced.md                # Estructuras JSON jerárquicas en criterios y opciones
│
├── patterns.md                    # Introducción a patrones de diseño
├── patterns/                      # Patrones de Ingeniería
│   ├── fan-out.md                 # Speculative Fan-out: múltiples preguntas en un solo request
│   ├── confidence-routing.md      # Enrutamiento basado en confianza (auto vs humano vs fallback)
│   ├── composite-scoring.md       # Descomposición de juicios complejos en scores atómicos
│   └── intent-routing.md          # Clasificación y enrutamiento inteligente de intents
│
├── cookbooks/                     # 18 Cookbooks Oficiales con Código de Producción
│   ├── autoformat.md              # Reconstrucción de Markdown y estructura desde texto plano
│   ├── autoresearch_feature_discovery.md # Loop de feature engineering asistido para ML
│   ├── citation_check.md          # Verificación de citas contra fuentes originales
│   ├── classification_using_confidence.md # Clasificación taxonómica jerárquica con confianza
│   ├── classifying_rag_passages.md # Filtrado y guardrails de pasajes RAG antes del LLM
│   ├── consistency_choice_cookbook.md # Auto-moderación con fallback para elecciones dudosas
│   ├── consistency_noul_cookbook.md   # Auto-moderación y enrutamiento en juicios booleanos
│   ├── date_extraction_cookbook.md    # Extracción y resolución de fechas relativas/absolutas
│   ├── entity_alignment.md        # Alineación de entidades entre catálogos dispares
│   ├── function_calling.md        # Mapeo de solicitudes libres a firmas de funciones tipadas
│   ├── hierarchical_classification.md # Beam search paralelo sobre taxonomías profundas
│   ├── llm_guardrails.md          # Filtro bidireccional de inyecciones y toxicidad para LLMs
│   ├── parallel_questions.md      # Batching masivo (12.2x más barato, 10x más rápido)
│   ├── pre_parsed_value_extraction_cookbook.md # Extracción combinando regex + TypeSafe
│   ├── rerank_typesafe.md         # Re-ranking semántico de pasajes sobre BM25
│   ├── sde_cascade.md             # Cascada mini → verify → reasoning para extracción de datos
│   ├── semantic_find.md           # Búsqueda semántica línea por línea en documentos legales
│   └── skill_suggestion.md        # Selección de herramientas/skills dinámicas para agentes
│
├── sdk.md                         # Visión general de los SDKs
├── sdk/python/                    # SDK Oficial de Python (`typesafe`)
│   ├── python.md                  # Instalación y configuración
│   ├── usage.md                   # Guía de uso sincrónico y asincrónico
│   ├── changelog.md               # Registro de versiones del SDK
│   └── api/                       # Referencia completa de clases y métodos Python
│       ├── clients/async.md       # AsyncTypeSafeClient
│       ├── clients/sync.md        # TypeSafeClient
│       ├── types/questions.md     # Modelos de preguntas (Choice, Score, Noul)
│       ├── types/responses.md     # Estructuras de respuesta y metadata de consumo
│       ├── types/common.md        # Tipos comunes
│       ├── retries.md             # Políticas de reintento y backoff exponencial
│       ├── exceptions.md          # Jerarquía de excepciones de la API
│       └── constants.md           # Constantes y variables de entorno
│
├── sdk/javascript/                # SDK Oficial de JavaScript / TypeScript
│   ├── javascript.md              # Instalación y configuración
│   ├── changelog.md               # Historial de cambios
│   └── api/                       # Clases, interfaces, tipos y funciones auxiliares
│
├── models.md                      # Catálogo de modelos disponibles (Jev)
├── model-jaggedness/
│   └── jev-1.13.md                # Bordes irregulares (*jagged edges*) y límites de jev-1.13
├── api.md                         # Referencia de la API HTTP directa (`/v1/systemone`)
├── legal.md                       # Términos, privacidad y cumplimiento legal
├── demos/                         # Demostraciones interactivas
│   ├── demos.md
│   └── smart-home.md              # Asistente domótico controlado por código y TypeSafe
└── skills/typesafe-ai/
    └── SKILL.md                   # Skill oficial para agentes de IA (Claude Code, Codex, Antigravity)
```

---

## ⚡ Las 3 Primitivas Fundamentales

| Primitiva | Pregunta que resuelve | Salida tipada | Caso de uso típico |
|---|---|---|---|
| **Choice** (`primitives/choice.md`) | Selección de 1 opción entre un conjunto finito | `answer: string`, `probabilities: { [key]: number }`, `confidence: number` | Clasificación, enrutamiento de intents, selección de herramientas |
| **Score** (`primitives/score.md`) | Calificación ordinal en escala descriptiva | `score: number`, `probabilities: number[]`, `confidence: number` | Priorización de tickets, severidad, relevancia semántica, calidad |
| **Noul** (`primitives/noul.md`) | Evaluación booleana binaria (Sí / No) | `probability: number` (P(Yes)), `confidence: number` | Guardrails, detección de anomalías, verificación de hechos, filtros |

---

## 🛠️ Contrato de la API HTTP (`/v1/systemone`)

- **Host Base**: `https://api.typesafe.ai`
- **Autenticación**: Cabecera `Authorization: Bearer <TYPESAFE_API_KEY>`
- **Modelo por Defecto**: `jev-1.13`
- **Endpoints Principales**:
  - `POST /v1/systemone`: Ejecución de una o múltiples preguntas sobre un estado dado.
  - `GET /v1/models`: Listado de modelos disponibles y sus metadatos.
- **Especificación OpenAPI**: Consulta el archivo local [openapi.json](openapi.json) para el esquema JSON Schema exhaustivo de requests y responses.

### Ejemplo de Payload Mínimo (`/v1/systemone`):

```json
{
  "model": "jev-1.13",
  "state": "El cliente solicita cancelar su suscripción debido a problemas de facturación reiterados.",
  "questions": {
    "motivo": {
      "type": "choice",
      "instruction": "¿Cuál es el motivo principal de la consulta?",
      "options": {
        "facturacion": "Problemas de cobro, tarjetas o pagos",
        "tecnico": "Fallas en el software o plataforma",
        "precio": "Considera el servicio muy caro",
        "otro": "Cualquier otra razón no contemplada"
      }
    },
    "riesgo_churn": {
      "type": "noul",
      "instruction": "¿El cliente tiene intención inminente de cancelar o abandonar el servicio?"
    },
    "urgencia": {
      "type": "score",
      "instruction": "Nivel de urgencia de atención para el equipo de soporte",
      "levels": [
        "Baja: consulta general o sin impacto operativo",
        "Media: incomodidad pero con workaround",
        "Alta: impacto directo en facturación o servicio",
        "Crítica: cliente bloqueado o en proceso de baja definitiva"
      ]
    }
  }
}
```

---

## 🤖 Skill Oficial Integrada para el Agente

La skill oficial de TypeSafe AI ha sido descargada e instalada en el workspace en:
- [SKILL.md](skills/typesafe-ai/SKILL.md)
- `.agents/skills/typesafe-ai/SKILL.md`

Esta skill proporciona las directrices y contratos para orquestar llamadas a Jev, estructurar estados, diseñar preguntas sin sesgos y aplicar patrones arquitectónicos avanzados en código Python o TypeScript.
