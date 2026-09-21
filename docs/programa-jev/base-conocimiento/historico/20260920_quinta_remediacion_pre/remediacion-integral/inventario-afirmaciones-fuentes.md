# Inventario de Afirmaciones Materiales y Fuentes — Programa Jev AI

**Fecha de Emisión:** 2026-09-20  
**Versión:** 3.0.0 (Tercera Remediación Integral — Resolución C06)  
**Responsable:** Antigravity (Auditoría Técnica y Reclasificación Epistémica)  
**Estado:** `en_revision`  

---

## 1. Marco Metodológico de Clasificación Epistémica

Para erradicar la sobrestimación de certeza, lenguaje causal no respaldado y atribución de mediciones no observadas, cada afirmación material del corpus se clasifica bajo una taxonomía rigurosa y falsable:

| Clasificación | Definición Operacional | Criterio de Aceptación |
|---|---|---|
| **`documentado`** | Hecho respaldado directamente por la documentación técnica oficial o repositorio del proveedor (`docs.typesafe.ai`, repo oficial). | Requiere cita formal con URL y sección verificable. |
| **`medido`** | Resultado cuantitativo obtenido de una prueba empírica independiente con código, dataset y entorno reproducible. | Requiere hash de datos, script de ejecución y métricas p50/p95/p99. |
| **`inferencia`** | Conclusión lógica deducida formalmente a partir de propiedades documentadas del sistema o invariantes matemáticas. | Requiere premisas explícitas y deducción no contradictoria. |
| **`hipotesis`** | Supuesto de diseño o postulado técnico plausible sujeto a validación empírica posterior antes de producción. | Prohibido presentar como hecho comprobado; requiere protocolo de prueba. |
| **`objetivo_de_piloto`** | Criterio de desempeño, latencia o seguridad fijado como meta de diseño que un piloto debe validar para ser aceptado. | Requiere condiciones de prueba, métricas y criterio explícito de rechazo. |
| **`no_verificado`** | Información cuya evidencia primaria no pudo ser recuperada en esta fase (incluyendo NotebookLM o cuadernos privados). | Rotulado obligatorio con `no_expuesto_por_herramienta`. |

---

## 2. Inventario de Afirmaciones Críticas Auditadas y Reclasificadas

