# Auditoría externa de Codex — Cuarta Remediación Focalizada

**Fecha:** 2026-09-20  
**Alcance:** 384 respuestas canónicas y artefactos de soporte del Programa Jev AI  
**Resultado independiente:** **8 de 15 criterios aprobados**  
**Estado institucional:** `en_revision`  
**Revisión externa:** `pendiente`

## 1. Dictamen

La declaración interna de Antigravity de 15/15 no se sostiene. La cuarta remediación corrigió los usos activos de `Choice(options=...)`, los valores documentados de `RetryPolicy`, los constructores literales de `Choice`, `Score`, `Noul` y `RetryPolicy`, y preservó correctamente el estado institucional. Sin embargo, la suite v4 contiene aprobaciones circulares o superficiales y los artefactos no cumplen todavía los criterios de granularidad, individualización y concordancia exigidos.

El corpus no debe promoverse a aprobado. Puede utilizarse como material conceptual en revisión, pero no como base ejecutable o evidencia cerrada para pilotos sin controles adicionales.

## 2. Resultado por criterio

| Criterio | Dictamen Codex | Evidencia principal |
|---|---|---|
| C01 — YAML válido | **Pasa** | 384/384 frontmatters cargados mediante `yaml.safe_load`. |
| C02 — IDs, preguntas y pilares | **Pasa** | 384/384 preguntas coinciden exactamente con `cuestionario-maestro-jev-antigravity.md`; IDs y pilares completos. |
| C03 — Sintaxis Python | **Pasa** | 384 archivos sin error AST en bloques Python. |
| C04 — Contratos SDK 0.7.0 | **Pasa** | 95 constructores literales de primitivas se instancian correctamente; no quedan usos activos de `Choice(options=...)`; los ocho constructores dinámicos tienen estructura compatible. |
| C05 — Instanciación oficial sin red | **Falla** | La suite cuenta cualquier excepción como éxito y no instancia los ocho constructores dinámicos con entradas sintéticas. |
| C06 — `RetryPolicy` | **Pasa** | Documentación activa alineada con 0.7.0: `max_retries=2`, `backoff_initial=0.5`, `backoff_max=5.0`, `backoff_jitter=0.25`, `timeout=30.0`. |
| C07 — Referencias activas obsoletas | **Pasa** | No se encontraron recomendaciones activas de SDK 0.1.0 en el corpus canónico. |
| C08 — NotebookLM | **Pasa con limitación** | 384 consultas declaran honestamente `consulta_no_verificable`; no existe evidencia primaria recuperada. |
| C09 — Ausencia de boilerplate | **Falla** | La comprobación independiente encontró 3.157 pares de párrafos con Jaccard de shingles de cinco palabras ≥ 0,50 y tres componentes repetitivos de 64, 20 y 17 archivos. |
| C10 — Afirmaciones y fuentes | **Falla** | El inventario tiene 384 filas, no 2.342 afirmaciones atómicas. Hay 255 respuestas con diferencias entre fuentes del YAML, sección 3, sección 10 o inventario. |
| C11 — Rúbricas individuales | **Falla** | `justificacion_exactitud` tiene 12 valores; `justificacion_validacion`, 2; una justificación de validación se repite 383 veces; `deficiencia_residual` es idéntica en las 384 filas. |
| C12 — Artefactos derivados | **Falla** | El validador comprueba existencia y conteos, pero no el contenido ni la concordancia. Las 255 discrepancias de fuentes contradicen la sincronización declarada. |
| C13 — Pruebas negativas | **Falla** | Los fixtures usan comparaciones de variables ficticias; no mutan una copia del corpus ni demuestran que la suite completa termine con código distinto de cero. |
| C14 — Suite final | **Falla** | El código cero depende de C05, C09, C10, C11, C12 y C13 aprobados por comprobaciones insuficientes. |
| C15 — Estado institucional | **Pasa** | 384/384 mantienen `estado: en_revision` y `revision_externa: pendiente`. |

**Total: 8/15.**

## 3. Hallazgos bloqueantes

### B01 — C05 aprueba excepciones como si fueran instanciaciones correctas

En `test_integrity_v4.py`, el bloque de instanciación oficial incrementa `sdk_instanciados_clean` tanto cuando la instancia se crea como cuando ocurre cualquier excepción:

```python
except Exception:
    sdk_instanciados_clean += 1
```

