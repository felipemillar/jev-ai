# Jev AI — Plataforma de Inferencia Semántica y Base de Conocimiento Canónica

Repositorio central del programa de adopción, investigación técnica e integración de **Jev** (el modelo insignia de Sistema Uno desarrollado por **TypeSafe AI**), optimizado para emitir decisiones tipadas y probabilidades calibradas directamente consumibles por software en tiempo real.

---

## 🧭 Estructura del Repositorio

El repositorio está organizado en dos componentes complementarios:

```
Jev AI/
├── README.md                      # Este documento maestro institucional
├── BITACORA.md                    # Registro cronológico de cambios y sesiones de desarrollo
├── .gitignore                     # Configuración de exclusión para Git (Python, venv, macOS)
├── Jev AI.code-workspace          # Configuración de espacio de trabajo para VS Code / Antigravity IDE
├── .agents/                       # Customizaciones del agente y reglas locales
│   ├── AGENTS.md                  # Reglas de gobernanza, seguridad y directrices del agente
│   └── skills/typesafe-ai/        # Skill oficial de TypeSafe AI para agentes autónomos
│
└── docs/
    ├── documentacion-oficial/     # 📚 Documentación Técnica Oficial (114 archivos descargados)
    │   ├── README.md              # Índice general de la documentación
    │   ├── llms.txt               # Índice optimizado para LLMs
    │   ├── llms-full.txt          # Toda la documentación compilada en un archivo (~895 KB)
    │   ├── openapi.json           # Especificación formal OpenAPI 3.1.0 de la API TypeSafe
    │   ├── concepts/              # Fundamentos de System One, Estado y Confianza
    │   ├── primitives/            # Choice, Score, Noul y Estructura Avanzada
    │   ├── patterns/              # Fan-out, Confidence Routing, Composite Scoring, Intent Routing
    │   ├── cookbooks/             # 18 Cookbooks con código de producción (Reranking, Guardrails, etc.)
    │   ├── sdk/                   # Referencia de SDKs oficiales para Python y JavaScript/TypeScript
    │   └── model-jaggedness/      # Límites documentados y bordes irregulares de jev-1.13
    │
    └── programa-jev/              # 🔬 Programa de Investigación Canónica (384 preguntas)
        ├── README.md              # Introducción al programa y protocolo de colaboración
        ├── cuestionario-maestro-jev-antigravity.md # 384 preguntas maestras sobre 18 pilares
        ├── registro-cuestionario-jev.csv # Matriz de seguimiento canónico
        ├── plan-investigacion-jev-spark.md # Plan de investigación de 18 pilares
        └── base-conocimiento/     # Base de conocimiento auditada con rigor formal
            ├── sintesis/          # Guía Maestra de Uso y síntesis de pilares P01–P18 y Pilar X
            ├── respuestas/        # 384 expedientes de respuesta estandarizados
            ├── pilotos.md         # Cartera de pilotos falsables (QRT, Wheelwork, SaaS)
            ├── glosario.md        # Glosario unívoco de terminología técnica
            ├── afirmaciones.md    # Registro de afirmaciones empíricas y verificables
            ├── fuentes.md         # Catálogo de fuentes bibliográficas y contratos de API
            └── remediacion-integral/verificacion-local/
                └── test_integrity.py # Suite de validación automatizada (15/15 criterios)
```

---

## ⚡ ¿Qué es Jev y System One?

A diferencia de los LLMs tradicionales (*Sistema Dos*) que generan texto libre con latencias altas (1–3 s) y riesgos de alucinación sintáctica, **Jev** es un modelo **Sistema Uno**:
- **Inferencia en ~100–150 ms**: Diseñado para rutas críticas de backend y UI reactiva.
- **Tipado estricto por construcción**: Devuelve objetos JSON válidos con esquemas cerrados (`Choice`, `Score`, `Noul`).
- **Probabilidades Calibradas**: Entrena sus salidas con RLCD (*Reinforcement Learning from Classifier Feedback*), garantizando que las probabilidades reportadas reflejen la frecuencia empírica de acierto.
- **Soberanía del Código**: El código en CPU (Python/TypeScript) gobierna el flujo de control, bases de datos y efectos secundarios; Jev actúa como un servicio de juicio semántico puro.

