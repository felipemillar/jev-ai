# Reporte de Línea Base de la Tercera Remediación

**Fecha:** 2026-09-20  
**Validador:** `base-conocimiento/remediacion-integral/verificacion-local/test_integrity.py`  
**Dictamen:** `DEFECTOS_DETECTADOS`  
**Criterios de Aceptación Cumplidos:** 7 / 15  
**Defectos Críticos Detectados:** 862  

---

## 1. Tabla de Criterios de Aceptación (Prompt Sección 11)

| Criterio | Descripción | Estado |
|---|---|---|
| C01 | 384/384 YAML válidos con `yaml.safe_load()` | PASÓ |
| C02 | 384 IDs y preguntas coincidentes con cuestionario maestro | PASÓ |
| C03 | Todos los bloques Python pasan `ast.parse()` | PASÓ |
| C04 | Cero argumentos incompatibles con SDK 0.7.0 (`Choice`, `Score`, `Noul`) | FALLÓ (315/384) |
| C05 | Todos los objetos del SDK se instancian sin red | FALLÓ (18/99) |
| C06 | `RetryPolicy.max_retries` documentado correctamente | FALLÓ (383/384) |
| C07 | Cero recomendaciones activas de `typesafe-sdk==0.1.0` | FALLÓ (2 activas) |
| C08 | 384 consultas con evidencia preservada o bloqueo explícito | FALLÓ (0/384) |
| C09 | Cero párrafos sustantivos repetidos fuera de excepciones | FALLÓ (24 párrafos repetidos) |
| C10 | Afirmaciones con fuentes pertinentes o clasificación honesta | PASÓ |
| C11 | Rúbricas justificadas individualmente sobre 25 | FALLÓ (0/384 justificadas) |
| C12 | Conteos y documentos derivados coherentes | PASÓ |
| C13 | Fixtures negativos detectan anomalías | PASÓ |
| C14 | Suite termina con código 0 únicamente si todo pasa | FALLÓ (Defectos pendientes) |
| C15 | 384 respuestas continúan en `en_revision` y `revision_externa: pendiente` | PASÓ |

---

## 2. Fixtures Negativos Ejecutados
- **yaml_invalido_detectado**: DETECTADO CORRECTAMENTE
- **choice_options_detectado**: DETECTADO CORRECTAMENTE
- **score_min_score_detectado**: DETECTADO CORRECTAMENTE
- **noul_statement_detectado**: DETECTADO CORRECTAMENTE
- **retry_backoff_factor_detectado**: DETECTADO CORRECTAMENTE
- **consulta_invalida_detectada**: DETECTADO CORRECTAMENTE
- **hash_incorrecto_detectado**: DETECTADO CORRECTAMENTE
- **parrafo_duplicado_detectado**: DETECTADO CORRECTAMENTE
- **rubrica_invalida_detectada**: DETECTADO CORRECTAMENTE

---

## 3. Muestra de Defectos Detectados (862 totales)
- JEV-P01-001: Recomienda o fija activamente typesafe-sdk==0.1.0
- JEV-P01-001: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-002: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-003: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-004: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-005: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-006: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-007: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-008: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-009: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-010: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-011: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-012: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-013: Llamada incompatible SDK 0.7.0 -> Choice() recibió argumento inválido 'options'. En typesafe-sdk==0.7.0 el contrato exige criteria={...}.
- JEV-P01-013: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-014: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-015: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-016: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-017: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-018: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-019: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P01-020: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P02-001: Llamada incompatible SDK 0.7.0 -> Choice() recibió argumento inválido 'options'. En typesafe-sdk==0.7.0 el contrato exige criteria={...}.
- JEV-P02-001: Llamada incompatible SDK 0.7.0 -> Score() recibió argumentos inválidos ['min_anchor', 'max_anchor']. En typesafe-sdk==0.7.0 el contrato exige criteria=[...].
- JEV-P02-001: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P02-002: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P02-003: Consulta JSON sin evidencia preservada y sin declarar consulta_no_verificable
- JEV-P02-004: Llamada incompatible SDK 0.7.0 -> Choice() recibió argumento inválido 'options'. En typesafe-sdk==0.7.0 el contrato exige criteria={...}.
- JEV-P02-004: Llamada incompatible SDK 0.7.0 -> Choice() recibió argumento inválido 'options'. En typesafe-sdk==0.7.0 el contrato exige criteria={...}.
- JEV-P02-004: Llamada incompatible SDK 0.7.0 -> Score() recibió argumentos inválidos ['min_anchor', 'max_anchor']. En typesafe-sdk==0.7.0 el contrato exige criteria=[...].
