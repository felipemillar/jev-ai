# Mandato de corrección integral de las 384 respuestas Jev

Fecha: 2026-09-20. Responsable de corrección: Antigravity. Revisión externa posterior: Codex, pendiente de ejecución.

## 1. Objetivo y alcance autorizado

Corregir la base de conocimiento completa: P01–P18 (360 respuestas), X (24 respuestas), 18 síntesis, guía maestra, pilotos, catálogos y registros derivados. Trabaja en `/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/`.

Activa tu mecanismo real de objetivo persistente o goal, si está disponible. Si no existe, no simules su activación: mantén una cola y un punto de reanudación en disco. Continúa con todo el trabajo ejecutable sin pedir permiso al terminar cada lote. No declares completado el objetivo mientras existan respuestas sin corregir o sin comprobar. Un bloqueo real debe quedar visible; persistencia no significa inventar evidencia ni reintentar indefinidamente el mismo fallo.

Este encargo autoriza leer fuentes públicas, consultar los notebooks Jev y corregir documentos locales. No autoriza publicaciones, cambios de permisos, conexiones nuevas de cuentas, uso de credenciales, comunicaciones externas, llamadas de inferencia de pago, benchmarks de Jev ni operaciones en QRT, Wheelwork, CRM, ATS, ERP o sistemas financieros. Puedes usar utilidades locales de análisis documental para validar Markdown, YAML, CSV, enlaces, duplicación y cálculos ilustrativos. No ejecutes los programas incrustados en las respuestas ni código descargado de fuentes.

Lee `cuestionario-maestro-jev-antigravity.md` completo, `especificacion-etapa-a1-remediacion.md`, el inventario y este mandato. Conserva los 384 IDs y las preguntas originales. Para esta remediación, este mandato aclara las discrepancias del encargo A.1; el cuestionario maestro sigue definiendo contenido y rúbrica. Los informes anteriores de aceptación son entregables a revisar, no una autorización para omitir trabajo.

## 2. Hallazgos de partida y límites de la auditoría

Revalida los hallazgos sobre los archivos actuales y registra lo que haya cambiado:

| Hallazgo observado | Alcance y acción |
|---|---|
| Existen los 384 archivos y sus filas CSV, sin IDs de fuente huérfanos | Es integridad del inventario; no demuestra exactitud ni que las preguntas estén respondidas. |
| Las secciones de respuesta directa se repiten literalmente dentro de cada grupo P08–P18 y X | 244 archivos afectados, agrupados en 12 textos de respuesta directa. Deben responder individualmente cada pregunta; cambiar sinónimos o títulos no resuelve el defecto. |
| P08–P13 repiten bloques técnicos, ejemplos y validaciones ajenos a preguntas distintas | Examinar las diez secciones de cada archivo. Reconstruir el contenido que no responde al encargo específico. |
| P03-001, P03-012 y P07-006 atribuyen salidas o confianza incorrectas a Noul; P05-001 niega indebidamente confidence en Choice | Corregir según documentación primaria vigente y propagar a ejemplos, tablas, glosario, síntesis y guía. Buscar variantes en todo el corpus. |
| 120 respuestas P08–P13 repiten 12–25 ms; la guía usa 10–25 ms y un coste fijo por decisión | No presentar esas cifras como contrato general del producto sin fuente que pruebe exactamente su alcance. |
| Las 384 respuestas se autodeclaran resueltas, con evidencia suficiente y candidato a piloto; el autor figura como auditor independiente | Separar autoevaluación y revisión externa real. No copiar calificaciones ni asignar a Codex una revisión que no realizó. |
| P13-002 etiqueta SRC-0095 como TypeSafe Docs | El catálogo identifica SRC-0095 como un artículo de CloudZero sobre precios de Groq. SRC-0010 es DataCamp; SRC-0115 es un cuaderno interno, no Fowler. Auditar identidad y pertinencia de todas las citas, no solo existencia de IDs. |

**Rectificación de la auditoría anterior de Codex:** el conteo de 11 o 15 encabezados en P04-010 y P06-020 incluía encabezados dentro de bloques de código. No se ha demostrado un defecto de estructura por ese conteo. Analizar Markdown respetando bloques delimitados; no eliminar ejemplos válidos para satisfacer una expresión regular incorrecta.

