# Auditoría externa de Codex — Segunda Remediación Integral Jev AI

**Fecha:** 2026-09-20  
**Revisor externo:** Codex  
**Objeto:** verificar de manera independiente la segunda remediación declarada por Antigravity  
**Dictamen:** **NECESITA REVISIÓN — NO ACEPTADA**  
**Estado del corpus:** debe permanecer `en_revision`; `revision_externa` debe permanecer `pendiente`

## 1. Alcance y método

La auditoría no tomó como prueba las cifras del informe de Antigravity. Se ejecutaron controles independientes sobre los 384 archivos de respuesta y se contrastaron los contratos técnicos con:

- la documentación oficial actual del SDK Python: <https://docs.typesafe.ai/sdk/python/>;
- la documentación oficial de `Choice`: <https://docs.typesafe.ai/primitives/choice>;
- la documentación oficial de `Noul`: <https://docs.typesafe.ai/primitives/noul>;
- el repositorio oficial `typesafe-ai/typesafe-sdk-python`: <https://github.com/typesafe-ai/typesafe-sdk-python>;
- el paquete `typesafe-sdk==0.7.0`, instalado en un directorio temporal y utilizado únicamente para validar constructores, sin credenciales ni llamadas a la API.

La revisión combinó una exploración automatizada completa de estructura, sintaxis, hashes, evidencia y firmas del SDK con una revisión semántica dirigida de respuestas, fuentes, afirmaciones e informe de cierre. La correspondencia afirmación-fuente no se verificó manualmente para cada afirmación de las 384 respuestas; los defectos reproducibles encontrados son suficientes para rechazar la aceptación global.

## 2. Controles que sí pasan

| Control | Resultado independiente | Dictamen |
|---|---:|---|
| Archivos de respuesta presentes | 384/384 | Pasa |
| YAML real con `yaml.safe_load()` | 384/384 | Pasa |
| Bloques Python encontrados | 357 | Informativo |
| Sintaxis Python con `ast.parse()` | 357/357 | Pasa solo sintaxis |
| Hashes de respuestas frente a `seguimiento.csv` | 384/384 | Pasa |
| Estado de revisión externa | 384 `pendiente` | Pasa |
| Archivos JSON de consulta presentes | 384/384 | Pasa presencia |
| Snapshot previo | 411 archivos de contenido + manifiesto | Pasa |
| Entradas del manifiesto SHA-256 | 411/411 coincidentes | Pasa |
| Similitud Jaccard 5-gram bajo 0,50 | máximo independiente observado 0,3978 con normalización propia | Pasa la métrica, no demuestra individualización semántica |

El snapshot existe y es íntegro. El nombre real del manifiesto es `manifest-sha256.txt`; el informe declara erróneamente `manifiesto-historico.json`.

## 3. Hallazgos bloqueantes

### C01 — El validador publicado no ejecuta las verificaciones que el informe le atribuye

**Severidad:** P0  
**Ubicación:** `base-conocimiento/remediacion-integral/verificacion-local/test_integrity.py`

El validador llama “YAML válido” a una búsqueda de cadenas como `id:` y `estado: en_revision`; no importa ni ejecuta `yaml.safe_load()`. Tampoco extrae ni analiza bloques Python con `ast.parse()`. La afirmación de que esa suite certificó ambas dimensiones no está respaldada por el código publicado.

El informe menciona `scratch/comprehensive_second_remediation_audit.py`, pero ese archivo no está presente dentro del directorio auditado. Por tanto, la prueba principal declarada no es reproducible desde el entregable.

**Corrección exigida:** publicar un verificador independiente que analice YAML real, AST, firmas de constructores, referencias, hashes y duplicación; hacer que falle con código de salida distinto de cero ante cualquier incumplimiento.

### C02 — Sesenta y nueve respuestas contienen código incompatible con `typesafe-sdk==0.7.0`

**Severidad:** P0  
**Alcance:** 69 archivos; 249 llamadas relevantes inspeccionadas por AST

Se encontraron argumentos no soportados por los constructores oficiales:

| Patrón inválido | Ocurrencias | Contrato oficial |
|---|---:|---|
| `Choice(options=...)` | 62 llamadas en 60 archivos | `Choice(criteria={...})` |
| `Score(min_score=..., max_score=...)` | 8 + 8 | `Score(criteria=[...])` |
| `Score(min_anchor=..., max_anchor=...)` | 3 + 3 | `Score(criteria=[...])` |
| `Score(anchors=...)` | 2 | `Score(criteria=[...])` |
| `Noul(statement=...)` | 6 llamadas en 5 archivos | `Noul(instructions=...)` |