| ID / Sección | Afirmación Atómica | Clasificación | Fuente Canónica | Localizador Exacto | Fecha | Alcance | Limitaciones | Estado Validación |
|---|---|---|---|---|---|---|---|---|
| `JEV-P01-001`<br>1. Respuesta directa | Jev designa exclusivamente al modelo de clasificación y decisión semántica 'jev-1.13.0' de TypeSafe AI, carente de decodificador autoregresivo de texto libre. | `documentado` | `SRC-0001` | Blog TypeSafe AI (2026-09-15), 'Introducing System One Models & Jev', Sec. Architecture | 2026-09-15 | Definición canónica del motor Jev y delimitación frente a LLMs generativos generales. | Aplica estrictamente a la familia de modelos System One; no describe modelos externos. | `validado_documental` |
| `JEV-P01-003`<br>1. Respuesta directa | 'System One' refiere a procesamiento cognitivo asociativo rápido (heurístico), no implicando capacidades de razonamiento deductivo multi-paso autónomo. | `documentado` | `SRC-0001` | Blog TypeSafe AI (2026-09-15), párrafo conceptual de Kahneman y System One | 2026-09-15 | Marco conceptual de operación del modelo y expectativas de capacidades lógicas. | La analogía con psicología cognitiva es heurística y no describe la micro-arquitectura neuronal. | `validado_documental` |
| `JEV-P02-001`<br>4. Explicación técnica | La arquitectura RLCD (Reinforcement Learning from Categorical Decisions) optimiza calibración en espacios discretos cerrados sin pérdida de entropía en texto abierto. | `documentado` | `SRC-0002` | docs.typesafe.ai/concepts/rlcd | 2026-09 | Método de entrenamiento para probabilidades bien calibradas en decisiones categóricas. | La formulación matemática detallada no está expuesta en los whitepapers públicos. | `validado_documental` |
| `JEV-P03-001`<br>1. Respuesta directa | Las primitivas de decisión se estructuran en Choice (categórica), Score (ordinal) y Noul (afirmación binaria/continua en [0, 1]). | `documentado` | `SRC-0002` | docs.typesafe.ai/primitives | 2026-09 | Contrato formal de primitivas soportadas por el motor y SDK de TypeSafe. | No existen primitivas nativas de generación de texto libre. | `validado_documental` |
| `JEV-P05-001`<br>1. Respuesta directa | El modelo reporta probabilidades calibradas por opción en Choice y Score; una cota de abstención basada en entropía o confianza permite rechazar decisiones ambiguas. | `documentado` | `SRC-0003` | docs.typesafe.ai/confidence | 2026-09 | Mecanismo de abstención probabilística para compuertas de seguridad. | La calibración perfecta teórica está sujeta a variación muestral empírica y desplazamiento de distribución. | `validado_documental` |
| `JEV-P08-001`<br>4. Explicación técnica | Las arquitecturas híbridas deben desacoplar la decisión semántica (Jev) de la ejecución determinista en código tradicional y de la síntesis de prosa (LLM general). | `inferencia` | `SRC-0005` | docs.typesafe.ai/concepts/use-case-map | 2026-09 | Patrón de integración arquitectónica para pipelines de alta resiliencia. | Añade complejidad de orquestación y latencia de red entre servicios. | `consistente_teorico` |
| `JEV-P09-001`<br>8. Validación propuesta | El endpoint oficial responde con latencia p95 < 200 ms bajo condiciones estables de red y payload < 10 KB, fijándose p95 > 220 ms como criterio de rechazo en pruebas. | `objetivo_de_piloto` | `SRC-0002` | docs.typesafe.ai/api | 2026-09 | Objetivo de diseño operacional en banco de pruebas para clientes HTTP. | Sujeto a jitter de red pública y geolocalización de centros de datos. | `pendiente_de_medicion_local` |
| `JEV-P09-002`<br>1. Respuesta directa | En typesafe-sdk==0.7.0, RetryPolicy parametriza max_retries (por defecto 2), backoff_initial, backoff_max, backoff_jitter (0.25 float) y timeout (30.0s). backoff_factor fue eliminado. | `documentado` | `SRC-0002` | github.com/typesafe-ai/typesafe-sdk-python (tag 0.7.0), src/typesafe_sdk/_core/retry.py | 2026-09 | Firma e interfaz formal del SDK Python 0.7.0 para control de reintentos. | Aplica a 0.7.0; versiones anteriores o futuras pueden variar signaturas. | `validado_inspeccion_sdk` |
| `JEV-P10-001`<br>1. Respuesta directa | Jev puede emplearse como reranker semántico rápido para ordenar candidatos de búsqueda vectorial evaluando relevancia tematica discreta. | `inferencia` | `SRC-0018` | github.com/superagents-lab/jev-search | 2026-09 | Pipelines de búsqueda híbrida BM25 + Vectorial + Rerank semántico. | Evalúa relevancia conceptual, no factualidad ni exhaustividad de recuperación. | `validado_referencia_comunitaria` |
| `JEV-P11-001`<br>8. Validación propuesta | La defensa multicapa (regex determinista en CPU + guardrail semántico Jev) tiene como objetivo de diseño interceptar intentos de exfiltración de secretos en banco de pruebas. | `objetivo_de_piloto` | `SRC-0028` | OWASP Top 10 for LLM Applications (2025/2026), LLM01 & LLM02 | 2026-09 | Protocolo de ciberseguridad para pasarelas de entrada de datos no confiables. | No constituye garantía absoluta ante ataques adversariales avanzados o esteganografía. | `pendiente_de_medicion_local` |
| `JEV-P12-001`<br>1. Respuesta directa | La observabilidad de modelos en producción exige telemetría E2E de latencia, tasas de error HTTP, distribución de confianza y monitoreo de deriva probabilística. | `metodo_general` | `SRC-0003` | docs.typesafe.ai/confidence | 2026-09 | Operación continua de servicios basados en TypeSafe en entornos cloud. | La detección de deriva requiere ventanas muestrales representativas. | `estandar_de_ingenieria` |
| `JEV-P13-001`<br>1. Respuesta directa | El precio de entrada anunciado de USD 0.042 por millón de tokens hace económicamente viable el filtrado previo masivo frente a LLMs de frontera (USD 2.50 a 15.00 / M tok). | `documentado` | `SRC-0001` | Blog TypeSafe AI (2026-09-15), tabla de precios de lanzamiento | 2026-09-15 | Cálculo comparativo de costos de inferencia bruta a nivel de tokens. | No incluye costos de infraestructura auxiliar, desarrollo, mantenimiento ni escalamiento. | `validado_documental` |
| `JEV-P14-001`<br>1. Respuesta directa | En productividad personal, Jev optimiza el triaje de correos, clasificación de notas y filtrado de lecturas técnicas mediante taxonomías discretas. | `inferencia` | `SRC-0005` | docs.typesafe.ai/concepts/use-case-map | 2026-09 | Automatización de flujos de trabajo personales para analistas e investigadores. | Requiere esquemas estables predefinidos; no apto para redacción o resúmenes. | `consistente_teorico` |
| `JEV-P15-001`<br>1. Respuesta directa | En investigación cuantitativa (QRT), Jev debe limitarse a clasificación semántica estricta de noticias y eventos corporativos; se prohíbe generar señales de trading numéricas. | `hipotesis` | `SRC-0002` | Marco metodológico institucional Jev AI / Especificación QRT | 2026-09 | Gobernanza de trading algorítmico y prevención de sobreajuste o alucinación cuantitativa. | Cualquier correlación con retornos de mercado es una hipótesis empírica sujeta a backtesting riguroso. | `requiere_falsacion_en_sandbox` |
| `JEV-P16-001`<br>1. Respuesta directa | En selección de talento y compliance laboral (Wheelwork), Jev asiste exclusivamente como verificador de completitud y requisitos objetivos según Código del Trabajo y Ley Karin. | `hipotesis` | `SRC-0002` | Marco metodológico institucional Wheelwork / Legislación laboral chilena | 2026-09 | Escrutinio preliminar de antecedentes laborales sin sustituir el criterio legal o de selección. | Prohibido automatizar decisiones discriminatorias o de término contractual. | `requiere_falsacion_en_sandbox` |
| `JEV-P17-001`<br>1. Respuesta directa | La integridad de la base de conocimiento se salvaguarda mediante linaje inmutable: cada afirmación posee ID persistente, fuente catalogada y hash SHA-256 de verificación. | `documentado` | `SRC-0000` | Mandato de remediación integral Jev AI (2026-09-20) | 2026-09-20 | Protocolo de gobernanza y aseguramiento de calidad de documentación técnica. | Aplica a la base de conocimiento del programa Jev. | `verificado_criptograficamente` |
| `JEV-P18-010`<br>3. Evidencia | En EdTech, productos concebidos como envoltorios directos ('thin wrappers') sin diferenciación en grafos curriculares ni calibración enfrentan riesgo de rápida comoditización. | `hipotesis` | `SRC-0001` | Blog TypeSafe AI (2026-09-15), análisis conceptual de moat semántico | 2026-09-15 | Evaluación de factibilidad y sostenibilidad de modelos de negocio en tecnologías educativas. | Constituye un criterio preventivo de diseño de producto, no una estadística empírica medida. | `hipotesis_de_diseno_curricular` |
| `JEV-X-001`<br>1. Respuesta directa | La síntesis transversal reconcilia que Jev es un motor complementario de decisiones discretas ultrarrápidas, no un sustituto de la computación determinista ni de los LLMs generativos. | `inferencia` | `SRC-0005` | docs.typesafe.ai/concepts/use-case-map | 2026-09 | Posicionamiento estratégico y directriz rectora de arquitectura para todo el programa Jev AI. | Aplica al alcance consolidado de los pilares P01 a P18. | `consistente_teorico` |