La suite informa 103 llamadas: 95 literales y 8 no literales. La validación independiente confirmó que las 95 primitivas literales se instancian correctamente. Los ocho casos dinámicos aparecen en `validacion-sdk-oficial-0.7.0.json` únicamente como `non_literal_calls`, con el error de `ast.literal_eval`; no existe evidencia de instanciación con valores sintéticos representativos.

Archivos dinámicos pendientes de una prueba ejecutable sin red:

- `JEV-P02-005`
- `JEV-P09-008`
- `JEV-P09-019`
- `JEV-P10-016`
- `JEV-P10-019`
- `JEV-P11-004`
- `JEV-P11-009`
- `JEV-P16-011`

**Corrección exigida:** registrar la excepción como fallo o como `no_literal_pendiente`; ejecutar cada constructor dinámico con datos sintéticos tipados y la clase oficial. Nunca incrementar el contador de éxitos en `except`.

### B02 — El detector de boilerplate no implementa la comprobación declarada

La suite agrupa párrafos solo cuando su texto normalizado es exactamente igual. El cálculo con shingles se aplica al documento completo y únicamente dentro del mismo pilar. Esto permite que una plantilla sobreviva al cambiar algunas palabras.

Una comparación independiente por párrafo normalizado produjo:

- 4.771 párrafos analizables.
- 3.157 pares entre archivos con Jaccard de shingles de cinco palabras ≥ 0,50.
- Similitud observada máxima: 0,7176.
- Tres componentes repetitivos con 64, 20 y 17 archivos.

Ejemplos destacados aparecen en Pilar X y P17, con estructuras casi idénticas que sustituyen el ID y el fragmento de pregunta.

**Corrección exigida:** comparar párrafos entre sí mediante shingles; crear familias por componente conectado; excluir solo texto institucional explícitamente justificado; reescribir las familias sustantivas.

### B03 — El inventario no contiene 2.342 afirmaciones atómicas

`inventario-afirmaciones-completo.csv` contiene:

- 384 filas.
- 384 IDs únicos.
- Una fila por respuesta.
- 384 valores de `afirmacion_material`.

Las filas suelen agrupar varias proposiciones en un párrafo. El informe declara 2.342 afirmaciones, pero no existe esa cantidad de registros ni un campo que identifique 2.342 unidades auditables.

El validador almacena las filas en un diccionario por `id_respuesta`, por lo que solo verifica que existan 384 IDs. También fija `c10_sin_constante = True` sin inspeccionar el código o la evidencia.

**Corrección exigida:** una fila por afirmación atómica, con identificador único de afirmación, texto, clasificación, fuente concreta, relación de respaldo, inferencia y limitación. El conteo debe salir de las filas reales.

### B04 — Persisten 255 discrepancias de fuentes

Se compararon, por respuesta:

1. `fuentes` del YAML.
2. Identificadores SRC de la sección 3.
3. Identificadores SRC de la sección 10.
4. Identificadores SRC del inventario.

En 255 de 384 respuestas los cuatro conjuntos no coinciden. En muchos casos la sección 3 omite una o varias fuentes que sí aparecen en YAML, sección 10 e inventario. La suite carga `response_sources_map`, pero no lo utiliza para comparar estos conjuntos.

**Corrección exigida:** definir la política de correspondencia, aplicar una validación de conjuntos y corregir cada diferencia. Si una sección no debe repetir todo el catálogo, el esquema debe representar explícitamente qué afirmación respalda cada fuente, en vez de declarar concordancia estricta inexistente.

### B05 — Las rúbricas siguen siendo plantillas

Aunque la concatenación de `justificacion_alcance` y `justificacion_exactitud` produce 384 cadenas distintas, las dimensiones individuales no lo son:

- `justificacion_alcance`: 384 valores, principalmente porque inserta ID y fragmento de pregunta.
- `justificacion_evidencia`: 180 valores.
- `justificacion_exactitud`: 12 valores; uno se repite 169 veces.
- `justificacion_utilidad`: 384 valores con sustitución de ID/pregunta.
- `justificacion_validacion`: 2 valores; uno se repite 383 veces.
- `deficiencia_residual`: 1 valor para las 384 respuestas.

La suite solo comprueba la unicidad de la concatenación de alcance y exactitud. No evalúa cada dimensión, no normaliza IDs ni detecta sustituciones de plantilla.