La prueba directa contra el paquete oficial 0.7.0 produjo `ValidationError` para esos constructores. Que el texto compile con `ast.parse()` solo demuestra sintaxis Python; no demuestra que el SDK acepte la llamada.

Ejemplos afectados: `JEV-P09-001`, `JEV-P09-002`, `JEV-P11-001`, `JEV-P18-010` y otros 65 archivos.

**Corrección exigida:** reconstruir cada llamada con `criteria` o `instructions` según corresponda y añadir una prueba sin red que instancie todos los objetos `Choice`, `Score`, `Noul` y `RetryPolicy` extraídos del corpus.

### C03 — La documentación de `RetryPolicy` continúa siendo materialmente falsa

**Severidad:** P0  
**Ubicación principal:** `JEV-P09-002`

La respuesta afirma que `RetryPolicy` posee exclusivamente cuatro argumentos y que `max_retries` ya no existe. El código oficial 0.7.0 define `max_retries: int = 2` y su propia documentación muestra `RetryPolicy(max_retries=3, ...)`.

La prueba directa confirmó:

- `RetryPolicy(max_retries=3)`: válido;
- `RetryPolicy(backoff_factor=1.5)`: inválido.

La remediación eliminó correctamente `backoff_factor`, pero convirtió `max_retries` válido en un supuesto parámetro obsoleto.

**Corrección exigida:** corregir `JEV-P09-002`, todas las síntesis y cualquier guía derivada; generar el inventario de campos directamente desde la firma oficial de 0.7.0.

### C04 — La evidencia de NotebookLM sigue sin estar preservada

**Severidad:** P1  
**Alcance:** 384 archivos JSON de `remediacion-integral/consultas/`

Resultados completos del inventario:

- `conversation_id` vacío: 384/384;
- `referencias_devueltas` vacío: 384/384;
- ausencia de respuesta cruda o completa: 384/384;
- resúmenes de marcador que comienzan con “Verificación individual”: 224/384.

La presencia del JSON demuestra que se creó un registro, pero no demuestra que NotebookLM haya respondido ni qué evidencia entregó. El centinela `no_expuesto_por_herramienta` evita inventar una cita, aunque no permite clasificar el resultado como evidencia suficiente ni como “extracto verificable”.

**Corrección exigida:** preservar la salida real y las referencias cuando la herramienta las exponga. Cuando no las exponga, registrar `consulta_no_verificable`, eliminar extractos presentados como verificados y rebajar el nivel de evidencia correspondiente.

### C05 — El corpus continúa utilizando bloques extensos de plantilla

**Severidad:** P1

La prueba de Jaccard queda por debajo de 0,50, pero el umbral no detecta repetición modular. Se observaron, entre otros:

- un mismo encabezado y párrafo de ejemplo en 64 respuestas de P17, P18 y X;
- un bloque de principios idéntico en las 24 respuestas de X;
- un bloque de arquitectura del conocimiento idéntico en las 20 respuestas de P17;
- un bloque de desarrollo de productos idéntico en las 20 respuestas de P18;
- recomendaciones operativas idénticas dentro de grupos de 20 o 24 respuestas;
- 160 respuestas con la misma frase de trazabilidad;
- 33 párrafos normalizados de al menos 24 palabras repetidos en tres o más respuestas;
- 55 líneas largas repetidas en cinco o más respuestas.

El resultado cumple una prueba numérica estrecha, pero no la exigencia de reconstrucción “100 % individualizada” ni la afirmación de que se eliminó todo el boilerplate.

**Corrección exigida:** separar una plantilla estructural permitida de contenido sustantivo. El verificador debe excluir encabezados y metadatos, analizar por sección y marcar párrafos sustantivos repetidos por encima de un umbral definido.

### C06 — Persisten afirmaciones específicas sin respaldo suficiente o con fuentes no pertinentes

**Severidad:** P1

Ejemplos reproducibles:

- `JEV-P18-010` afirma que los productos “thin wrapper” fracasan comercialmente en menos de 12 meses, sin fuente pertinente que sostenga esa cifra. Sus fuentes incluyen documentos de P06 y un artículo de precios de Groq, que no respaldan esa conclusión educativa o comercial.
- `JEV-P11-001` propone 99,8 % de bloqueo y criterio de 99,5 % sin datos observados.
- `JEV-P09-001` propone p95 menor de 200 ms y luego un “criterio de rechazo” de latencia menor o igual a 220 ms, con dirección lógica inconsistente y sin benchmark preservado.
- Varias respuestas describen resultados concretos del modelo con probabilidades o confianza como si hubieran sido observados, aunque los registros de consulta no conservan la salida que permitiría verificarlos.

