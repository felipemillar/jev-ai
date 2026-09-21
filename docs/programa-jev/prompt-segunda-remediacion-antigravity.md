# Prompt para AntiGravity — Segunda remediación integral de Jev

Activa tu modo Goal real para esta tarea. Si tu entorno no dispone de un modo Goal verificable, no simules su activación: crea y mantén una cola persistente y un punto de reanudación en disco. No des por terminado el objetivo hasta completar todo el trabajo ejecutable, ejecutar las verificaciones finales y dejar visibles los bloqueos que dependan de evidencia no recuperable.

Trabaja exclusivamente en:

`/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/`

Lee completos, antes de modificar archivos y en este orden:

1. `base-conocimiento/remediacion-integral/auditoria-externa-codex-2026-09-20.md`
2. `mandato-correccion-integral-antigravity.md`
3. `cuestionario-maestro-jev-antigravity.md`
4. `base-conocimiento/remediacion-integral/informe-entrega.md`
5. `base-conocimiento/remediacion-integral/seguimiento.csv`

El informe de auditoría externa de Codex contiene un dictamen **NO APROBADO — CAMBIOS REQUERIDOS**. Debes resolver todos los hallazgos B01–B10. No discutas el dictamen mediante la repetición del verificador anterior: corrige los defectos comprobados y construye verificaciones que realmente los detecten.

## Reglas de gobernanza

- Conserva las 384 respuestas en `estado: en_revision` y `revision_externa: pendiente`.
- No marques ninguna respuesta como `resuelta`, `aceptada` o certificada por Codex.
- Tu trabajo sigue siendo una autorrevisión de AntiGravity.
- No atribuyas acciones, resultados, consultas o revisiones a Codex o a una persona sin un registro real.
- No publiques, no cambies permisos, no conectes cuentas nuevas, no uses datos privados, no llames APIs pagadas de Jev y no ejecutes operaciones en QRT, Wheelwork, MT5, CRM, ATS o ERP.
- Puedes consultar los notebooks canónicos mediante el MCP ya autorizado, leer fuentes públicas y ejecutar validaciones locales de documentos y sintaxis.
- No ejecutes los programas incrustados en las respuestas ni código descargado. La validación de ejemplos debe ser estática, sintáctica y contractual.
- No inventes respuestas de NotebookLM, identificadores, referencias, métricas, resultados de ejecución ni evidencia ausente.
- Antes de modificar, crea un nuevo snapshot fechado del estado actual, posterior a la primera remediación, con manifiesto SHA-256. No sobrescribas el histórico anterior.

## Orden obligatorio de corrección

### 1. Reparar el YAML de las 384 respuestas

La línea actual `revisor: pendiente (Codex); autorrevision: Antigravity` invalida todo el frontmatter. Sepárala en campos YAML válidos, por ejemplo:

```yaml
revisor: pendiente
autorrevisor: Antigravity
revision_externa: pendiente
```

Usa un parser YAML real. No basta buscar cadenas. Las 384 respuestas deben parsearse sin errores y conservar tipos coherentes para listas, valores nulos y escalares.

### 2. Verificar y corregir versiones, paquete y firmas del SDK

Los 384 archivos declaran `typesafe_sdk 0.1.0`, pero durante la auditoría externa el repositorio oficial declaraba `typesafe-sdk 0.7.0`. Vuelve a verificar la versión vigente directamente en:

- `https://github.com/typesafe-ai/typesafe-sdk-python`
- `https://docs.typesafe.ai/sdk/python`

Registra versión, fecha, URL y commit o referencia recuperable. No reemplaces ciegamente por 0.7.0 si la versión vigente ha cambiado. Si una respuesta no depende del SDK, evita afirmar una versión innecesaria o marca claramente su alcance.

Revisa todos los ejemplos contra las firmas reales. En particular, corrige los veinte ejemplos de P09:

- `RetryPolicy` usa campos como `backoff_initial`, `backoff_max`, `backoff_jitter` y `timeout`; no `backoff_factor`.
- `AsyncTypeSafeClient` recibe `retry=...`; no `retry_policy=...`.

### 3. Corregir y propagar los contratos de Choice, Score y Noul

Usa como fuentes primarias vigentes:

- `https://docs.typesafe.ai/api`
- `https://docs.typesafe.ai/primitives/choice`
- `https://docs.typesafe.ai/primitives/score`
- `https://docs.typesafe.ai/primitives/noul`
- `https://docs.typesafe.ai/confidence`

Contrato esperado durante la auditoría, que debes volver a comprobar:

- Choice: `type`, `choice`, `probabilities`, `confidence`.
- Score: `type`, `score` numérico que puede caer entre niveles, `legend` como mapa, `probabilities` como mapa, `confidence`.
- Noul: `type`, `noul` entre 0 y 1; sin `confidence` nativo.

Corrige como mínimo y revisa todas sus propagaciones:

- `JEV-P03-001`
- `JEV-P03-012`
- `JEV-P05-001`
- `JEV-P07-006`
- `sintesis/guia-maestra-de-uso.md`
- `remediacion-integral/informe-entrega.md`
- Las 18 síntesis, glosario, afirmaciones, lagunas, pilotos y demás respuestas que reutilicen esos contratos.

Elimina los campos nativos inventados `prediction`, `probability`, `value` y `confidence` cuando se atribuyan a Noul. Una transformación local como `|2p-1|` debe estar rotulada como cálculo del cliente y no como salida o garantía del proveedor.

### 4. Reconstruir realmente P08–P18 y X

Las 244 respuestas todavía comparten bloques completos. No te limites a diferenciar la respuesta directa.

Para cada pregunta reconstruye de manera específica:

- Evidencia y contraste.
- Explicación técnica.
- Ejemplo y contraejemplo.
- Aplicación, solo cuando sea pertinente.
- Fallos y controles.
- Hipótesis y protocolo de validación.

Las secciones deben responder la pregunta individual. No copies una tabla de evidencia, ejemplo o validación común a veinte preguntas. Si existe un fundamento verdaderamente compartido, muévelo a un documento común enlazado y explica en cada respuesta únicamente la consecuencia específica.

Ejecuta detección exacta y aproximada de duplicación por sección, excluyendo código, encabezados, IDs y referencias. Revisa manualmente cada coincidencia alta. Una paráfrasis superficial no es una corrección.

### 5. Reparar la evidencia de NotebookLM

Los 384 JSON actuales no demuestran una respuesta: todos tienen `conversation_id` vacío, `referencias_devueltas: []` y no conservan el texto recibido.

Para cada consulta nueva conserva, cuando el conector lo exponga:

- Herramienta real utilizada.
- Fecha y hora real.
- ID exacto del notebook.
- Pregunta exacta enviada.
- Respuesta original recibida o artefacto bruto equivalente.
- Referencias o citas devueltas.
- Identificador de conversación o llamada.
- Limitaciones y errores del conector.

Si la herramienta no expone un campo, escribe explícitamente `no_expuesto_por_herramienta`; no dejes vacío un campo que luego se presentará como evidencia. Si una respuesta antigua no puede recuperarse, marca la procedencia como pendiente y vuelve a consultar. Si la consulta falla, conserva el error y deja la respuesta parcial; no reconstruyas una respuesta supuestamente recibida.

No uses como `extracto_verificable` una paráfrasis tomada de la propia respuesta redactada. El extracto debe ser recuperable en la evidencia guardada.

### 6. Corregir y rotular el código

- Los veinte bloques Python de P11 deben compilar sintácticamente. Corrige la expresión regular rota y comprueba cada bloque con `ast.parse` después de retirar únicamente la sangría Markdown.
- Revisa las firmas de los veinte ejemplos de P09 contra el SDK oficial vigente.
- Revisa todos los bloques Python restantes mediante análisis sintáctico.
- Si un ejemplo no fue ejecutado, denomínalo `pseudocódigo`, `ejemplo ilustrativo no ejecutado` o `ejemplo estáticamente validado`, según corresponda. No uses “implementación verificada” sin evidencia real.
- No conviertas una validación sintáctica en afirmación de que la integración funciona o que produjo resultados.
- Mantén error masking solo cuando sea pertinente; no copies el mismo bloque `try/except` como relleno en todas las respuestas.

### 7. Rehacer las 384 autoevaluaciones

Está prohibido asignar 4/4 a todas las respuestas y dimensiones.

Para cada respuesta:

- Puntúa individualmente alcance, evidencia, exactitud, utilidad y validación entre 0 y 4.
- Añade una justificación breve y específica por dimensión.
- Una dependencia abierta, evidencia no recuperable, ejemplo no ejecutado o fuente secundaria debe reducir la dimensión correspondiente.
- Mantén separadas autoevaluación y revisión externa.
- Sincroniza `seguimiento.csv` y `registro-cuestionario-jev.csv`.

### 8. Corregir afirmaciones estadísticas y fuentes

Corrige expresamente:

- La afirmación de que 1.000 predicciones de 0,80 producen “exactamente 800” aciertos. Explica expectativa, frecuencia y variación muestral.
- Las atribuciones de ECE 0,12–0,22 a español, textos jurídicos o finanzas chilenas si el estudio citado no evaluó esos dominios.
- La clasificación de fuentes internas como `medido_independiente`.
- Las generalizaciones del ECE 0,024: corresponde a un conjunto y una configuración concretos, no a toda tarea in-domain.
- Cualquier porcentaje de efectividad de nonces, regex o guardrails que no tenga un pasaje verificable.
- TLS, timeouts, latencias y umbrales presentados como obligaciones o garantías sin una fuente contractual.

Para `scienthoon/jev-ood-calibration` y `yodablocks/jev-orderby-bench`, conserva dataset, tamaño, fecha, integración, versión o alias, métrica, cifra exacta y limitaciones. No extrapoles a español chileno, QRT o Wheelwork.

### 9. Corregir inventarios y documentos derivados

- El catálogo actual contiene 120 fuentes, no 134. Calcula el número real después de corregir.
- `pilotos.md` contiene seis pilotos; informa el número real o añade pilotos solo si están completamente definidos y sustentados.
- Reemplaza la URL 404 de `SRC-0039` por la ruta oficial vigente `https://docs.typesafe.ai/api`, si sigue siendo correcta al momento de revisar.
- Trata `SRC-0000` como un centinela sintético fuera del espacio de fuentes reales o reemplázalo por un nombre que no simule una fuente catalogada.
- Propaga toda corrección a las 18 síntesis, guía, pilotos, glosario, afirmaciones, fuentes, lagunas, registros e informes.

### 10. Reemplazar la suite de verificación insuficiente

Amplía `remediacion-integral/verificacion-local/test_integrity.py` o crea un verificador nuevo que compruebe realmente:

1. 384 IDs únicos y correspondencia exacta con el cuestionario.
2. YAML válido mediante parser real y tipos coherentes.
3. Diez secciones fuera de bloques de código.
4. Hashes finales después de terminar las correcciones.
5. Duplicación exacta por sección y similitud aproximada con reporte de coincidencias.
6. Sintaxis de todos los bloques etiquetados `python`.
7. Firmas conocidas del SDK para los ejemplos de P09 y contratos de primitivas.
8. Registros de consulta con respuesta o bloqueo explícito; no solo existencia del JSON.
9. IDs de fuente sin huérfanos y URLs decisivas recuperables.
10. Coherencia entre seguimiento, CSV maestro, YAML y documentos derivados.
11. Conteo real de fuentes, pilotos, respuestas y síntesis.
12. Ausencia de las expresiones contractuales y estadísticas que fueron declaradas incorrectas.

El verificador no puede afirmar que una respuesta es semánticamente correcta por superar controles estructurales. Separa claramente integridad, sintaxis, evidencia y revisión semántica.

## Criterios de cierre obligatorios

No declares la segunda remediación preparada para Codex hasta que:

- Los 384 YAML sean válidos con un parser real.
- Las 384 preguntas coincidan exactamente y no existan IDs duplicados.
- Las 244 respuestas reconstruidas superen detección de duplicación y revisión semántica por sección.
- Los contratos de Choice, Score y Noul sean coherentes en todo el corpus.
- La versión y las firmas del SDK estén verificadas y fechadas.
- Todos los bloques `python` sean sintácticamente válidos.
- No quede código denominado “verificado” sin evidencia de la clase de verificación realizada.
- Los registros de NotebookLM contengan evidencia real o bloqueo explícito, sin campos vacíos presentados como prueba.
- Las rúbricas sean individuales, justificadas y no uniformes.
- Las cifras, benchmarks y fuentes estén acotados al dominio realmente observado.
- Los derivados y sus conteos sean coherentes.
- La suite nueva falle deliberadamente ante fixtures con YAML inválido, duplicación, contrato Noul incorrecto, firma SDK inválida y consulta sin respuesta.
- Los hashes se calculen al final y coincidan.

## Entregables finales

Actualiza o crea:

1. Las 384 respuestas corregidas.
2. `remediacion-integral/seguimiento.csv` con puntuaciones y justificaciones individuales.
3. `registro-cuestionario-jev.csv` sincronizado.
4. `remediacion-integral/consultas/` con evidencia real o bloqueos explícitos.
5. La suite y su reporte reproducible.
6. `remediacion-integral/informe-segunda-remediacion.md`, separando:
   - corregido,
   - verificado estructuralmente,
   - verificado contra fuentes,
   - pendiente empírico,
   - pendiente de revisión externa.
7. `remediacion-integral/continuacion.md` con último lote, siguiente acción y bloqueos.

Al finalizar, no solicites que se dé por aprobada la base. Informa: “Segunda remediación completada y autorrevisada; 384 respuestas permanecen en revisión externa pendiente de Codex”, seguido de los bloqueos reales y la ruta de los reportes.

