# Guía Maestra de Adopción y Uso de Jev AI — Manual Canónico

**Versión:** 2.0.0 (Remediación Integral y Normalización Canónica)  
**Fecha de Publicación:** 2026-09-20  
**Responsable del Programa:** Antigravity (Autorrevisión técnica integral; revisión externa independiente pendiente a cargo de Codex)  
**Alcance:** Marco unificado de ingeniería, arquitectura, gobernanza y cartera de pilotos para los 18 pilares de investigación (P01–P18) y síntesis transversal (Pilar X).  
**Estado:** `en_revision` (Basado en 384/384 respuestas autorrevisadas y saneadas, listas para auditoría externa por parte de Codex)  

---

## 1. Declaración Unificada de Principios y Naturaleza de Jev

TypeSafe Jev (versión de referencia congelada `jev-1.13.0`) es un **modelo de inferencia semántica ligera de Sistema 1**, alojado por TypeSafe AI y accesible exclusivamente mediante el endpoint `POST /v1/systemone`. Su diseño está optimizado para emitir estructuras de salida discretas tipadas a partir de un estado de entrada estructurado (`state`, hasta 64k tokens) y un diccionario de preguntas cerradas.

### Principios Innegociables de Ingeniería:
1. **Soberanía Determinista**: El código de software anfitrión en CPU gobierna de forma absoluta el flujo de control, la persistencia en bases de datos, las reglas de negocio y los efectos colaterales. Jev actúa exclusivamente como un servicio de juicio semántico rápido, jamás como un orquestador autónomo con mutaciones no supervisadas.
2. **Asimetría de Riesgo y Veto Operativo**: En decisiones que comprometan capital financiero (QRT), personas y relaciones laborales (Wheelwork) o infraestructura crítica, la inferencia de Jev solo puede actuar como filtro previo o sugerencia asistida; la autorización final y la responsabilidad legal corresponden obligatoriamente a una compuerta determinista o a un operador humano calificado (Human-in-the-Loop).
3. **Ausencia de Infalibilidad Semántica**: La propiedad de "ausencia de alucinaciones sintácticas" garantizada por TypeSafe se refiere estrictamente a la **adherencia tipada al esquema JSON**, no a la veracidad fáctica universal de sus decisiones. Un juicio sintácticamente válido puede ser fácticamente erróneo ante entradas ambiguas, sesgadas o fuera de distribución (OOD).
4. **Desacoplamiento y Portabilidad (Decision Gateway)**: Todo diseño de software debe encapsular las llamadas a Jev mediante un adaptador agnóstico de proveedor, asegurando que el sistema anfitrión pueda operar con modelos locales alternativos (`jeff`), heurísticas deterministas o reglas locales ante interrupciones de servicio o cambios unilaterales en la API.
5. **Economía de Escala Verificada**: La tarifa contractual documentada es de **USD 0.042 por millón de tokens de entrada** (salida sin coste). No obstante, el Coste Total de Propiedad (TCO) está dominado por la tasa de escalamiento a revisión humana (HITL); si la abstención supera el 15%, los sobrecostes humanos superan el ahorro de computación.

---

## 2. Matriz Universal de Asignación Tecnológica

Para erradicar la sobreingeniería y el uso indebido de modelos de lenguaje, el equipo debe aplicar estrictamente la siguiente matriz de selección funcional:

