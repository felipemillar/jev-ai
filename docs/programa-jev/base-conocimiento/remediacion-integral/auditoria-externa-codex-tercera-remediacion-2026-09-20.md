# Auditoría externa de Codex — Tercera Remediación Jev AI

**Fecha:** 2026-09-20  
**Revisor externo:** Codex  
**Dictamen:** **NECESITA REVISIÓN — 15/15 REFUTADO**  
**Estado exigido:** las 384 respuestas deben continuar en `en_revision` con `revision_externa: pendiente`

## 1. Conclusión

La tercera remediación produjo avances verificables, pero su declaración de 15/15 no está respaldada por el entregable. La suite de Antigravity aprueba mediante validaciones sustitutas, condiciones incompletas y un criterio fijado manualmente en `True`.

La revisión independiente confirma **7 de 15 criterios**. Ocho criterios continúan incumplidos: C04, C05, C06, C09, C10, C11, C12 y C14.

## 2. Controles que pasan independientemente

| Criterio | Resultado | Estado |
|---|---:|---|
| C01 — YAML real | 384/384 con `yaml.safe_load()` | Pasa |
| C02 — IDs, pilares y preguntas | 384/384 coinciden exactamente con el cuestionario maestro | Pasa |
| C03 — Sintaxis Python | 357/357 bloques pasan `ast.parse()` | Pasa |
| C07 — Referencias activas a 0.1.0 | 0 recomendaciones activas | Pasa |
| C08 — Consulta o bloqueo explícito | 384/384 declaran `consulta_no_verificable` | Pasa con limitación: 0 respuestas primarias y 0 referencias preservadas |
| C13 — Fixtures publicados | 9/9 son detectados por la suite | Pasa dentro de su alcance estrecho |
| C15 — Estado institucional | 384/384 permanecen `en_revision` y `pendiente` | Pasa |

También pasan la integridad de los 384 hashes y el snapshot previo de 411 archivos con 411 hashes coincidentes.

## 3. Hallazgos bloqueantes

### T01 — C05 no instancia el SDK oficial

**Severidad:** P0  
**Ubicación:** `verificacion-local/test_integrity.py`, clase `SdkContractValidator`

La suite define una clase propia que solo busca algunos nombres de argumentos. Nunca importa ni instancia `Choice`, `Score`, `Noul` o `RetryPolicy` desde `typesafe-sdk==0.7.0`. Aun así incrementa `sdk_instanciacion_sin_red` y declara 99/99 instanciaciones.

La prueba independiente instaló el paquete oficial 0.7.0 en un directorio temporal y evaluó los constructores literales sin red. Resultado:

- 75 constructores válidos;
- 17 constructores rechazados por el SDK oficial;
- 7 constructores con argumentos no literales que requieren otra estrategia de validación.

Los 17 fallos aparecen en seis respuestas:

- `JEV-P01-013`;
- `JEV-P02-001`;
- `JEV-P02-004`;
- `JEV-P02-006`;
- `JEV-P18-006`;
- `JEV-X-006`.

Las causas incluyen argumentos posicionales que los modelos Pydantic no aceptan y dos objetos `Score` sin `criteria`, que el contrato oficial exige.

**Decisión:** C04 y C05 fallan.

### T02 — Persisten ejemplos contractualmente inválidos fuera de bloques Python

**Severidad:** P1

La suite solo analiza bloques etiquetados `python`. La revisión completa del Markdown encontró diez respuestas activas que todavía muestran `Choice(options=...)` como sintaxis válida:

- `JEV-P01-018`;
- `JEV-P02-003`;
- `JEV-P02-004`;
- `JEV-P02-006`;
- `JEV-P10-011`;
- `JEV-P14-009`;
- `JEV-P14-011`;
- `JEV-P16-013`;
- `JEV-P16-014`;
- `JEV-P18-007`.

La documentación oficial usa `Choice(criteria={...})`, también cuando el ejemplo está dentro de texto corrido.

**Decisión:** C04 falla.

### T03 — `RetryPolicy` continúa documentado con valores falsos

**Severidad:** P0  
**Ubicaciones:** `JEV-P09-002`, `glosario.md` y `JEV-X-010`

El corpus afirma que:

- `backoff_jitter` es booleano o flotante y su valor predeterminado es `True`;
- `timeout` predeterminado es `10.0`;
- la clase está en `typesafe.policy.RetryPolicy` o `typesafe/policy.py`.

El código oficial 0.7.0 define:

- `backoff_jitter: float = 0.25`;
- `timeout: float | None = 30.0`;
- módulo real `typesafe_sdk._core.retry` y exportación pública desde `typesafe_sdk`.

`True` puede pasar accidentalmente la validación numérica de Python porque `bool` hereda de `int`; eso no lo convierte en el tipo ni valor predeterminado documentado.

**Decisión:** C06 falla por documentación materialmente inexacta, aunque `max_retries=2` sí fue corregido.

### T04 — C10 está aprobado mediante una constante y el inventario no cubre el corpus

**Severidad:** P0

La suite contiene literalmente:

`c["C10_afirmaciones_fuentes"] = True`

No calcula cobertura ni correspondencia afirmación-fuente. El archivo `inventario-afirmaciones-fuentes.md` contiene solo 18 filas de respuesta y 18 IDs únicos, frente a 384 respuestas. Su frase “Todas las 384 respuestas han sido auditadas” no está respaldada por un inventario completo.

Además, hay contradicciones activas. En `JEV-P18-010`:

- el YAML repite `SRC-0046` dos veces;
- la sección 3 declara `SRC-0001`, `SRC-0002` y `SRC-0046`;
- la sección 10 conserva `SRC-0010`, `SRC-0046` y `SRC-0095`;
- el informe sostiene que `SRC-0095` fue eliminado.

**Decisión:** C10 y C12 fallan.

### T05 — La detección de boilerplate se evade mediante IDs y pequeñas sustituciones

**Severidad:** P1

El validador compara párrafos exactos. No normaliza IDs, números ni referencias, aunque el mandato exigía evitar diferencias artificiales. Una prueba independiente que normaliza esos elementos encuentra diez familias de párrafos repetidos en tres o más respuestas. Varias se repiten en series de 18 o 20 respuestas.

Ejemplos:

- el mismo párrafo de trazabilidad de NotebookLM en las 20 respuestas de P07;
- bloques de fuentes, cuaderno y trazabilidad repetidos en P09, P10, P11, P12, P13, P14, P15 y P16.

La trazabilidad puede compartir una estructura, pero el informe no puede afirmar “cero boilerplate sustantivo” usando un detector que considera diferente el mismo párrafo por cambiar solo el ID.

**Decisión:** C09 falla.

### T06 — Las rúbricas no son individuales

**Severidad:** P1

Las 384 filas contienen solo ocho justificaciones distintas. Una misma justificación se repite 180 veces. La existencia de texto de más de veinte caracteres no demuestra una evaluación individual por respuesta.

La suite solo comprueba longitud, rango y suma; no comprueba correspondencia entre justificación, respuesta, fuentes, código o bloqueos.

**Decisión:** C11 falla.

### T07 — La suite final puede devolver código cero con defectos materiales

**Severidad:** P0

La suite devuelve 15/15 y código cero pese a:

- 17 constructores rechazados por el SDK oficial;
- diez ejemplos activos con `Choice(options=...)`;
- documentación incorrecta de `RetryPolicy`;
- un inventario que cubre 18 de 384 respuestas;
- contradicciones en documentos derivados;
- rúbricas basadas en ocho plantillas.

También define C12 comprobando solo que existan 384 respuestas y 384 consultas; no inspecciona síntesis, glosario, fuentes ni coherencia derivada.

**Decisión:** C14 falla.

## 4. Limitación documental de NotebookLM

Los 384 JSON declaran correctamente el bloqueo, pero ninguno conserva una respuesta primaria o referencias de NotebookLM:

- respuesta primaria real: 0/384;
- referencias devueltas: 0/384;
- ID de conversación real: 0/384;
- centinela `no_expuesto_por_herramienta`: 384/384.

Esto satisface honestidad instrumental, pero la base continúa sin verificación independiente de los cuadernos. Los conocimientos sostenidos únicamente por esos cuadernos deben mantenerse como no verificados o apoyarse en fuentes públicas pertinentes.

## 5. Resultado de los quince criterios

| Criterio | Dictamen Codex |
|---|---|
| C01 | Pasa |
| C02 | Pasa |
| C03 | Pasa |
| C04 | Falla |
| C05 | Falla |
| C06 | Falla |
| C07 | Pasa |
| C08 | Pasa con bloqueo explícito |
| C09 | Falla |
| C10 | Falla |
| C11 | Falla |
| C12 | Falla |
| C13 | Pasa |
| C14 | Falla |
| C15 | Pasa |

**Resultado independiente: 7/15.**

## 6. Correcciones mínimas antes de una cuarta presentación

1. Importar e instanciar el SDK oficial 0.7.0; eliminar la clase sustituta usada como prueba.
2. Corregir los 17 constructores fallidos y validar los siete no literales.
3. Corregir las diez apariciones de `Choice(options=...)` en prosa o pseudocódigo.
4. Documentar `RetryPolicy` con `backoff_jitter=0.25`, `timeout=30.0` y ruta oficial correcta.
5. Generar un inventario afirmación-fuente que cubra las 384 respuestas o limitar explícitamente su alcance sin afirmar cobertura total.
6. Sustituir `C10=True` por una comprobación calculada.
7. Normalizar IDs, números y referencias en la detección de duplicación.
8. Generar justificaciones de rúbrica específicas y comprobables por respuesta.
9. Corregir las fuentes duplicadas y contradictorias de P18-010 y revisar los derivados.
10. Hacer que C12 inspeccione realmente los documentos derivados y que C14 falle ante cualquiera de estos defectos.

La base no está aprobada para ejecución de pilotos con el código actual. Puede seguir utilizándose para diseño conceptual, manteniendo las limitaciones y el estado de revisión externa pendiente.