**Otras precisiones:** una aparición de `$0.0002` puede ser un ejemplo sintético o una medición de una tarea concreta. No hacer sustituciones masivas. El rango 70–500 ms procedía del anuncio del proveedor y no es un SLA ni una medición local. Las verificaciones externas anteriores fueron selectivas, no una certificación factual de las 384 respuestas. La inaccesibilidad previa de Safari tampoco demuestra que tu conector MCP esté inaccesible ahora.

## 3. Preservación, estados y orden de trabajo

1. Inventaría archivos, fechas, tamaños y hashes. Preserva una copia fechada de los documentos que modificarás en `base-conocimiento/historico/`, con manifiesto. Excluye ese histórico de las comprobaciones del corpus activo. No borres versiones previas ni sobrescribas cambios concurrentes; relee antes de guardar.
2. Abre `base-conocimiento/remediacion-integral/seguimiento.csv`, con una fila por ID. Campos mínimos: ID, hash inicial, requisitos específicos, defectos, evidencia consultada, acción, estado de corrección, cinco notas de rúbrica, autoevaluador, revisión externa, bloqueo y hash final.
3. Marca las 384 respuestas y el registro principal como `en_revision`, manteniendo las puntuaciones anteriores identificadas como históricas. Retira del corpus activo las afirmaciones de aceptación total mediante notas de rectificación visibles; conserva el original en el histórico. Las calificaciones externas no comprobadas pasan a pendientes, no a cero.
4. Corrige primero contratos y afirmaciones comunes de P01–P07; reconstruye P08–P13, después P14–P18 y finalmente X. Revisa todas las respuestas, incluidas las que parezcan correctas. Cada una requiere un resultado documentado.
5. Trabaja en lotes de hasta cinco preguntas relacionadas. Tras cada lote guarda cambios, evidencia y el próximo ID. El tamaño del lote no permite emitir una respuesta genérica para cinco preguntas.

## 4. Investigación y prueba de pertinencia por pregunta

Antes de escribir, descompón la pregunta exacta en requisitos observables. Registra para cada requisito: respuesta concreta, sección que lo resuelve, evidencia y limitación. Esta matriz debe permitir a un revisor decidir si se contestó todo sin fiarse del título ni de la autoevaluación.

Ejemplos de aceptación específica:

- P13-002 exige componentes del costo total. Debe desglosar inferencia, preparación, infraestructura, desarrollo, revisión humana, errores y mantenimiento, con fórmula, unidades, horizonte y ejemplo sintético sin doble conteo. Una explicación de arquitectura híbrida no basta.
- Una pregunta de API exige campos, tipos, versión, errores y ejemplos sustentados. Si falta documentación, declarar el vacío y usar pseudocódigo rotulado.
- Una pregunta sobre particiones temporales exige fechas de disponibilidad, reglas de corte, revisiones retrospectivas y prevención de fuga; una advertencia genérica de supervisión humana no basta.
- Una pregunta que pida tres pilotos exige tres propuestas distintas y comparables, con problema, baseline, datos, resultado medible y condición de descarte.

Consulta el notebook canónico tomado del cuestionario, sin reconstruir sus IDs de memoria. Descubre las herramientas MCP realmente disponibles y usa acceso de lectura. Guarda por consulta: herramienta, fecha real, ID del notebook, pregunta enviada, respuesta recibida, referencias devueltas y artefacto de evidencia. Si la herramienta expone identificador de llamada o de cita, consérvalo; si no, indícalo sin inventarlo.

Guarda las respuestas originales del conector en `remediacion-integral/consultas/` cuando sea posible. No conviertas el primer párrafo de tu respuesta redactada en un supuesto extracto de NotebookLM. No reconstruyas consultas históricas con fechas pasadas. Si solo tienes metadatos antiguos no corroborados, identifícalos como procedencia pendiente y realiza una consulta nueva.

Abre las fuentes originales de cada afirmación decisiva. NotebookLM y los documentos internos orientan la investigación; sus resúmenes no prueban experimentos ni constituyen corroboraciones independientes. Si el notebook falla, continúa con fuentes originales disponibles y registra qué queda parcial. Una conclusión documentada de falta de información puede ser válida; no lo es inventar la información faltante.

