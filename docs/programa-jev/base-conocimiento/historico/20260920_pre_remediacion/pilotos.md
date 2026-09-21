# Cartera Canónica de Pilotos Experimentales — Programa Jev

**Versión:** 1.0.0 (Etapa D)  
**Fecha de Emisión:** 2026-09-20  
**Responsable:** Antigravity (Auditoría Independiente)  
**Estado:** Propuestas de Laboratorio Homologadas (`propuesto_no_ejecutado`)  

Este documento reúne las fichas comparables de los proyectos piloto propuestos a lo largo de los 18 pilares para QRT, Wheelwork, productividad personal y nuevos productos de software. Cada piloto define estrictamente su valor esperado, línea base determinista, datos sintéticos de prueba, métricas de éxito, controles de riesgo y condición explícita de abandono.

---

## 1. Cartera de Pilotos QRT (Finanzas Cuantitativas e Investigación)

### Piloto QRT-01: Triaje Semántico de Cables de Noticias con Procedencia Temporal
- **Problema**: Dificultad para filtrar y clasificar en tiempo real miles de cables informativos financieros sin saturar los modelos deliberativos de alto coste.
- **Solución Asistida**: Jev evalúa en un único forward pass la pertinencia respecto al universo de activos (`Choice`) y detecta eventos macroeconómicos binarios (`Noul`).
- **Línea Base**: Búsqueda por palabras clave (expresiones regulares deterministas).
- **Datos de Prueba**: 5,000 cables financieros sintéticos y públicos históricos con marcas de tiempo UTC inmutables.
- **Métrica de Éxito**: Macro-F1 $\ge 0.90$, latencia p95 $< 35$ ms, coste $< \$1.50$ USD por 10,000 noticias.
- **Control de Seguridad**: Salidas confinadas a tablas analíticas de investigación; prohibida la conexión con la capa de ejecución de órdenes en MetaTrader 5 (MT5).
- **Condición de Abandono**: Si el clasificador no supera a la línea base de palabras clave en al menos 8 puntos porcentuales de F1 o introduce latencia variable $> 100$ ms.

### Piloto QRT-02: Auditoría Semántica de Citas en Reportes Técnicos
- **Problema**: Inclusión involuntaria de afirmaciones sin respaldo empírico en notas metodológicas cuantitativas.
- **Solución Asistida**: Pipeline que descompone el reporte en afirmaciones atómicas y verifica el soporte en el anexo de datos mediante Jev `Noul`.
- **Línea Base**: Revisión manual completa por analistas junior.
- **Métrica de Éxito**: Detección de $> 95\%$ de afirmaciones no soportadas en datos de prueba.
- **Condición de Abandono**: Tasa de falsos positivos en verificación de citas $> 5\%$.

---

## 2. Cartera de Pilotos Wheelwork (Talento, Selección y Consultoría)

### Piloto WW-01: Mapeo Asistido de Competencias en Descriptores de Cargo
- **Problema**: Desalineación entre los requisitos indispensables declarados en una vacante y las competencias acreditadas en perfiles heterogéneos.
- **Solución Asistida**: Jev identifica correspondencias conceptuales (`Choice`) vinculando cada sugerencia al fragmento textual exacto del perfil.
- **Línea Base**: Coincidencia léxica tradicional de ATS.
- **Datos de Prueba**: 1,000 perfiles laborales sintéticos construidos conforme a la normativa chilena de privacidad (Ley 19.628).
- **Gobernanza Ética**: Preprocesamiento que elimina género, edad y origen social; prohibición absoluta de descarte automático sin revisión por consultor humano.
- **Métrica de Éxito**: Reducción del $40\%$ en el tiempo de revisión preliminar por consultor; cero sesgos detectados en pruebas contrafactuales.
- **Condición de Abandono**: Si el modelo penaliza sistemáticamente trayectorias laborales con pausas temporales en pruebas contrafactuales pareadas.

### Piloto WW-02: Triaje Semántico de Solicitudes Comerciales B2B
- **Problema**: Demora en el enrutamiento y priorización de solicitudes entrantes de consultoría corporativa.
- **Solución Asistida**: Clasificación rápida de la industria, urgencia y adecuación al catálogo de servicios de Wheelwork.
- **Métrica de Éxito**: Tiempo de enrutamiento $< 2$ minutos con exactitud de despacho $\ge 92\%$.
- **Condición de Abandono**: Tasa de enrutamiento erróneo a especialistas $> 4\%$.

---

## 3. Cartera de Pilotos de Productividad Personal

### Piloto FP-01: Priorización Semántica de Lecturas de Investigación
- **Problema**: Sobrecarga de preprints y literatura científica semanal en IA y matemáticas.
- **Solución Asistida**: Clasificador que asigna artículos a categorías temáticas activas y puntúa relevancia (`Score`) respecto a la agenda del trimestre.
- **Línea Base**: Filtros de palabras clave en lectores RSS.
- **Métrica de Éxito**: Ahorro neto $> 30$ minutos semanales con menos de 1 artículo crítico omitido por mes.
- **Condición de Abandono**: Si el tiempo dedicado a revisar falsos positivos excede el tiempo de lectura ahorrado.

---

## 4. Cartera de Nuevos Productos

### Piloto NP-01: Linter Semántico y Verificador de Calidad Documental
- **Problema**: Falta de herramientas ligeras para comprobar en tiempo real que los párrafos de una propuesta técnica correspondan con los requisitos del pliego.
- **Solución Asistida**: Microservicio basado en Jev que audita textos en segundo plano durante la edición.
- **Métrica de Éxito**: Respuesta en $< 200$ ms integrada en editores Markdown/IDE.
- **Condición de Abandono**: Coste mensual de inferencia no sostenible para el modelo de tarificación fija.
