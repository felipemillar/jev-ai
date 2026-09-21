# Auditoría externa de Codex — Quinta remediación del Programa Jev AI

**Fecha:** 2026-09-20  
**Objeto:** determinar si las 384 preguntas del cuestionario canónico están correctamente respondidas y pueden aceptarse como base de conocimiento verificada.  
**Dictamen:** **NO APROBADO**. El corpus está completo y estructuralmente consistente, pero no puede certificarse que las 384 respuestas estén bien respondidas. Sigue siendo una base en revisión.

## 1. Resultado ejecutivo

La quinta remediación resolvió gran parte de la integridad mecánica del corpus:

- existen 384 respuestas para 384 preguntas;
- las preguntas coinciden con el cuestionario maestro;
- los 384 frontmatters YAML son válidos;
- cada respuesta contiene las diez secciones previstas;
- los bloques Python examinados compilan sintácticamente;
- las llamadas activas observadas usan las clases y métodos presentes en `typesafe-sdk==0.7.0`;
- los estados institucionales continúan correctamente como `en_revision` y `revision_externa: pendiente`.

Sin embargo, **completitud documental no equivale a corrección factual**. La trazabilidad de las afirmaciones, la pertinencia de las fuentes y la validación semántica continúan siendo insuficientes. Por ello, ninguna de las 384 respuestas puede declararse todavía plenamente conforme con el contrato de evidencia del cuestionario maestro.

## 2. Evidencia cuantitativa

| Dimensión | Resultado observado | Dictamen |
|---|---:|---|
| Respuestas presentes | 384/384 | Cumple |
| Preguntas alineadas con el maestro | 384/384 | Cumple |
| YAML válido | 384/384 | Cumple |
| Estructura de diez secciones | 384/384 | Cumple |
| Bloques Python con AST válido | 357 bloques | Cumple sintaxis |
| Identificadores de afirmación en inventario | 1.681 únicos | Cumple unicidad |
| Afirmaciones con texto probatorio genérico | 1.681/1.681 | **No cumple trazabilidad** |
| Respuestas con al menos una fuente catalogada para otro pilar | 345/384 | Requiere revisión semántica |
| Referencias cruzadas de pilar detectadas | 934 | Señal de pertinencia deficiente |
| Respuestas con salida primaria preservada de NotebookLM | 0/384 | No verificable instrumentalmente |
| Respuestas bajo la orientación de 500 palabras | 153/384 | Señal de profundidad desigual |

La pertenencia de una fuente a otro pilar no demuestra por sí sola que sea incorrecta. Sí constituye una señal fuerte cuando conjuntos idénticos de fuentes se reutilizan en todas las preguntas de un pilar y varias fuentes no guardan relación material con la pregunta respondida.

## 3. Hallazgos que impiden la aprobación

### H01 — La tabla de evidencia no contiene afirmaciones verificables

Las 1.681 filas del inventario usan variantes de la fórmula:

> “Fundamentación técnica documentada en [título] relativa a [pregunta]”.

Ese texto no identifica una afirmación factual concreta, no reproduce ni parafrasea el pasaje que la sustenta y no proporciona página, sección, encabezado, fragmento o localizador recuperable. La existencia de un identificador de fuente prueba que hubo una asociación documental; no prueba que la fuente respalde el contenido de la respuesta.

Esto contradice el contrato del cuestionario maestro, que exige URL original, metadatos, pasaje o sección, afirmación respaldada, identificadores estables y recuperabilidad de la cita.

### H02 — Hay reutilización sistemática de fuentes con pertinencia insuficiente

Se observaron conjuntos casi fijos para pilares completos:

- P13 reutiliza el mismo conjunto de cuatro fuentes en sus 20 respuestas;
- P14 reutiliza el mismo conjunto de cuatro fuentes en sus 20 respuestas;
- P15 reutiliza el mismo conjunto de cuatro fuentes en sus 20 respuestas;
- P16, P17 y P18 repiten patrones equivalentes con variaciones menores.

Ejemplos materiales incluyen un benchmark de recuperación de información usado como respaldo de flujos personales, un trabajo sobre recuperación correctiva citado para procesos de personas y Wheelwork, y una página de precios de otro proveedor empleada en preguntas de capacidades de producto. Estas referencias pueden aportar contexto lateral, pero no respaldan las conclusiones concretas que se les atribuyen.

### H03 — Persisten afirmaciones incorrectas o no demostradas

Se encontraron, entre otras, las siguientes afirmaciones problemáticas:

- “ausencia total de documentación multilingüe”, aunque la documentación oficial declara soporte para otros idiomas y recomienda pruebas porque el inglés ofrece el mejor rendimiento;
- Noul descrito como “abstención estructurada”, cuando la documentación oficial lo define como una probabilidad continua de que la respuesta sea sí/verdadero;
- inferencia `O(1)`, ausencia de variabilidad estocástica, latencias específicas y reducciones porcentuales de costo presentadas sin medición reproducible ni fuente primaria que las establezca;
- umbrales exactos, valores de calibración y mejoras porcentuales tratados como resultados generales, aunque no existe un experimento local que los sustente.