| Requerimiento del Sistema | Tecnología Mandatoria | Criterio de Selección | Riesgo si se usa otra herramienta |
|---|---|---|---|
| **Cálculo matemático, contabilidad, fechas, sumas** | **Código Determinista** (Python / SQLite) | Exactitud $100\%$, coste cero, latencia $<1$ ms. | Los modelos semánticos cometen errores de redondeo e inconsistencias numéricas. |
| **Búsqueda léxica, filtrado relacional, recuperación por ID** | **Bases de Datos Relacionales / Vectoriales / BM25** | Recuperación exacta indexada y escalable. | Intentar buscar con Jev degrada la cobertura y satura la ventana de contexto. |
| **Juicio semántico rápido, clasificación tipada, triaje temprano** | **TypeSafe Jev (Sistema 1)** | Latencia $70–300$ ms, coste \$0.042/Mtok, tipado cerrado. | Usar LLMs de 70B encarece el sistema y añade $800+$ ms de latencia innecesaria. |
| **Redacción abierta, síntesis multifuente, explicación extensa** | **LLM Generativo (Sistema 2: Claude / GPT-4)** | Razonamiento deliberativo complejo y generación de prosa. | Jev carece de decodificador autorregresivo abierto para generar texto libre. |
| **Autorización de trading, descarte laboral, acciones irreversibles** | **Operador Humano Responsable (HITL)** | Cumplimiento legal, ético y responsabilidad fiduciaria. | Prohibición regulatoria absoluta de automatización desatendida. |

---

## 3. Primitivas Oficiales de la API TypeSafe

Toda integración técnica debe ajustarse a las especificaciones exactas del proveedor (`SRC-0002`):

1. **`Choice`**:
   - Parámetros: `instructions` (str), `criteria` (dict[str, str]).
   - Retorno oficial: `choice` (str), `probabilities` (dict[str, float]), `confidence` (float en $[0, 1]$).
2. **`Score`**:
   - Parámetros: `instructions` (str), `scale` (int), `criteria` (dict[int, str]).
   - Retorno oficial: `score` (int), `legend` (str), `probabilities` (dict[int, float]), `confidence` (float en $[0, 1]$).
3. **`Noul`**:
   - Parámetros: `instructions` (str), `condition` (str).
   - Retorno oficial: `noul` (float en $[0, 1]$).
   - **Advertencia crítica de contrato**: `Noul` **NO** devuelve campo `confidence` nativo del proveedor. La transformación de certidumbre $|2p - 1|$ es una métrica determinista ejecutada localmente en la CPU del cliente.

---

## 4. Patrones de Arquitectura Canónicos

### 4.1. Enrutamiento Semántico y Salida Rápida (*Early-Exit Triage*)
En flujos de alta concurrencia, Jev evalúa la complejidad o intención de la solicitud. Si la confianza supera el umbral de corte calibrado ($\gamma \ge 0.85$), el software resuelve inmediatamente la consulta mediante plantillas o microservicios deterministas en $<150$ ms, escalando a un LLM de Sistema 2 únicamente el $15–25\%$ de casos complejos.

### 4.2. Mecanismo de Doble Veto y *Circuit Breaker*
1. **Primer Veto**: Validación determinista de invariantes en cliente (CPU) antes de la llamada de red (sanitización de PII y regex de secretos).
2. **Inferencia Semántica**: Evaluación con Jev en `POST /v1/systemone`. Si el margen de separación entre opciones colapsa o la confianza es baja ($\gamma < 0.75$), se activa la abstención forzada.
3. **Segundo Veto**: Si el servicio registra más de 3 anomalías consecutivas o timeouts (> 450 ms), el *Circuit Breaker* transiciona a estado `OPEN`, desviando el tráfico a rutas de contingencia deterministas sin interrumpir el servicio anfitrión.
4. **Manejo Seguro de Excepciones**: Todo bloque `except` en Python debe utilizar `type(err).__name__` con el sufijo `(detalles omitidos por seguridad)` para evitar fugas de tokens o credenciales en registros de auditoría.

---

## 5. Gobernanza y Regulaciones por Ecosistema

### 5.1. Ecosistema QRT (Trading Cuantitativo)
- **Aislamiento de Red Total (Air-Gap Lógico)**: Queda terminantemente prohibido conectar las salidas de Jev a la capa de ejecución de órdenes en MetaTrader 5 (MT5) o pasarelas FIX.
- **Procedencia Temporal Inmutable (Point-in-Time)**: Todo documento y noticia debe registrar su marca de tiempo UTC de primera emisión pública antes de ser procesado, erradicando el sesgo de anticipación (*lookahead bias*).
- **Prohibición de Señales Alfa**: Se veta tratar clasificaciones textuales como señales directas de compra/venta o atribuir rentabilidad a la precisión lingüística.