**Corrección exigida:** convertir cifras no observadas en objetivos explícitos de piloto, eliminar lenguaje causal o empírico no respaldado y exigir localizador de fuente por afirmación material.

### C07 — La autoevaluación continúa sobreestimando la calidad

**Severidad:** P1

`seguimiento.csv` contiene solo diez combinaciones de rúbrica para 384 respuestas. Los totales reales son:

- 245 respuestas con 22 puntos;
- 120 con 21;
- 14 con 19;
- 5 con 20.

El informe afirma “18/20 a 20/20”, pero existen cinco dimensiones de hasta cinco puntos y los totales observados son 19 a 22 sobre 25. Además, 365 respuestas reciben 21 o 22 puntos pese a la ausencia total de evidencia NotebookLM preservada y a los 69 archivos con contratos inválidos.

**Corrección exigida:** recalcular cada rúbrica después de las correcciones, documentar el denominador correcto `/25` y vincular cada puntaje a pruebas objetivas.

### C08 — Permanece una contradicción activa de versión

**Severidad:** P1  
**Ubicación:** `JEV-P01-001`, sección de controles

Aunque el frontmatter declara 0.7.0, la respuesta todavía recomienda fijar `typesafe-sdk==0.1.0`. Esto contradice el contrato técnico adoptado por el propio corpus.

**Corrección exigida:** cambiar la fijación a la versión comprobada y ejecutar una búsqueda global limitada al corpus activo, excluyendo el histórico inmutable.

## 4. Evaluación de calidad

Los denominadores corresponden al inventario auditado; `0/N` significaría ausencia de defectos observados, no revisión semántica total.

### Calidad del entregable

| Categoría | Defectos observados | Evaluación |
|---|---:|---|
| Completitud y utilidad | 4/6 | Existen las 384 respuestas, síntesis, seguimiento y snapshot, pero faltan evidencia reproducible de NotebookLM, un verificador fiel, contratos ejecutables y una evaluación honesta. |
| Claridad analítica | 3/10 | La estructura es consistente, pero mezcla hechos, hipótesis, objetivos y resultados no observados. |
| Consistencia documental | 4/8 | Hay contradicciones entre informe, validador, rúbricas, manifiesto y respuestas activas. |

### Corrección y robustez

| Categoría | Defectos observados | Evaluación |
|---|---:|---|
| Autoridad y trazabilidad de fuentes | 384/384 | Todos los registros de consulta carecen de respuesta y referencias preservadas; la trazabilidad documental de NotebookLM no puede verificarse. |
| Exactitud del contrato del SDK | 69/384 | Se detectaron llamadas incompatibles con 0.7.0 en 69 respuestas, además del error transversal sobre `max_retries`. |
| Sintaxis y metadatos | 0/384 | YAML y AST pasan las pruebas independientes. |
| Integridad de archivos | 0/384 | Hashes de respuestas y snapshot pasan. |
| Individualización sustantiva | denominador no cerrado | La métrica Jaccard pasa, pero la repetición modular sigue siendo material y contradice el informe. |
| Apoyo de conclusiones | denominador no cerrado | La muestra dirigida encontró varias afirmaciones numéricas o empíricas sin evidencia adecuada; requiere inventario afirmación-fuente completo. |

## 5. Decisión

La segunda remediación **no se acepta**. Los avances estructurales son útiles y deben conservarse, pero B03, B06, B07 y B10 no están resueltos de forma suficiente; B02 y B04 pasan las pruebas independientes; B01 pasa con una discrepancia menor en el nombre del manifiesto.

No debe iniciarse un piloto que dependa del código actual. Sí puede continuarse el diseño de pilotos, siempre que todos los fragmentos se consideren ilustrativos y no ejecutables hasta completar la siguiente remediación y una nueva auditoría externa.

## 6. Criterios mínimos para una nueva presentación

1. Cero argumentos incompatibles con `typesafe-sdk==0.7.0` en las 384 respuestas.
2. Prueba real de instanciación de todos los objetos del SDK sin llamadas de red.
3. `RetryPolicy.max_retries` documentado correctamente.
4. Validador publicado, reproducible y con salida de error ante defectos.
5. Evidencia NotebookLM preservada o estado explícito `consulta_no_verificable`, sin extractos simulados.
6. Cero párrafos sustantivos de plantilla repetidos en series completas de un pilar.
7. Inventario afirmación-fuente con localizador y estado `documentado`, `medido`, `hipótesis` u `objetivo`.
8. Rúbricas recalculadas sobre 25 y sustentadas por resultados verificables.
9. Corrección de `typesafe-sdk==0.1.0` en `JEV-P01-001`.
10. Nueva auditoría externa independiente antes de cambiar cualquier respuesta a `aceptada`.
