# Guía Maestra de Adopción y Uso de Jev AI — Manual Canónico

**Versión:** 1.0.0 (Consolidación Etapas B, C y D)  
**Fecha de Publicación:** 2026-09-20  
**Responsable del Programa:** Antigravity (Auditoría Independiente Integral)  
**Alcance:** Marco unificado de ingeniería, arquitectura, gobernanza y cartera de pilotos para los 18 pilares de investigación (P01–P18) y síntesis transversal (Pilar X).  
**Estado:** Documento Normativo Aprobado (Basado en 384/384 respuestas aceptadas)  

---

## 1. Declaración Unificada de Principios y Naturaleza de Jev

TypeSafe Jev (versión de referencia `jev-1.13.0`) es un **modelo de Sistema 1 especializado en evaluación semántica tipada, rápida (10–25 ms) y de bajo coste ($0.0002/decisión)**, optimizado para emitir estructuras de salida discretas (`Choice`, `Noul`, `Score`) a partir de un estado tipado (`state`) y una pregunta cerrada (`question`).

### Principios Innegociables de Ingeniería:
1. **Soberanía Determinista**: El código de software anfitrión gobierna de forma absoluta el flujo de control, la persistencia en bases de datos, las reglas de negocio y los efectos colaterales. Jev actúa como un servicio de juicio semántico, jamás como un orquestador autónomo.
2. **Asimetría de Riesgo y Veto Operativo**: En decisiones que comprometan capital (QRT), personas (Wheelwork) o infraestructura crítica, la inferencia de Jev solo puede actuar como filtro previo o sugerencia asistida; la autorización final y la responsabilidad legal o financiera corresponden obligatoriamente a una compuerta determinista o a un operador humano calificado.
3. **Ausencia de Infalibilidad Semántica**: La propiedad de "ausencia de alucinaciones" garantizada por TypeSafe se refiere exclusivamente a la **adherencia estricta al esquema tipado**, no a la veracidad fáctica universal de sus decisiones. Un formato sintácticamente válido puede ser fácticamente erróneo si la entrada está fuera de distribución o contiene ruido adversarial.
4. **Desacoplamiento y Portabilidad**: Todo diseño de software debe encapsular las llamadas a Jev mediante una Capa de Abstracción de Proveedor (PAL), asegurando que el sistema pueda operar con modelos locales alternativos (`jeff`) o heurísticas de respaldo ante interrupciones de servicio o cambios en la API.

---

## 2. Matriz Universal de Asignación Tecnológica

Para erradicar la sobreingeniería y el uso indebido de modelos de lenguaje, el equipo debe aplicar estrictamente la siguiente matriz de selección funcional:

| Requerimiento del Sistema | Tecnología Mandatoria | Criterio de Selección | Riesgo si se usa otra herramienta |
|---|---|---|---|
| **Cálculo matemático, contabilidad, validaciones sintácticas** | **Código Determinista** (Python / TypeScript) | Exactitud $100\%$, coste cero, latencia $<1$ ms. | Los LLMs y clasificadores semánticos cometen errores de redondeo e inconsistencias. |
| **Búsqueda léxica, filtrado relacional, recuperación por ID** | **Bases de Datos Relacionales / Vectoriales / BM25** | Recuperación exacta indexada y escalable. | Intentar buscar con Jev degrada la cobertura y satura la ventana de contexto. |
| **Juicio semántico rápido, clasificación tipada, triaje temprano** | **TypeSafe Jev (Sistema 1)** | Latencia 15 ms, coste $10	imes$ menor que GPT-4o-mini, tipado cerrado. | Usar LLMs de 70B encarece el sistema y añade $400+$ ms de latencia innecesaria. |
| **Redacción abierta, síntesis multifuente, explicación contextual** | **LLM Generativo (Sistema 2: Claude / GPT-4)** | Razonamiento deliberativo complejo y generación de prosa. | Jev carece de capacidad de generar texto libre o explicaciones explicativas extensas. |
| **Autorización de trading, descarte laboral, mutaciones críticas** | **Operador Humano Responsable (HITL)** | Cumplimiento legal, ético y responsabilidad fiduciaria. | Prohibición regulatoria absoluta de automatización desatendida. |

---

## 3. Patrones de Arquitectura Canónicos