### 5.2. Ecosistema Wheelwork (Talento y Consultoría)
- **Garantías de No Discriminación y Privacidad**: El preprocesador en CPU debe anonimizar nombres, género, edad, domicilios y colegios antes de invocar la API.
- **Prohibición de Descarte Autónomo**: Jev solo puede actuar como asistente para emparejar requisitos documentados con competencias acreditadas; todo descarte o selección de candidatos exige el visto bueno expreso de un consultor humano calificado.
- **Pruebas Contrafactuales Obligatorias**: Verificación continua de que candidatos con trayectorias idénticas pero atributos demográficos permutados obtienen idéntico resultado.

### 5.3. Ecosistema de Productividad Personal
- **Confirmación Expresa para Acciones Irreversibles**: Borrado de archivos, pagos y envíos de mensajes exigen confirmación humana obligatoria.
- **Evaluación de Tiempo Neto Ahorrado**: Si el tiempo de supervisión y corrección supera al tiempo del proceso manual, la automatización debe retirarse.

---

## 6. Índice y Mapa de Navegación del Programa

### Síntesis de Pilares Temáticos (P01–P18):
- [Pilar P01 — Identidad, Límites y Arquitectura](P01.md)
- [Pilar P02 — Entrada de Contexto y Ventana](P02.md)
- [Pilar P03 — Primitivas de Decisión y Salida Tipada](P03.md)
- [Pilar P04 — Calibración, Confianza y Probabilidades](P04.md)
- [Pilar P05 — Evaluación, Benchmarks y Calidad](P05.md)
- [Pilar P06 — Latencia, Rendimiento y Concurrencia](P06.md)
- [Pilar P07 — Integración y Patrones Arquitectónicos](P07.md)
- [Pilar P08 — Robustez, Casos Límite y Degradación](P08.md)
- [Pilar P09 — Calibración OOD y Deriva Semántica](P09.md)
- [Pilar P10 — Orquestación, Enrutamiento y Composición](P10.md)
- [Pilar P11 — Seguridad, Guardrails y Verificación Defensiva](P11.md)
- [Pilar P12 — Operación en Producción, Telemetría y SRE](P12.md)
- [Pilar P13 — Economía, Coste Total y Alternativas](P13.md)
- [Pilar P14 — Flujos Personales y Productividad](P14.md)
- [Pilar P15 — QRT: Trading Cuantitativo y Soberanía Operativa](P15.md)
- [Pilar P16 — Wheelwork: Recursos Humanos y Gobernanza Ética](P16.md)
- [Pilar P17 — Metodología de Investigación y Aprendizaje Acumulativo](P17.md)
- [Pilar P18 — Nuevos Productos, SaaS y Viabilidad Comercial](P18.md)

### Respuestas Transversales del Pilar X (JEV-X-001 a JEV-X-024):
Las 24 respuestas normativas se encuentran catalogadas en `base-conocimiento/respuestas/X/`:
- [JEV-X-001](../respuestas/X/JEV-X-001.md) a [JEV-X-006](../respuestas/X/JEV-X-006.md): Fundamentos, matrices de decisión y biblioteca de recetas.
- [JEV-X-007](../respuestas/X/JEV-X-007.md) a [JEV-X-012](../respuestas/X/JEV-X-012.md): Contratos de evidencia, políticas de calidad, privacidad y batería de pruebas.
- [JEV-X-013](../respuestas/X/JEV-X-013.md) a [JEV-X-017](../respuestas/X/JEV-X-017.md): Cartera de pilotos prioritarios, presupuesto TCO y observabilidad de valor.
- [JEV-X-018](../respuestas/X/JEV-X-018.md) a [JEV-X-024](../respuestas/X/JEV-X-024.md): Capacitación, 20 casos de estudio, vigencia, vacíos y auditoría final.
