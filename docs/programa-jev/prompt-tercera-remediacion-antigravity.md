# Prompt para Antigravity — Tercera remediación verificable de Jev AI

Activa tu **modo Goal real** para esta tarea. No simules que está activo: si la interfaz no ofrece un estado Goal verificable, crea una cola persistente, un registro de progreso y un punto de reanudación en disco. No declares el objetivo completado mientras quede un criterio de aceptación incumplido. Ante un bloqueo externo, conserva el Goal como bloqueado con evidencia, termina todo el trabajo independiente y no conviertas el bloqueo en un éxito ficticio.

Trabaja exclusivamente en:

`/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/`

## 1. Documentos que debes leer antes de editar

Lee completos, en este orden:

1. `base-conocimiento/remediacion-integral/auditoria-externa-codex-segunda-remediacion-2026-09-20.md`
2. `prompt-segunda-remediacion-antigravity.md`
3. `mandato-correccion-integral-antigravity.md`
4. `cuestionario-maestro-jev-antigravity.md`
5. `base-conocimiento/remediacion-integral/informe-segunda-remediacion.md`
6. `base-conocimiento/remediacion-integral/seguimiento.csv`
7. `base-conocimiento/remediacion-integral/verificacion-local/test_integrity.py`

La auditoría externa de Codex concluye **NECESITA REVISIÓN — NO ACEPTADA**. Debes resolver completamente C01–C08. No respondas al dictamen repitiendo las métricas de Antigravity ni cambiando umbrales para que el corpus apruebe. Corrige las causas y construye pruebas capaces de detectar los defectos.

## 2. Reglas invariables

- Conserva las 384 respuestas en `estado: en_revision` y `revision_externa: pendiente`.
- No atribuyas aprobación, revisión o aceptación a Codex.
- No modifiques ni elimines snapshots anteriores.
- Antes de editar, crea un nuevo snapshot fechado de todo el estado actual y un manifiesto SHA-256 verificable.
- No publiques, no cambies permisos, no conectes cuentas nuevas y no uses credenciales privadas.
- No llames APIs pagadas de Jev ni ejecutes operaciones reales en QRT, Wheelwork, MT5, ATS, CRM o ERP.
- Puedes instalar temporalmente `typesafe-sdk==0.7.0` para pruebas locales sin red y consultar fuentes públicas oficiales.
- No ejecutes fragmentos del corpus que puedan efectuar red, escritura externa o acciones reales.
- No inventes respuestas de NotebookLM, IDs de conversación, referencias, citas, benchmarks o resultados.
- No modifiques archivos históricos para ocultar errores anteriores. Las correcciones deben aplicarse al corpus activo.
- Si la versión oficial del SDK cambia durante la tarea, registra fecha, versión y commit y actualiza el mandato de forma coherente; no mezcles contratos de versiones diferentes.

## 3. Estrategia obligatoria: prueba que falla, corrección y nueva prueba

Trabaja por fases y registra cada transición en `base-conocimiento/remediacion-integral/continuacion.md`.

Para cada familia de defectos:

1. Añade primero una prueba reproducible que falle con el estado actual.
2. Conserva la salida inicial como evidencia de línea base.
3. Corrige los archivos afectados.
4. Ejecuta nuevamente la prueba.
5. Registra archivos modificados, conteos antes/después y resultado final.

Una prueba estructural no certifica exactitud semántica. Separa explícitamente:

- integridad y presencia;
- sintaxis;
- compatibilidad con el SDK;
- trazabilidad de evidencia;
- respaldo de afirmaciones;
- revisión semántica;
- revisión externa pendiente.

## 4. Fase A — Reemplazar el validador insuficiente

Reescribe o sustituye `base-conocimiento/remediacion-integral/verificacion-local/test_integrity.py` para que compruebe realmente:

1. Exactamente 384 respuestas y 384 IDs únicos.
2. Correspondencia exacta de ID, pilar y pregunta con `cuestionario-maestro-jev-antigravity.md`.
3. YAML mediante `yaml.safe_load()`, verificando tipos, campos requeridos y estados.
4. Las diez secciones fuera de bloques de código.
5. Hashes de todas las respuestas contra `seguimiento.csv`.
6. Extracción y `ast.parse()` de todos los bloques etiquetados `python`.
7. Inspección AST de los constructores del SDK y de sus argumentos.
8. Instanciación local, sin red, de todos los objetos `Choice`, `Score`, `Noul` y `RetryPolicy` presentes en ejemplos ejecutables.
9. Ausencia de argumentos incompatibles con la versión fijada del SDK.
10. Coherencia de versiones entre YAML, respuestas, síntesis, guía e informes.
11. Evidencia de NotebookLM con salida preservada o bloqueo explícito.
12. IDs de fuente existentes, localizadores y ausencia de fuentes huérfanas.
13. Duplicación exacta y aproximada por sección, excluyendo encabezados y metadatos.
14. Coherencia de rúbricas, denominador `/25` y justificación por dimensión.
15. Conteos reales de respuestas, fuentes, pilotos, síntesis y consultas.

El validador debe terminar con código distinto de cero ante cualquier fallo. Incluye fixtures negativos que demuestren que detecta al menos:

- YAML inválido;
- `Choice(options=...)`;
- `Score(min_score=..., max_score=...)`;
- `Noul(statement=...)`;
- `RetryPolicy(backoff_factor=...)`;
- una consulta sin respuesta ni bloqueo declarado;
- un hash incorrecto;
- un párrafo sustantivo duplicado;
- una rúbrica fuera de rango o sin justificación.

Publica el verificador, sus fixtures y los reportes de línea base y resultado final. No menciones scripts que no estén presentes en el entregable.

## 5. Fase B — Corregir íntegramente el contrato del SDK 0.7.0

Usa como autoridad primaria:

- `https://docs.typesafe.ai/sdk/python/`
- `https://docs.typesafe.ai/primitives/choice`
- `https://docs.typesafe.ai/primitives/score`
- `https://docs.typesafe.ai/primitives/noul`
- `https://docs.typesafe.ai/api`
- `https://github.com/typesafe-ai/typesafe-sdk-python`
- código fuente del paquete instalado `typesafe-sdk==0.7.0`.

Corrige todos los archivos activos, no solo los ejemplos citados por Codex:

- `Choice(options=[...])` debe convertirse en `Choice(criteria={...})`.
- `Score(min_score=..., max_score=...)`, `Score(min_anchor=..., max_anchor=...)` y `Score(anchors=...)` deben convertirse a `Score(criteria=[...])` con niveles ordenados y semánticamente descritos.
- `Noul(statement=...)` debe convertirse en `Noul(instructions=...)`.
- `RetryPolicy(max_retries=...)` es válido en 0.7.0 y debe documentarse correctamente.
- `RetryPolicy(backoff_factor=...)` es inválido y debe desaparecer.
- Conserva `retry=...` en clientes o llamadas donde corresponda.
- `Choice` y `Score` sí pueden devolver `confidence`; `Noul` devuelve `noul` y no posee `confidence` nativo.
- Una medida como `abs(2 * p - 1)` debe rotularse como transformación calculada por el cliente.

La auditoría encontró 69 respuestas con argumentos inválidos. Tu resultado final debe producir:

- cero archivos con argumentos no soportados;
- cero constructores que fallen al instanciarse localmente;
- cero afirmaciones falsas sobre `max_retries`;
- cero referencias activas que recomienden `typesafe-sdk==0.1.0`.

Corrige expresamente `JEV-P01-001`, `JEV-P09-001`, `JEV-P09-002`, `JEV-P11-001`, `JEV-P18-010` y todas las propagaciones en síntesis, guía maestra, glosario e informes.

## 6. Fase C — Reparar la evidencia de NotebookLM con honestidad instrumental