Las referencias oficiales pertinentes son [TypeSafe Introduction](https://docs.typesafe.ai/introduction), [Python SDK](https://docs.typesafe.ai/sdk/python/), [Models](https://docs.typesafe.ai/models) y [Jev Model Jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13). Esta última, además, documenta límites en lectura literal, matemáticas y números, fechas, indirección, estados grandes, contenido adversarial e invariantes estructurales.

### H04 — Los artefactos derivados no están sincronizados semánticamente

`afirmaciones.md`, `lagunas-y-contradicciones.md`, `pilotos.md` y partes del registro de ejecución conservan contenido anterior a la quinta remediación. Contienen referencias mal asociadas y cifras que no aparecen respaldadas por evidencia primaria. La validación C12 solo cuenta archivos y comprueba hashes de respuestas; no compara el contenido de estos artefactos con las 384 respuestas ni con el inventario de afirmaciones.

### H05 — La respuesta de auditoría interna contiene conclusiones circulares

`JEV-X-024.md` sigue refiriéndose a la “Segunda Remediación Integral”, aunque el ciclo actual es el quinto. También afirma cumplimiento total y plantea como hipótesis que la verificación determinista garantizará cero hallazgos de Codex. Una auditoría no puede usar la ausencia futura de hallazgos como evidencia de su propia corrección. Además, la respuesta evalúa principalmente formato y automatización, no la verdad, utilidad y soporte documental de cada recomendación.

### H06 — Las pruebas automatizadas permiten falsos positivos

La suite `test_integrity_v5.py` y sus auxiliares tienen limitaciones relevantes:

- C06 asigna el resultado aprobado de forma fija después de una búsqueda incompleta;
- C10 comprueba conjuntos de identificadores y conteos, pero no verifica que la fuente respalde la afirmación;
- C11 comprueba que los textos sean distintos, pero no que sean correctos;
- C12 comprueba existencia y conteos, pero no coherencia semántica;
- `run_sdk_audit.py` informa errores sin devolver necesariamente un código de salida fallido;
- las pruebas de mutación prueban funciones auxiliares y cadenas sintéticas, no ejecutan la suite canónica completa contra una copia mutada del corpus;
- varias firmas simuladas por las mutaciones no corresponden al contrato real de SDK 0.7.0.

Por ello, el resultado “15/15” demuestra que el corpus satisface las reglas que la suite decidió medir, pero no que las respuestas estén correctamente fundamentadas.

### H07 — No existe verificación independiente del contenido generado por los cuadernos

Las 384 respuestas registran `consulta_no_verificable`; no se preservó una salida primaria recuperable de NotebookLM para comparar pregunta, fuentes utilizadas y respuesta. Esto impide reconstruir la cadena documental completa y verificar si el texto final conserva fielmente lo que entregó el cuaderno.

## 4. Estado real de la base de conocimiento

| Capacidad | Estado |
|---|---|
| Índice completo de temas y preguntas | Listo |
| Plantilla común para investigación | Lista |
| Ejemplos de integración y SDK | Parcialmente listos; requieren revisión por caso |
| Conocimiento factual verificable | No aprobado |
| Recomendaciones operativas | Hipótesis de trabajo |
| Umbrales, métricas y cifras | No usar sin revalidación |
| Aplicación a QRT y Wheelwork | No validada contra los sistemas reales |
| Base apta para pilotos de bajo riesgo con datos sintéticos | Sí, con revisión humana previa de cada hipótesis usada |
| Base apta para decisiones productivas, financieras o de seguridad | No |

## 5. Correcciones necesarias para una aprobación posterior

1. Reescribir el inventario con **una afirmación atómica real por fila**, su fuente específica y un localizador recuperable.
2. Verificar manualmente cada afirmación crítica contra la fuente original; registrar versión, fecha, alcance y limitaciones.
3. Sustituir las asignaciones de fuentes por pilar por fuentes seleccionadas según cada pregunta.
4. Eliminar o convertir en hipótesis todas las cifras, garantías, umbrales y resultados que no provengan de una medición reproducible.
5. Corregir la interpretación de Noul, paralelismo, latencia, idiomas y límites del modelo según la documentación oficial vigente.
6. Regenerar `afirmaciones.md`, `lagunas-y-contradicciones.md`, `pilotos.md`, las síntesis y la guía maestra desde el corpus corregido.
7. Hacer que las pruebas fallen con código distinto de cero ante errores y ejecutar las mutaciones contra la suite canónica completa.
8. Auditar semánticamente por pilar, con prioridad en P07, P13–P18 y Pilar X.
9. Inspeccionar los flujos y artefactos reales de QRT y Wheelwork antes de convertir sus recomendaciones en diseños aceptados.
10. Mantener `estado: en_revision` y `revision_externa: pendiente` hasta completar estas correcciones y una nueva muestra independiente.

## 6. Decisión

La quinta remediación puede aceptarse como **cierre de completitud estructural**, pero se rechaza como cierre de calidad epistemológica. Las 384 preguntas tienen texto de respuesta; no hay evidencia suficiente para afirmar que las 384 estén bien respondidas.

El corpus puede utilizarse para diseñar pilotos controlados y formular hipótesis. Cada afirmación que afecte arquitectura, costos, seguridad, decisiones financieras o producción debe volver a la fuente primaria y validarse antes de su uso.

No se recomienda iniciar una sexta remediación masiva de las 384 respuestas. El siguiente ciclo debe ser focalizado: corregir primero la documentación maestra y las afirmaciones que se utilizarán en pilotos, seguridad, costos, arquitectura, QRT y Wheelwork. El resto del corpus puede permanecer como material de consulta en revisión hasta que una necesidad concreta justifique su validación.