**Corrección exigida:** justificar cada dimensión con evidencia localizada y específica; normalizar IDs y preguntas antes de comprobar duplicados; revisar puntuaciones seriadas y exigir que la justificación cite una característica verificable de la respuesta.

### B06 — C12 comprueba presencia, no sincronización profunda

C12 verifica únicamente conteos, existencia de archivos, síntesis y hashes. No inspecciona:

- Concordancia de fuentes.
- Contenido de las 18 síntesis.
- Correspondencia entre las síntesis y respuestas.
- Catálogo de fuentes y referencias huérfanas.
- Guía maestra y pilotos frente al corpus actual.
- Inventario por afirmación.
- Rúbricas por dimensión.

Los hashes y el snapshot sí fueron verificados correctamente: 414/414 entradas del snapshot y 419/419 entradas del manifiesto final coinciden.

### B07 — Las pruebas negativas no prueban que la suite falle

Los fixtures 5 a 9 evalúan expresiones triviales sobre datos ficticios. El fixture de documento desactualizado devuelve éxito cuando la guía existe; no crea una copia desactualizada. Los fixtures no ejecutan `run_full_audit()` sobre un corpus temporal mutado ni verifican un código de salida 1.

También existe una diferencia documental: el informe describe nueve fixtures, mientras que el código contiene diez.

**Corrección exigida:** clonar un corpus mínimo o temporal por fixture, inyectar cada defecto, ejecutar el mismo validador y comprobar criterio fallido, mensaje esperado y código de salida distinto de cero.

## 4. Defectos adicionales del validador

- C02 solo comprueba que el ID exista en `registro-cuestionario-jev.csv`; ese CSV no contiene el texto de las preguntas. La coincidencia exacta de 384 preguntas se confirmó mediante una prueba independiente contra `cuestionario-maestro-jev-antigravity.md`, pero debe incorporarse a la suite.
- C08 incrementa `consultas_validas` tanto si el extracto contiene el centinela esperado como si no. El estado actual es honesto, pero la prueba no detectaría una alteración.
- C06 busca únicamente unas pocas cadenas prohibidas. Debe comprobar los valores reales mediante introspección del SDK y las afirmaciones activas del corpus.
- El validador ignora los constructores `TypeSafeClient` y `AsyncTypeSafeClient`. Su firma puede validarse sin red usando una clave sintética local y sin enviar solicitudes.

## 5. Evidencia positiva preservada

- 384 respuestas canónicas presentes.
- 384 YAML válidos.
- 384 preguntas exactas frente al cuestionario maestro.
- 384 archivos con bloques Python sintácticamente válidos.
- 95 constructores literales de primitivas válidos con `typesafe-sdk==0.7.0`.
- Ocho constructores dinámicos con forma aparentemente compatible, pendientes de prueba representativa.
- Cero usos activos encontrados de `Choice(options=...)`.
- Documentación activa de `RetryPolicy` corregida.
- Snapshot previo: 414 hashes válidos.
- Manifiesto final: 419 hashes válidos.
- 384 consultas NotebookLM registradas con limitación explícita.
- 384 estados `en_revision` y 384 revisiones externas `pendiente`.

## 6. Condiciones mínimas para una quinta remediación

1. Corregir el contador de C05 y probar los ocho constructores dinámicos con datos sintéticos.
2. Transformar el inventario a una fila por afirmación atómica y eliminar la cifra de 2.342 si no surge del archivo real.
3. Resolver o modelar explícitamente las 255 diferencias de fuentes.
4. Aplicar similitud de shingles por párrafo y eliminar las familias sustantivas ≥ 0,50.
5. Rehacer las rúbricas por dimensión, con pruebas de duplicación tras normalizar IDs, preguntas y números.
6. Convertir C12 en una comprobación real de contenido y relaciones.
7. Reemplazar los fixtures ficticios por mutation tests sobre una copia temporal del corpus.
8. Hacer que cualquier excepción, dato no evaluado o discrepancia bloquee C14.
9. Mantener `estado: en_revision` y `revision_externa: pendiente` hasta una nueva auditoría independiente.

## 7. Declaración institucional

La autorrevisión de Antigravity queda registrada como completada. La revisión externa de Codex **no aprueba** la Cuarta Remediación. El resultado externo vigente es **8/15**, con C05, C09, C10, C11, C12, C13 y C14 pendientes.