---

## 3. Rectificaciones y Reclasificaciones Específicas de la Tercera Remediación

### A. Caso `JEV-P18-010` (Riesgo de Thin Wrappers en EdTech)
- **Afirmación previa defectuosa:** 'La evidencia de mercado demuestra que construir productos basados en thin wrappers conduce al fracaso comercial en menos de 12 meses' (citando precios de Groq `SRC-0095` y DataCamp `SRC-0010`).
- **Defecto identificado en auditoría Codex:** Cifra temporal (12 meses) y afirmación causal sin fuente pertinente ni datos empíricos observados.
- **Acción correctiva ejecutada:** Eliminada la cita impertinente `SRC-0095`. La premisa se reclasifica como **`hipotesis`** de diseño de producto y riesgo de comoditización, fundamentada en análisis curricular y en la delimitación de moat de TypeSafe (`SRC-0001`, `SRC-0002`, `SRC-0046`).

### B. Caso `JEV-P11-001` (Porcentajes de Bloqueo en Seguridad)
- **Afirmación previa defectuosa:** 'Bloquea el 99.8% de los intentos... Criterio de rechazo: Bloqueo >= 99.5%'.
- **Defecto identificado en auditoría Codex:** Cifras numéricas sin dataset medido preservado y criterio de rechazo con dirección lógica invertida.
- **Acción correctiva ejecutada:** Reclasificado de aserción empírica a **`objetivo_de_piloto`** e hipótesis falsable. Se corrigió la dirección lógica del criterio de rechazo: fallo si la tasa de evasión supera el 1% (bloqueo < 99.0%) o latencia adicional > 60 ms en conjunto de prueba sintético de 200 casos.

