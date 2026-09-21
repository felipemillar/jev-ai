# Glosario Canónico — Programa Jev

Versión: 1.0.0  
Última actualización: 2026-09-19  
Responsable de integración: Antigravity  

Este glosario define unívocamente la terminología técnica del ecosistema Jev y el programa de investigación, fijando distinciones críticas para evitar confusiones operativas.

---

## Términos Fundamentales

### System One Model (Modelo de Sistema Uno)
Categoría de modelo de lenguaje/inteligencia artificial diseñada para responder de forma reactiva, directa y rápida emitiendo una estructura tipada o decisión sin generar tokens intermedios de texto libre o cadenas de pensamiento (*Chain-of-Thought*). Inspirado en la teoría dual de Daniel Kahneman, se opone a los modelos de "Sistema Dos" (que gastan tiempo de cómputo deliberando en texto).

### Jev
Nombre propio del modelo fundacional de Sistema Uno desarrollado por **TypeSafe AI Inc.** (versión de referencia documentada: `jev-1.13.0`). Su nombre alude a la Paradoja de Jevons (William Stanley Jevons).

### jeff
Proyecto comunitario independiente de código abierto creado por **Logan Markewich** (`logan-markewich/jeff`). Implementa un servidor con interfaz API compatible con Jev montado sobre el modelo abierto GLiFormer-large-v1 (400M parámetros). No comparte pesos ni arquitectura con el Jev oficial.

### Choice
Primitiva nativa de Jev para clasificación categórica discreta entre un conjunto finito y mutuamente excluyente de opciones, retornando la opción ganadora junto con sus probabilidades calibradas.

### Score
Primitiva nativa de Jev para emitir una valoración escalar numérica (generalmente en una escala de 1 a 5 o rúbrica continua/ordinal) evaluando un criterio respecto al estado proporcionado.

### Noul
Primitiva o salida nativa de Jev que indica abstención formal o rechazo a decidir cuando la evidencia provista en el estado es insuficiente, ambigua o contradictoria, evitando la emisión de una decisión forzada no fundamentada.

### RLCD (Reinforcement Learning from Classifier Feedback / AI Feedback)
Técnica de optimización de políticas para modelos de decisión donde la retroalimentación proviene de clasificadores o evaluadores automáticos que penalizan la descalibración y el error semántico de formato.

### Calibración
Propiedad probabilística de un clasificador según la cual la confianza predicha ($p$) refleja la frecuencia real observada de acierto ($P(\hat{y} = y \mid \hat{p} = p) = p$). Se distingue de la exactitud o la discriminación (ROC-AUC).

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
Patrón arquitectónico jerárquico donde un modelo rápido y de bajo coste (Sistema 1) resuelve la mayoría de las solicitudes rutinarias en $<40$ ms, escalando a modelos deliberativos más pesados (Sistema 2) o a humanos solo cuando la incertidumbre excede los umbrales seguros.

### Circuit Breaker Semántico
Mecanismo de protección de software que monitoriza la salud de las respuestas del modelo. Si se detectan más de $N$ fallos consecutivos, respuestas inválidas o caídas drásticas en el margen de convicción, el circuito se abre y desvía inmediatamente el tráfico a rutas de respaldo deterministas.

### Point-in-Time Integrity (Procedencia Temporal)
Garantía metodológica estricta en estudios históricos o cuantitativos (QRT) que asegura que ningún componente o modelo acceda a información, revisiones o documentos publicados con posterioridad al instante exacto de la decisión simulada, erradicando el sesgo de anticipación.

### FrugalGPT
Estrategia de optimización económica de inferencia en inteligencia artificial que combina cascadas de modelos, almacenamiento en caché de respuestas y enrutamiento adaptativo para minimizar el coste total sin degradar la precisión percibida por el usuario.

### Provider Abstraction Layer (PAL)
Capa de software intermedia que desacopla la aplicación anfitriona de la API propietaria de TypeSafe, permitiendo sustituir proveedores o utilizar réplicas locales abiertas (`jeff`) mediante contratos de interfaz estandarizados.