---

## 🚀 Inicio Rápido y Entorno Local

### 1. Requisitos Previos
- Python $\ge$ 3.10
- Clave de API de TypeSafe (obtén tu acceso en [console.typesafe.ai](https://console.typesafe.ai))

### 2. Instalación de Dependencias
```bash
# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias del SDK oficial y herramientas de verificación
pip install typesafe-sdk pyyaml requests
```

### 3. Configuración de Credenciales
```bash
export TYPESAFE_API_KEY="tu-api-key-de-consola"
```

### 4. Ejecución del Primer Ejemplo
```python
import os
from typesafe import TypeSafeClient

client = TypeSafeClient(api_key=os.environ["TYPESAFE_API_KEY"])

response = client.systemone(
    state="El cliente solicita soporte urgente por fallo en la sincronización de su cuenta.",
    questions={
        "categoria": {
            "type": "choice",
            "instruction": "Clasifica la consulta.",
            "options": {
                "tecnico": "Problemas de plataforma o errores de sincronización.",
                "comercial": "Dudas de tarifas o compras.",
                "otro": "Cualquier otra consulta.",
            },
        }
    },
)

print(response.results["categoria"].choice)  # 'tecnico'
print(response.results["categoria"].confidence)  # ej. 0.94
```

---

## 🧪 Verificación de Integridad Automatizada

El repositorio cuenta con un arnés de pruebas estricto e independiente que valida la integridad estructural, sintáctica y matemática de toda la base de conocimiento:

```bash
python docs/programa-jev/base-conocimiento/remediacion-integral/verificacion-local/test_integrity.py
```

### Cobertura de la Suite (`test_integrity.py`):
1. Verificación de **384/384 preguntas canónicas** mapeadas unívocamente contra el cuestionario maestro.
2. Parseo sintáctico de metadatos YAML (`yaml.safe_load`).
3. Cumplimiento de las 10 secciones canónicas obligatorias por respuesta.
4. Coherencia criptográfica de hashes SHA-256 frente a `seguimiento.csv`.
5. Inspección AST de todos los bloques Python y validación de constructores `typesafe-sdk`.
6. Instanciación local sin red (`0 network calls`) de objetos SDK extraídos.
7. Verificación de fuentes bibliográficas cruzadas frente a `fuentes.md`.
8. Detección y rechazo de duplicación modular de párrafos sustantivos.
9. Evaluación de rúbricas multidimensionales sobre 25 puntos.
10. Ejecución de *fixtures* negativos para verificar la capacidad de detección del validador.

---

## 🛡️ Principios de Gobernanza y Seguridad

1. **Aislamiento de Entornos (Air-Gap Lógico)**: En aplicaciones financieras o cuantitativas (QRT), queda prohibida la conexión directa de inferencias a pasarelas de ejecución de órdenes (MT5/FIX) sin supervisión determinista o humana.
2. **Garantías de Privacidad y Ética**: En flujos de evaluación de personas (Wheelwork), los datos sensibles (PII) deben ser anonimizados en la CPU local antes de invocar la API. Queda vetado el descarte automático desatendido.
3. **Manejo Seguro de Excepciones (*Error Masking*)**: En bloques `except`, registrar únicamente `type(err).__name__` y el sufijo `(detalles omitidos por seguridad)` para evitar la exposición de tokens o datos sensibles en logs.

---

## 👥 Contribución y Trabajo en Equipo

1. Toda modificación a la base de conocimiento debe pasar exitosamente `test_integrity.py` antes de fusionarse.
2. Cada sesión de trabajo debe documentarse cronológicamente en [BITACORA.md](BITACORA.md).
3. Mantener el desacoplamiento mediante adaptadores (*Decision Gateway*) para asegurar portabilidad entre Jev y modelos locales o deterministas.