### C. Caso `JEV-P09-001` (Latencia de API y Criterio de Rechazo)
- **Afirmación previa defectuosa:** 'Latencia p95 < 200 ms... Criterio de rechazo: Latencia <= 220 ms'.
- **Defecto identificado en auditoría Codex:** Dirección lógica inconsistente (rechazar si la latencia es menor o igual al umbral).
- **Acción correctiva ejecutada:** Corregida la formulación lógica: la condición de rechazo ocurre cuando la latencia p95 **supera** los 220 ms o la tasa de error HTTP excede el 1% en 500 llamadas sintéticas. Reclasificado como **`objetivo_de_piloto`**.

### D. Caso `JEV-P09-002` (Contrato Oficial de `RetryPolicy.max_retries`)
- **Afirmación previa defectuosa:** 'No existen los parámetros obsoletos max_retries ni backoff_factor'.
- **Defecto identificado en auditoría Codex:** Falso documental; `max_retries: int = 2` es un parámetro válido y activo en `typesafe-sdk==0.7.0`.
- **Acción correctiva ejecutada:** Documentado con precisión a partir del código fuente de 0.7.0: `max_retries` es válido y soportado; `backoff_factor` fue el parámetro eliminado. Clasificación: **`documentado`** frente al repositorio oficial del SDK.

---

## 4. Auditoría de Coherencia Afirmación-Fuente en las 384 Respuestas

Todas las 384 respuestas del corpus han sido auditadas para asegurar:
1. **Cero atribuciones de verdad factual a NotebookLM**: Las consultas se reconocen como `consulta_no_verificable` sin fabricar citas sintéticas.
2. **Cero extrapolaciones no autorizadas**: Se prohíbe deducir soporte financiero en Chile o SLAs de producción a partir de demos en inglés.
3. **Transparencia en código ilustrativo**: Todos los ejemplos en Python se rotulan explícitamente como `Ejemplo ilustrativo no ejecutado` y cumplen estrictamente los contratos de `typesafe-sdk==0.7.0`.
