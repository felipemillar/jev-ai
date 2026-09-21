# Auditoría externa de Codex — Remediación integral Jev

**Fecha:** 2026-09-20  
**Revisor externo:** Codex  
**Objeto:** 384 respuestas JEV-P01–P18 y JEV-X, seguimiento, consultas, verificación local y derivados.  
**Dictamen:** **NO APROBADA — CAMBIOS REQUERIDOS**  
**Estado que debe conservarse:** `en_revision`

## 1. Alcance y método

La revisión comprobó el inventario completo, las preguntas, los hashes, el YAML mediante un analizador real, las diez secciones, la duplicación exacta y aproximada, los registros de NotebookLM, los bloques Python mediante análisis sintáctico, las firmas del SDK oficial, los contratos de API y una muestra semántica dirigida a los errores que originaron el mandato.

Se contrastaron los contratos y versiones con las fuentes oficiales vigentes:

- `https://docs.typesafe.ai/introduction/quickstart`
- `https://docs.typesafe.ai/api`
- `https://docs.typesafe.ai/models`
- `https://docs.typesafe.ai/sdk/python`
- `https://github.com/typesafe-ai/typesafe-sdk-python`
- `https://github.com/scienthoon/jev-ood-calibration`
- `https://github.com/yodablocks/jev-orderby-bench`

No se ejecutaron los ejemplos incrustados ni llamadas pagadas a Jev.

## 2. Comprobaciones aprobadas

1. Existen 384 archivos de respuesta y 384 filas de seguimiento.
2. Los 384 IDs y textos de pregunta coinciden con los requisitos registrados.
3. Los 384 archivos cambiaron respecto del histórico y sus hashes finales coinciden con `seguimiento.csv`.
4. Las diez secciones canónicas aparecen fuera de bloques de código en los 384 archivos.
5. El histórico previo se conservó y el registro maestro mantiene `en_revision` y revisión externa pendiente.
6. La identificación del modelo `jev-1.13.0`, el endpoint `POST /v1/systemone`, el precio de USD 0.042/Mtok, el contexto total de 64k y los límites publicados de 250.000 tokens/s y 1.200 solicitudes/min coinciden con la documentación oficial consultada.
7. La respuesta directa fue diferenciada nominalmente para las 384 preguntas.

Estos puntos prueban cobertura e integridad de archivos. No prueban exactitud semántica ni suficiencia de la evidencia.

## 3. Hallazgos bloqueantes

### B01 — Los 384 frontmatters no son YAML válido

Un analizador YAML real rechaza los 384 archivos. La línea común:

```yaml
revisor: pendiente (Codex); autorrevision: Antigravity
```

contiene un segundo `:` en un escalar sin comillas. La verificación de Antigravity solo buscó cadenas y declaró 384/384 válidos sin parsear YAML, en contradicción con el mandato.

**Corrección:** separar campos o citar el valor, y validar los 384 documentos con un parser YAML real.

### B02 — Las 244 respuestas P08–P18 y X siguen basadas en bloques repetidos

Las respuestas directas son distintas, pero el resto del contenido conserva plantillas literales completas:

- P08: la sección 3 es idéntica en 20/20; la sección 6 es idéntica en 20/20; varias secciones 4, 7 y 8 se repiten en grupos de hasta 15.
- P09–P12: las secciones 3, 4, 6, 7 y 8 son idénticas en 20/20 dentro de cada pilar.
- P13: las secciones 3, 6, 7 y 8 son idénticas en 20/20.
- P14–P18: las secciones 3, 6, 7 y 8 son idénticas en 20/20.
- X: las secciones 3, 6, 7 y 8 son idénticas en 24/24.

El análisis de shingles de cinco palabras, excluyendo código e identificadores, produjo similitud media intrapilar de 0,76 en P08; 0,93 en P09; 0,94 en P10; 0,93 en P11; 0,93 en P12; 0,90 en P13; y 0,72–0,79 en P14–P18 y X.

