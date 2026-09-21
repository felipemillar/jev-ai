# Glosario Canónico — Programa Jev

**Versión:** 2.0.0 (Remediación Integral y Normalización Canónica)  
**Fecha de Publicación:** 2026-09-20  
**Responsable:** Antigravity (Autorrevisión técnica; revisión externa pendiente a cargo de Codex)  
**Estado:** `en_revision`  

Este glosario define unívocamente la terminología técnica del ecosistema Jev y el programa de investigación, fijando distinciones críticas para evitar confusiones operativas.

---

## Términos Fundamentales

### System One Model (Modelo de Sistema Uno)
Categoría de modelo de lenguaje/inteligencia artificial diseñada para responder de forma reactiva, directa y rápida emitiendo una estructura tipada o decisión sin generar tokens intermedios de texto libre o cadenas de pensamiento (*Chain-of-Thought*). Inspirado en la teoría dual de Daniel Kahneman, se opone a los modelos de "Sistema Dos" (que gastan tiempo de cómputo deliberando en texto).

### Jev
Nombre propio del modelo fundacional de Sistema Uno desarrollado por **TypeSafe AI Inc.** (versión de referencia documentada: `jev-1.13.0`). Su nombre alude a la Paradoja de Jevons (William Stanley Jevons). Inferencia disponible exclusivamente a través de la API `POST /v1/systemone` con tarifa oficial de $0.042 por millón de tokens de entrada (salida gratuita).

### jeff
Proyecto comunitario independiente de código abierto creado por **Logan Markewich** (`logan-markewich/jeff`). Implementa un servidor con interfaz API compatible con Jev montado sobre el modelo abierto GLiFormer-large-v1 (400M parámetros). No comparte pesos ni arquitectura con el Jev oficial.

### Choice
Primitiva nativa de Jev para clasificación categórica discreta entre un conjunto finito y mutuamente excluyente de opciones declaradas en `criteria`. Retorna contractualmente: `choice` (str), `probabilities` (dict[str, float]) y `confidence` (float en $[0, 1]$).

### Score
Primitiva nativa de Jev para emitir una valoración escalar u ordinal en una escala numérica definida (ej. 0 a 3 o 1 a 5) con leyendas semánticas asociadas. Retorna contractualmente: `score` (int), `legend` (str), `probabilities` (dict[int, float]) y `confidence` (float en $[0, 1]$).

### Noul
Primitiva nativa de Jev para evaluar de forma continua el grado de satisfacción de una condición lógica o fáctica dada en el texto de entrada. Retorna exclusivamente: `noul` (float en $[0, 1]$). **No devuelve campo `confidence` nativo del proveedor**. La interpretación de certeza o distancia respecto a la incertidumbre máxima ($|2p - 1|$) es una métrica determinista calculada en la CPU del cliente.

### Transformación de Distancia de Convicción ($|2p - 1|$)
Operación determinista ejecutada localmente en el cliente sobre el valor de `noul` ($p \in [0, 1]$). Mapea el valor a la escala $[0, 1]$ donde 0 representa ambigüedad máxima ($p = 0.50$) y 1 representa certeza extrema ($p \in \{0.0, 1.0\}$). No es un campo retornado por la API de TypeSafe.

### RLCD (Reinforcement Learning from Classifier Feedback / AI Feedback)
Técnica de optimización de políticas para modelos de decisión donde la retroalimentación proviene de clasificadores o evaluadores automáticos que penalizan la descalibración y el error semántico de formato.

### Calibración
Propiedad probabilística de un clasificador según la cual la confianza predicha ($p$) refleja la frecuencia real observada de acierto ($P(\hat{y} = y \mid \hat{p} = p) = p$). Se evalúa mediante el Error de Calibración Esperado (ECE) y el Brier Score. Se distingue de la exactitud o la discriminación (ROC-AUC).

### Jaggedness (Capacidad Irregular)
Patrón no lineal de capacidades de un modelo de IA donde sobresale en tareas complejas de clasificación pero falla en tareas triviales adyacentes debido a la ausencia de cómputo deliberativo.