## 5. Evidencia, citas y exactitud

Para cada cita comprueba cuatro relaciones: ID → documento real; documento → pasaje recuperable; pasaje → afirmación; afirmación → conclusión dentro de su alcance. Un enlace que abre no basta. Conserva título, autor, fecha/versión, URL, localizador y fecha de consulta. Respeta límites de reproducción: extractos breves o paráfrasis fieles, con enlace.

Usa los tipos del cuestionario: `documentado_proveedor`, `medido_independiente`, `metodo_general`, `inferencia`, `propuesta`, `no_verificado`, `contradicho`. Documenta equivalencias con etiquetas anteriores como `hipotesis_de_diseno`; no cambies la certeza mediante un mero renombrado. La literatura general sobre calibración no demuestra la arquitectura o entrenamiento interno de Jev.

Verifica expresamente, sin limitar la investigación a estos puntos:

- Primitivas: la documentación revisada indicaba `choice`, `probabilities`, `confidence` para Choice; `score`, `probabilities`, `confidence` para Score; `noul` entre 0 y 1 para Noul. Comprueba la versión actual y distingue API directa, SDK y adaptadores. No inventes `prediction`, `probability` o booleanos como campos nativos ni fórmulas de confidence. Una transformación local debe identificarse como tal.
- Versiones, nombres de paquetes, endpoints, límites de contexto y tasas: comprobarlos directamente. No asumir que `jev-1.13.0`, `POST /v1/systemone` o un paquete determinado son válidos porque aparecen repetidos en el corpus.
- Rendimiento: distinguir tiempo del modelo, transporte, extremo a extremo y percentiles. Conservar fecha, carga, ubicación y método. No convertir una demo en una garantía.
- Coste: el anuncio consultado declaraba USD 0.042 por millón de tokens de entrada y salida gratuita. Verificar la tarifa vigente antes de usarla. Bajo esa tarifa, el componente de entrada es `0.042 × tokens_entrada / 1_000_000`; no incluye automáticamente gateways, reintentos, infraestructura ni trabajo humano. Un valor por decisión exige el tamaño de entrada y supuestos.
- Benchmarks: los repositorios comunitarios citados existen; eso no valida cualquier cifra atribuida a ellos. Comprueba dataset, versión, métrica, tamaño y resultado exacto. No extrapoles soporte en español o finanzas chilenas desde tickets sintéticos de otro dominio.
- Probabilidad: no afirmar que calibración perfecta obliga a exactamente 800 aciertos en cualquier muestra de 1.000 predicciones de 0.8. Hay variación muestral. Para cascadas, usar la regla de probabilidades condicionales; un producto de probabilidades marginales exige supuestos y no es una cota universal bajo dependencia.
- Legislación, contratos y políticas: comprobar jurisdicción, vigencia y artículo que sustente la afirmación. No presentar una recomendación interna o un marco voluntario como obligación legal universal. Si no se puede verificar, dejar revisión especializada pendiente.

Fuentes de entrada para estas comprobaciones, sin presumir que cada página respalda cada afirmación:

- https://docs.typesafe.ai/introduction
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/model-jaggedness/jev-1.13
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://github.com/scienthoon/jev-ood-calibration
- https://github.com/yodablocks/jev-orderby-bench

## 6. Redacción y reconstrucción

Respeta las diez secciones y todos los metadatos del cuestionario maestro, además de `pilar`, `nivel_evidencia` y los campos de seguimiento usados en A.1. Mantén consistentes `evidencia_global` y `nivel_evidencia`; cuando una versión o consulta no esté verificada, dilo explícitamente.

Reconstruye las 244 respuestas P08–P18 y X cuya respuesta directa fue duplicada. Reutiliza solo lo que sea pertinente y verificado; no te limites a variar introducciones. La explicación, evidencia, ejemplo, contraejemplo y prueba de validación deben resolver la pregunta propia. Lleva fundamentos compartidos a documentos enlazados para evitar repetirlos como investigación nueva. No impongas un porcentaje arbitrario de palabras diferentes: la prueba es semántica y debe quedar en la matriz de requisitos.

Revisa P01–P07 completos y corrige la propagación de errores. No cambies masivamente toda aparición de Noul, confidence, precio o latencia sin leer el contexto.