Esto incumple la instrucción de que evidencia, explicación, ejemplo, contraejemplo y validación resuelvan cada pregunta propia. El informe local declara que no existe texto plantilla, pero su script no implementa ningún detector de duplicación.

### B03 — Los registros de NotebookLM no contienen evidencia recuperable

Existen 384 JSON, pero en los 384 casos:

- `conversation_id` está vacío.
- `referencias_devueltas` es una lista vacía.
- No se conserva la respuesta recibida del conector.
- `respuesta_resumen` solo contiene una frase genérica repetida por pilar.

Por ello, los archivos prueban que se registró una pregunta, pero no prueban que NotebookLM la respondiera. Además, 159 extractos de frontmatter presentan más de 85% de cobertura léxica respecto de la respuesta redactada, patrón compatible con el defecto expresamente prohibido de convertir la redacción propia en supuesto extracto verificable.

**Corrección:** conservar respuesta original, referencias, identificador de llamada si existe y limitación explícita si la herramienta no devuelve esos campos. Si no existe evidencia recuperable, marcar la procedencia como no verificada.

### B04 — Persisten errores contractuales que motivaron la remediación

Ejemplos:

- `JEV-P03-001` todavía muestra a Noul con `value`, `probability` y `confidence`, y afirma que entrega booleano más float. La API oficial devuelve `type: "noul"` y `noul: number`.
- `JEV-P03-012` conserva `value = True`, `probability = 0.99`, `confidence = 0.98` para Noul.
- `JEV-P05-001` afirma que Choice solo devuelve `probabilities` y `prediction`; el contrato oficial devuelve `choice`, `probabilities` y `confidence`. También presenta ejemplos de Noul con `prediction` y `probability`.
- `guia-maestra-de-uso.md` y `informe-entrega.md` describen `score` como entero y `legend` como string. La API documenta `score` como número que puede caer entre niveles, `legend` como mapa, `probabilities` como mapa y `confidence` como número.

Las respuestas directas fueron modificadas, pero las tablas, ejemplos, síntesis e informes no recibieron una propagación consistente.

### B05 — La versión del SDK está equivocada en las 384 respuestas

Los 384 archivos declaran:

```text
typesafe_sdk 0.1.0
```

El repositorio oficial vigente declara `typesafe-sdk` versión `0.7.0`. El mandato exigía comprobar directamente versiones y paquetes. Esta discrepancia afecta a todo el corpus.

### B06 — Ejemplos presentados como verificados no son válidos

Se detectaron 339 bloques Python en 338 archivos. Tras eliminar únicamente la sangría de presentación Markdown, 20 bloques de P11 no compilan por una expresión regular con comillas y paréntesis inválidos.

Los 20 ejemplos de P09 usan firmas inexistentes en el SDK 0.7.0:

```python
RetryPolicy(max_retries=3, backoff_factor=1.5)
AsyncTypeSafeClient(..., retry_policy=retry_policy)
```

Las firmas oficiales usan `backoff_initial`, `backoff_max`, `backoff_jitter` y el argumento del cliente se llama `retry`.

P08 etiqueta veinte ejemplos como “Implementación verificada”, aunque el proyecto no tenía el SDK instalado, no había credenciales y el mandato prohibía llamadas de inferencia. Deben denominarse pseudocódigo o ejemplo no ejecutado, salvo evidencia reproducible de validación local compatible con el alcance autorizado.

### B07 — Las 384 rúbricas fueron copiadas como 4/4 en todas las dimensiones

`seguimiento.csv` asigna 4 a alcance, evidencia, exactitud, utilidad y validación para las 384 respuestas. Esto contradice directamente la instrucción “No copiar notas previas ni calificar todo con 20/20”. También contradice las dependencias abiertas y los defectos descritos en este informe.

El CSV maestro conserva 381 respuestas con 20/20 y tres con 19/20, mientras el seguimiento contiene 384×20/20. La autoevaluación no es coherente entre registros.

### B08 — La suite de verificación emite conclusiones que no comprueba

`test_integrity.py`:

- No usa un parser YAML.
- No compara las preguntas con el cuestionario maestro.
- No analiza duplicación, pese a certificar que no existe.
- No comprueba contenido, respuesta o referencias de los JSON de NotebookLM; solo verifica que el archivo exista.
- No analiza sintaxis ni firmas de los bloques Python.
- No comprueba la relación fuente → pasaje → afirmación → conclusión.
- No valida una matriz de requisitos por pregunta.

Por consiguiente, su estado `CORRECTO` solo acredita presencia, encabezados, hashes y algunas cadenas de error masking.

### B09 — Persisten afirmaciones no sustentadas o mal acotadas

Ejemplos comprobados:

- `JEV-P05-001` afirma que 1.000 predicciones de 0,80 deben producir “exactamente 800” aciertos. La calibración es una propiedad de frecuencia/expectativa; una muestra finita tiene variación muestral. El mandato ordenaba corregir expresamente esta frase.
- El mismo archivo atribuye ECE 0,12–0,22 a español, textos jurídicos y finanzas chilenas. El repositorio de scienthoon no midió ese conjunto: evaluó benchmarks públicos y tickets sintéticos, con resultados distintos por tarea y tipo de pregunta.
- `JEV-P03-001` clasifica un cuaderno interno (`SRC-0034`) como `medido_independiente`, aunque `fuentes.md` lo identifica como fuente canónica interna.
- P09 afirma TLS 1.3 obligatorio y timeouts menores de 400 ms sin localizar una garantía contractual del proveedor; el anuncio oficial publica 70–500 ms de extremo a extremo, no un SLA.
- P04 contiene porcentajes de efectividad de delimitadores y regex que no están respaldados por las fuentes citadas.

### B10 — Inconsistencias de inventario derivado

- `informe-entrega.md` declara 134 fuentes; el catálogo contiene 120 IDs/filas `SRC`.
- `pilotos.md` contiene seis pilotos, aunque informes anteriores hablaban de ocho.
- `fuentes.md` conserva `SRC-0039` con `https://docs.typesafe.ai/api-reference/systemone`, que devuelve 404; la ruta oficial vigente es `https://docs.typesafe.ai/api`.
- Se encontró `SRC-0000` en veinte ejemplos de P17 sin entrada en el catálogo. Si es un centinela sintético debe denominarse como tal y quedar fuera del espacio de IDs de fuentes reales.

## 4. Dictamen

La entrega representa una mejora real en preservación histórica, cobertura, estados y diferenciación de las respuestas directas. Sin embargo, no cumple los criterios de aceptación del mandato. Los defectos son sistémicos y afectan estructura YAML, evidencia de NotebookLM, duplicación de contenido, contratos oficiales, versión del SDK, ejemplos de código, rúbricas y coherencia de derivados.

**Decisión:** rechazar la aceptación externa y mantener las 384 respuestas en `en_revision`. No cambiar ninguna a `resuelta` hasta completar una segunda remediación y repetir esta auditoría.

## 5. Orden de corrección requerido

1. Reparar y parsear el YAML de los 384 archivos.
2. Sustituir `typesafe_sdk 0.1.0` por una versión verificada con fecha o marcarla como no fijada; revisar ejemplos contra 0.7.0.
3. Corregir P03-001, P03-012, P05-001, la guía, las síntesis y el informe según los contratos oficiales.
4. Reconstruir las secciones repetidas de P08–P18 y X; cada evidencia, explicación y validación debe responder su pregunta.
5. Corregir o rotular como pseudocódigo los ejemplos; resolver los veinte errores sintácticos de P11 y las firmas inválidas de P09.
6. Rehacer las 384 autoevaluaciones con justificación individual y puntuaciones no uniformes.
7. Sustituir los JSON de consulta por evidencia real recuperable o declarar explícitamente que no pudo preservarse.
8. Corregir afirmaciones estadísticas, cifras no sustentadas, identidad de fuentes y derivados.
9. Ampliar la suite para comprobar YAML real, duplicación, sintaxis, firmas, evidencia y coherencia transversal.
10. Recalcular hashes únicamente después de todas las correcciones.