Examina los 384 JSON de `base-conocimiento/remediacion-integral/consultas/`.

Para cada pregunta, consulta el notebook canónico mediante el MCP disponible cuando sea posible y conserva:

- herramienta utilizada;
- fecha y hora real;
- notebook exacto;
- pregunta literal;
- respuesta completa o artefacto bruto equivalente;
- referencias o citas devueltas;
- ID de conversación o llamada, si la herramienta lo expone;
- errores y limitaciones del conector.

Si un campo no es expuesto por la herramienta, usa explícitamente `no_expuesto_por_herramienta`. Si no existe respuesta recuperable, usa `estado_consulta: consulta_no_verificable`, registra el motivo y no fabriques un extracto.

Reglas:

- Un archivo JSON vacío o un resumen como “Verificación individual” no constituye evidencia.
- No reutilices como `extracto_verificable` el texto redactado en la propia respuesta.
- No clasifiques la evidencia como `suficiente_para_el_alcance` cuando la salida primaria no pueda comprobarse.
- Cuando exista evidencia externa oficial suficiente, distingue `verificado_fuente_externa` de `verificado_notebooklm`.
- Los 384 registros deben terminar con evidencia recuperable o con un bloqueo explícito y honesto; no deben quedar campos críticos silenciosamente vacíos.

## 7. Fase D — Eliminar boilerplate sustantivo sin forzar diferencias artificiales

La estructura común de diez secciones puede repetirse. También pueden repetirse nombres de campos y fórmulas normativas breves. No puede repetirse como relleno el contenido sustantivo que responde, explica, valida o recomienda.

Corrige, como mínimo:

- el bloque común de las 24 respuestas X;
- el bloque de arquitectura repetido en las 20 respuestas P17;
- el bloque de desarrollo de productos repetido en las 20 respuestas P18;
- recomendaciones idénticas por series completas;
- tablas de fallos copiadas sin relación específica con la pregunta;
- frases de supuesta evidencia repetidas que no tienen respaldo preservado.

Cuando varias respuestas necesiten el mismo fundamento:

1. mueve el fundamento a un documento común con fuente y alcance;
2. enlázalo desde cada respuesta;
3. explica en cada respuesta solo la consecuencia específica para esa pregunta.

Crea una lista explícita de repeticiones permitidas limitada a encabezados, campos estructurales y fórmulas institucionales breves. Cualquier párrafo sustantivo de 24 palabras o más repetido en tres o más respuestas debe fallar, salvo excepción documentada y justificada. La lista de excepciones no puede utilizarse para legitimar bloques completos de contenido genérico.

## 8. Fase E — Auditar afirmaciones y fuentes

Construye un inventario de afirmaciones materiales con:

- ID de respuesta y sección;
- afirmación atómica;
- clasificación: `documentado`, `medido`, `inferencia`, `hipotesis`, `objetivo_de_piloto` o `no_verificado`;
- fuente y localizador exacto;
- fecha de la fuente;
- alcance real;
- limitaciones;
- estado de validación.

Corrige o reclasifica toda cifra no observada. Como mínimo:

- elimina o respalda la afirmación de P18-010 sobre fracaso comercial en menos de 12 meses;
- reclasifica los porcentajes 99,8 % y 99,5 % de P11-001 como objetivos de prueba si no existen resultados;
- corrige la lógica del criterio de latencia de P09-001;
- elimina probabilidades, confianzas y resultados atribuidos a Jev cuando no exista salida preservada;
- no uses fuentes de precios de Groq o documentos de P06 para sostener conclusiones educativas o comerciales no relacionadas;
- separa evidencia del proveedor, evidencia independiente, síntesis interna e hipótesis.

Toda afirmación material sin respaldo debe quedar marcada como hipótesis, objetivo de piloto o no verificada. No puede conservar lenguaje como “la evidencia demuestra” sin evidencia pertinente.