### 3.1. Enrutamiento Semántico y Salida Rápida (*Early-Exit Triage*)
En flujos de alta concurrencia, Jev evalúa la complejidad o intención de la solicitud. Si la confianza supera el umbral de corte calibrado ($\gamma \ge 0.85$), el software resuelve inmediatamente la consulta mediante plantillas o microservicios deterministas en $<40$ ms, escalando a un LLM de Sistema 2 únicamente el $15–25\%$ de casos complejos.

### 3.2. Mecanismo de Doble Veto y *Circuit Breaker*
1. **Primer Veto**: Validación determinista de invariantes en cliente antes de la llamada de red.
2. **Inferencia Semántica**: Evaluación con Jev. Si el margen de separación entre opciones colapsa ($\gamma < 0.20$), se activa la abstención forzada.
3. **Segundo Veto**: Si el servicio registra más de 3 anomalías consecutivas o timeouts, el *Circuit Breaker* transiciona a estado `OPEN`, desviando el tráfico a rutas de contingencia deterministas sin interrumpir el servicio.

---

## 4. Gobernanza y Regulaciones por Ecosistema

### 4.1. Ecosistema QRT (Trading Cuantitativo)
- **Aislamiento Total**: Queda terminantemente prohibido conectar las salidas de Jev a la capa de ejecución de órdenes en MetaTrader 5 (MT5).
- **Procedencia Temporal Inmutable**: Todo dato no estructurado debe registrar su marca de tiempo UTC de primera publicación antes de ser procesado como variable de investigación cuantitativa, evitando el sesgo de anticipación (*lookahead bias*).

### 4.2. Ecosistema Wheelwork (Talento y Consultoría)
- **Garantías de No Discriminación**: El preprocesador debe anonimizar nombres, género, edad y datos de contacto antes de invocar la API.
- **Prohibición de Descarte Autónomo**: Jev solo puede actuar como asistente para emparejar requisitos documentados con competencias acreditadas; todo descarte o selección de candidatos exige el visto bueno expreso de un consultor humano calificado.

---

## 5. Índice y Mapa de Navegación del Programa

### Síntesis de Pilares Temáticos:
- [Pilar P01 — Evidencia y Afirmaciones](P01.md)
- [Pilar P02 — Arquitectura y RLCD](P02.md)
- [Pilar P03 — Diseño de Decisiones](P03.md)
- [Pilar P04 — Contexto y Preparación de Datos](P04.md)
- [Pilar P05 — Probabilidad, Calibración y Abstención](P05.md)
- [Pilar P06 — Evaluación Independiente](P06.md)
- [Pilar P07 — Español y Lenguaje Sectorial](P07.md)
- [Pilar P08 — Arquitecturas Híbridas](P08.md)
- [Pilar P09 — API, Conectores e Integración](P09.md)
- [Pilar P10 — Búsqueda y Conocimiento](P10.md)
- [Pilar P11 — Seguridad y Verificación](P11.md)
- [Pilar P12 — Operación y Mantenimiento](P12.md)
- [Pilar P13 — Economía y Alternativas](P13.md)
- [Pilar P14 — Flujos Personales](P14.md)
- [Pilar P15 — QRT](P15.md)
- [Pilar P16 — Wheelwork](P16.md)
- [Pilar P17 — Investigación y Aprendizaje Acumulativo](P17.md)
- [Pilar P18 — Nuevos Productos y Posibilidades](P18.md)

### Respuestas Transversales del Pilar X (JEV-X-001 a JEV-X-024):
Las 24 respuestas normativas se encuentran catalogadas en `docs/programa-jev/base-conocimiento/respuestas/X/` con acceso directo por identificador canónico:
- [JEV-X-001](../respuestas/X/JEV-X-001.md) a [JEV-X-006](../respuestas/X/JEV-X-006.md): Fundamentos, matrices de decisión y biblioteca de recetas.
- [JEV-X-007](../respuestas/X/JEV-X-007.md) a [JEV-X-012](../respuestas/X/JEV-X-012.md): Contratos de evidencia, políticas de calidad, privacidad y batería de pruebas.
- [JEV-X-013](../respuestas/X/JEV-X-013.md) a [JEV-X-017](../respuestas/X/JEV-X-017.md): Cartera de pilotos prioritarios, presupuesto y observabilidad de valor.
- [JEV-X-018](../respuestas/X/JEV-X-018.md) a [JEV-X-024](../respuestas/X/JEV-X-024.md): Capacitación, casos de estudio, vigencia, vacíos y auditoría final.