### Invarianza Dialectal (INV)
Propiedad de robustez semántica según la cual una decisión tipada y su confianza asociada se mantienen estables ($f(x') = f(x)$) ante paráfrasis y modismos regionales (ej. español chileno vs. estándar) que conservan la intención transaccional.

### Sensibilidad Direccional (DIR / Contrast Sets)
Propiedad según la cual una alteración mínima pero semánticamente decisiva en el texto (ej. partícula restrictiva "salvo que" o negador) produce necesariamente un cambio en la decisión tipada ($f(x'') \neq f(x)$).

### Patrón de Emisión Dual Tipada (PEDT)
Arquitectura de salida desacoplada que emite simultáneamente una estructura normalizada canónica para bases de datos y motores de ejecución (FIX/SQL) y una cita textual literal inmutable firmada criptográficamente (SHA-256) para auditoría legal y humana.

### Worst-Slice Recall (WSR)
Métrica de gobernanza que evalúa la capacidad de detección del modelo en el fenómeno lingüístico o subgrupo con peor rendimiento ($\min_k \text{Recall}_k$), bloqueando despliegues si cae por debajo del 80% independientemente del promedio global.

### Soberanía Determinista
Principio rector de ingeniería que establece que el flujo de control, la validación de invariantes, la autorización de acciones y la persistencia de datos son gobernados exclusivamente por código de software determinista y verificable, manteniendo a los modelos de inteligencia artificial como evaluadores semánticos subordinados.

### Early-Exit Triage (Salida Rápida)
Patrón arquitectónico jerárquico donde un modelo rápido y de bajo coste (Sistema 1) resuelve la mayoría de las solicitudes rutinarias en $<150$ ms, escalando a modelos deliberativos más pesados (Sistema 2) o a humanos solo cuando la incertidumbre excede los umbrales seguros.

### Circuit Breaker Semántico
Mecanismo de protección de software que monitoriza la salud de las respuestas del modelo. Si se detectan más de $N$ fallos consecutivos, respuestas inválidas o caídas drásticas en el margen de convicción, el circuito se abre y desvía inmediatamente el tráfico a rutas de respaldo deterministas.

### Point-in-Time Integrity (Procedencia Temporal)
Garantía metodológica estricta en estudios históricos o cuantitativos (QRT) que asegura que ningún componente o modelo acceda a información, revisiones o documentos publicados con posterioridad al instante exacto de la decisión simulada, erradicando el sesgo de anticipación (*lookahead bias*).

### Error Masking Seguro
Regla estricta de desarrollo en Python que prohíbe exponer mensajes internos de excepción o stack traces en respuestas al usuario o registros centralizados, empleando obligatoriamente `type(err).__name__` con el sufijo `(detalles omitidos por seguridad)`.

### Coste Total de Propiedad (TCO)
Evaluación económica integral de un flujo automatizado que suma: inferencia de tokens, preparación en CPU, infraestructura auxiliar, amortización de ingeniería, supervisión humana de casos inciertos (HITL, componente mayoritario), coste del error residual y mantenimiento continuo.

### Provider Abstraction Layer (PAL / Decision Gateway)
Capa de software intermedia que desacopla la aplicación anfitriona de la API propietaria de TypeSafe, permitiendo sustituir proveedores o utilizar réplicas locales abiertas (`jeff`) mediante contratos de interfaz estandarizados.

### RetryPolicy (Política de Reintentos)
Clase canónica de `typesafe-sdk==0.7.0` (`typesafe.policy.RetryPolicy`) para gobernar reintentos automáticos ante errores de transporte o códigos HTTP 429 transitorios. Sus parámetros oficiales son: `max_retries` (int, por defecto 2), `backoff_initial` (float, por defecto 0.5s), `backoff_max` (float, por defecto 5.0s), `backoff_jitter` (bool o float, por defecto True) y `timeout` (float, por defecto 10.0s). El parámetro obsoleto `backoff_factor` ha sido eliminado del SDK 0.7.0 en favor de la decorrelación exponencial con jitter.
