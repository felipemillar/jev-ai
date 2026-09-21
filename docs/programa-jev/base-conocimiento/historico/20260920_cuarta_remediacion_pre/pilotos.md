# Cartera Canónica de Pilotos Experimentales — Programa Jev

**Versión:** 2.0.0 (Remediación Integral y Normalización Canónica)  
**Fecha de Emisión:** 2026-09-20  
**Responsable:** Antigravity (Autorrevisión técnica; revisión externa pendiente a cargo de Codex)  
**Estado:** `en_revision` (Propuestas de laboratorio homologadas con diseño experimental falsable, pendientes de validación externa por Codex)  

Este documento reúne las fichas comparables de los proyectos piloto propuestos a lo largo de los 18 pilares para QRT, Wheelwork, productividad personal y nuevos productos de software. Cada piloto define estrictamente su valor esperado, línea base determinista, datos sintéticos de prueba, métricas de éxito, controles de riesgo y condición explícita de abandono.

---

## 1. Cartera de Pilotos QRT (Finanzas Cuantitativas e Investigación)

### Piloto QRT-01: Triaje Semántico de Cables de Noticias con Procedencia Temporal
- **Problema**: Dificultad para filtrar y clasificar en tiempo real miles de cables informativos financieros sin incurrir en costes masivos de modelos generativos de 70B ni saturar a los investigadores.
- **Solución Asistida**: Jev evalúa en un único forward pass la pertinencia respecto al universo de activos (`Choice`) y detecta eventos macroeconómicos binarios (`Noul`).
- **Línea Base**: Búsqueda por palabras clave (expresiones regulares deterministas en CPU).
- **Datos de Prueba**: 5.000 cables financieros sintéticos y públicos históricos con marcas de tiempo UTC inmutables de primera emisión (Point-in-Time).
- **Métrica de Éxito**: Macro-F1 $\ge 0.90$, latencia p95 $< 300$ ms extremo a extremo, coste de tokens $< \$0.25$ USD por 50.000 noticias ($0.042/Mtok).
- **Control de Seguridad**: Salidas confinadas estrictamente a tablas analíticas de investigación; prohibición absoluta de conexión con la capa de ejecución de órdenes en MetaTrader 5 (MT5) o pasarelas FIX.
- **Condición de Abandono**: Si el clasificador no supera a la línea base de palabras clave en al menos 8 puntos porcentuales de F1 o si la tasa de errores de la API supera el 1% en condiciones normales de red.

### Piloto QRT-02: Auditoría Semántica de Citas en Reportes Técnicos Cuantitativos
- **Problema**: Inclusión involuntaria de afirmaciones metodológicas sin respaldo en memorandos de investigación cualitativa.
- **Solución Asistida**: Pipeline que descompone el reporte en proposiciones atómicas y verifica el soporte documental mediante preguntas `Choice` estructuradas en Jev. Los cálculos de t-stat, p-values y Sharpe ratio permanecen estrictamente en Python determinista.
- **Línea Base**: Revisión manual completa por analistas cuantitativos junior.
- **Métrica de Éxito**: Detección de $> 95\%$ de afirmaciones desalineadas en datos de prueba sintéticos.
- **Condición de Abandono**: Tasa de falsos positivos en verificación de citas $> 5\%$.

---

## 2. Cartera de Pilotos Wheelwork (Talento, Selección y Consultoría)

### Piloto WW-01: Mapeo Asistido de Competencias en Descriptores de Cargo y CVs Sintéticos
- **Problema**: Desalineación entre los requisitos indispensables de una vacante y las competencias acreditadas en perfiles laborales heterogéneos.
- **Solución Asistida**: Jev identifica correspondencias conceptuales objetivas (`Choice`), vinculando obligatoriamente cada sugerencia al fragmento textual exacto del currículum.
- **Línea Base**: Coincidencia léxica tradicional de ATS y filtrado booleano por palabras clave.
- **Datos de Prueba**: 1.000 perfiles laborales sintéticos construidos conforme a la normativa de privacidad y protección de datos laborales (Ley 19.628 y estándares AI Act).
- **Gobernanza Ética**: Preprocesamiento en CPU local que redacta nombre, género, edad, fotografía, domicilios y colegios; prohibición absoluta de descarte automático de postulantes sin revisión final de un consultor humano calificado.
- **Métrica de Éxito**: Reducción del $40\%$ en el tiempo de revisión preliminar por consultor; cero discrepancias estadísticas en pruebas contrafactuales pareadas.
- **Condición de Abandono**: Si el modelo penaliza sistemáticamente trayectorias con lagunas temporales o muestra sesgos medibles en pruebas contrafactuales.

### Piloto WW-02: Triaje Semántico de Solicitudes Comerciales B2B
- **Problema**: Demora en el enrutamiento y priorización de solicitudes entrantes de consultoría corporativa.
- **Solución Asistida**: Clasificación rápida de la industria, urgencia y adecuación técnica al catálogo de servicios de Wheelwork.
- **Métrica de Éxito**: Tiempo de enrutamiento $< 2$ minutos con exactitud de despacho $\ge 92\%$.
- **Condición de Abandono**: Tasa de enrutamiento erróneo a especialistas $> 4\%$.

---

## 3. Cartera de Pilotos de Productividad Personal

### Piloto FP-01: Priorización Semántica de Lecturas de Investigación Científica
- **Problema**: Sobrecarga de preprints y literatura científica semanal en IA, matemáticas y finanzas cuantitativas.
- **Solución Asistida**: Clasificador que asigna artículos a categorías temáticas activas y puntúa relevancia (`Score`) respecto a los objetivos estratégicos vigentes. Incluye exploración epsilon-greedy ($\epsilon = 0.15$) para evitar cámaras de eco.
- **Línea Base**: Filtros de palabras clave en lectores RSS.
- **Métrica de Éxito**: Ahorro neto $> 30$ minutos semanales con menos de 1 artículo de frontera omitido por mes.
- **Condición de Abandono**: Si el tiempo dedicado a revisar falsos positivos o supervisar la herramienta excede el tiempo manual ahorrado ($T_{\text{neto}} \le 0$).

---

## 4. Cartera de Nuevos Productos y Servicios SaaS

### Piloto NP-01: Microservicio de Enrutamiento Semántico y Linter Documental
- **Problema**: Sobrecoste masivo al procesar peticiones masivas de triaje o soporte con modelos frontier generativos ($3.00–$15.00/Mtok).
- **Solución Asistida**: Decision Gateway basado en Jev 1.13.0 ($0.042/Mtok) que resuelve solicitudes rutinarias en $< 150$ ms y deriva a frontier models únicamente el $15–20\%$ de casos complejos.
- **Línea Base**: Enrutamiento estático por palabras clave o llamadas indiscriminadas a modelos generativos.
- **Métrica de Éxito**: Ahorro neto superior al $60\%$ en la factura total de computación con una precisión de enrutamiento $\ge 93\%$.
- **Condición de Abandono**: Si la tasa de falsos enrutamientos degrada la satisfacción de usuario o si el coste de supervisión humana supera el ahorro de tokens.