Para QRT, Wheelwork y proyectos futuros, distingue lo confirmado por el usuario de escenarios hipotéticos. No inventes SLA, plataformas, procesos, costos de error ni arquitectura existente. Umbrales como 0.85, 0.80 y 0.65 y decisiones como excluir traducción necesitan justificación y validación; una nota genérica de hipótesis al final no corrige una orden categórica en la introducción.

Rotula salidas y resultados sintéticos en el lugar donde aparecen. No afirmar “Jev respondió” o “medido” si no hay ejecución registrada. Las validaciones documentales requieren un protocolo de comprobación, no necesariamente un experimento ni un piloto.

## 7. Autorrevisión y revisión externa

Evalúa cada respuesta con las cinco dimensiones del cuestionario, 0–4 cada una, y justifica cada puntuación. No copiar notas previas ni calificar todo con 20/20. Una puntuación no compensa citas falsas, contratos inventados o conclusiones que exceden la evidencia.

Tu comprobación se llama `autorrevision`. No te rebautices como auditor independiente. No atribuyas revisiones a Codex, personas u otros agentes sin un registro real.

En esta remediación, una respuesta corregida y autorrevisada queda `en_revision`, con `revision_externa: pendiente`. Una incompleta queda `parcial` o `bloqueada`, con causa, evidencia faltante y siguiente acción. La aceptación externa y el paso a `resuelta` corresponden a una revisión posterior realmente realizada. Entregar 384 archivos corregidos para esa revisión es un hito distinto de obtener 384 aceptaciones.

## 8. Comprobaciones finales y entregables

Construye verificaciones locales reproducibles que no ejecuten ejemplos del corpus. Deben comprobar:

1. Los 384 IDs y preguntas coinciden con el cuestionario; no hay ausentes, duplicados o archivos sin seguimiento.
2. YAML válido mediante un analizador real, valores y listas coherentes; no basta encontrar nombres de claves con una expresión regular.
3. Las diez secciones existen fuera de bloques de código. Los títulos dentro de ejemplos no cuentan como secciones del documento.
4. Enlaces relativos resolubles, referencias a fuentes y afirmaciones consistentes, sin fuentes renombradas de forma contradictoria.
5. Duplicación de respuestas directas y de secciones de contenido. Cada coincidencia relevante queda corregida o justificada por escrito; no esquivar el detector parafraseando.
6. Evidencia recuperable para citas decisivas y consultas declaradas. Identificar qué verificó la herramienta y qué comprobaste manualmente.
7. Matriz de requisitos completada para cada pregunta, con criterios de cierre específicos. Ningún requisito desaparece por cambiar de plantilla.
8. Coherencia transversal: propagar correcciones a 18 síntesis, X, guía maestra, pilotos, glosario, afirmaciones, lagunas, CSV y reportes. Conservar las limitaciones en todos los derivados.

Entregables nuevos en `base-conocimiento/remediacion-integral/`:

- `seguimiento.csv`: las 384 decisiones de revisión, requisitos, acciones, evidencia, rúbrica y pendientes externos.
- `consultas/`: registros reales preservados; no transcripciones reconstruidas.
- `verificacion-local/`: comprobaciones y resultados reproducibles, con manifiesto de hashes de los archivos evaluados.
- `informe-entrega.md`: cobertura redactada, corregida, autorrevisada, externamente revisada y aceptada por separado; defectos resueltos, fuentes corregidas, dependencias abiertas y próximo paso.
- `continuacion.md`: último lote guardado, siguiente trabajo, herramientas disponibles y bloqueos; permite reanudar sin repetir ni perder contexto.

La entrega está preparada para revisión externa cuando los 384 IDs tengan una evaluación específica, se hayan corregido los defectos comprobables, exista evidencia real y estén actualizados los derivados. Si falta información necesaria, informa el alcance parcial: no conviertas un bloqueo en aceptación ni declares “100% auditado y aceptado”.

Continúa hasta agotar el trabajo ejecutable. Si se agota el contexto, reanuda desde el registro durable. Si una dependencia exige intervención externa, conserva el objetivo como pendiente y comunica el bloqueo concreto después de avanzar todo lo independiente. Tu cierre debe distinguir claramente lo terminado de lo que aún requiere revisión o evidencia.