## 9. Fase F — Recalcular las rúbricas

La escala posee cinco dimensiones de 0 a 5 y un total máximo de 25:

- alcance;
- evidencia;
- exactitud;
- utilidad;
- validación.

Para cada una de las 384 respuestas:

- asigna un puntaje individual;
- añade una justificación concreta por dimensión;
- reduce evidencia cuando NotebookLM sea no verificable;
- reduce exactitud ante afirmaciones pendientes;
- reduce validación cuando el ejemplo sea solo ilustrativo o no ejecutado;
- no aumentes puntajes para alcanzar una meta predeterminada.

Sincroniza `seguimiento.csv`, `registro-cuestionario-jev.csv` y los metadatos de cada respuesta. El informe final debe declarar correctamente el rango sobre `/25`.

## 10. Fase G — Propagar correcciones y cerrar sin autoproclamación

Propaga las correcciones a:

- las 384 respuestas;
- `sintesis/P01.md` a `sintesis/P18.md`;
- `sintesis/guia-maestra-de-uso.md`;
- `fuentes.md`;
- `afirmaciones.md`;
- `glosario.md`;
- `lagunas-y-contradicciones.md`;
- `pilotos.md`;
- `seguimiento.csv`;
- `registro-cuestionario-jev.csv`;
- informes de remediación activos.

Actualiza hashes solo después de finalizar todas las ediciones. Ejecuta nuevamente toda la suite y conserva el reporte final.

## 11. Criterios de aceptación obligatorios

No declares el Goal completado hasta que se cumpla todo lo siguiente:

1. 384/384 YAML válidos con parser real.
2. 384 IDs y preguntas coincidentes con el cuestionario maestro.
3. Todos los bloques Python pasan `ast.parse()`.
4. Cero argumentos incompatibles con la versión oficial fijada.
5. Todos los objetos del SDK de los ejemplos se instancian sin red.
6. `RetryPolicy.max_retries` está documentado correctamente.
7. Cero recomendaciones activas de `typesafe-sdk==0.1.0`.
8. Los 384 registros de consulta contienen evidencia preservada o bloqueo explícito, sin campos críticos vacíos presentados como prueba.
9. Cero párrafos sustantivos repetidos fuera de la lista de excepciones permitidas.
10. Toda afirmación material tiene fuente pertinente o clasificación honesta de hipótesis/objetivo/no verificada.
11. Las rúbricas están justificadas individualmente y calculadas sobre 25.
12. Los conteos y documentos derivados son coherentes.
13. Los fixtures negativos hacen fallar el nuevo validador.
14. La suite final termina con código cero únicamente cuando todos los criterios anteriores pasan.
15. Las 384 respuestas continúan en `en_revision` y `revision_externa: pendiente`.

Si algún criterio no puede cumplirse por un bloqueo real de NotebookLM o del MCP, no declares 100 %. Registra el número exacto de elementos bloqueados, completa todo lo demás y mantén el Goal abierto o bloqueado.

## 12. Entregables finales

Entrega:

1. Snapshot previo y manifiesto SHA-256.
2. Corpus corregido de 384 respuestas.
3. Registros de consulta corregidos.
4. Inventario afirmación-fuente.
5. Seguimiento y registro maestro sincronizados.
6. Validador reproducible y fixtures negativos.
7. Reporte de línea base y reporte final.
8. Informe de tercera remediación con conteos exactos.
9. `continuacion.md` con estado, bloqueos y siguiente acción.
10. Lista completa de archivos modificados.

El mensaje de cierre permitido es:

> “Tercera remediación ejecutada y autorrevisada por Antigravity. Las 384 respuestas permanecen en revisión externa pendiente de Codex. Se cumplieron N de 15 criterios; los criterios pendientes y sus evidencias están enumerados en el informe.”

Solo puedes informar 15 de 15 si el reporte reproducible lo demuestra. No solicites ni declares aprobación externa.
