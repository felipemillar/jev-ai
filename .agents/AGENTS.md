# Reglas y Directrices del Agente — Proyecto Jev AI

Este archivo define las directrices canónicas de comportamiento, arquitectura y seguridad que cualquier agente de IA (Antigravity, Codex o subagentes) debe respetar estrictamente al operar dentro de este repositorio.

---

## 1. Soberanía Determinista y Rol de Jev
- El software anfitrión (Python/TypeScript) en CPU gobierna de forma absoluta el flujo de control, la persistencia, las invariantes de negocio y los efectos colaterales.
- Jev (`POST /v1/systemone`) actúa exclusivamente como un servicio de juicio semántico ligero y calibrado. **Nunca debe actuar como un agente autónomo desatendido con permisos de mutación o ejecución directa sobre sistemas externos.**

## 2. Regla Obligatoria: Error Masking en Python
Cuando escribas o modifiques manejadores de errores en Python (bloques `except`):
- **SIEMPRE** usar `type(err).__name__` en lugar de `str(err)` para evitar fugas involuntarias de información o tokens sensibles.
- **NUNCA** exponer stack traces o mensajes internos no sanitizados en respuestas o registros de auditoría.
- Incluir obligatoriamente el sufijo descriptivo: `(detalles omitidos por seguridad)`.
- Patrón canónico:
  ```python
  except Exception as err:
      logger.error(f"Error {context}: {type(err).__name__} (detalles omitidos por seguridad)")
      return f"Error de operación: {type(err).__name__}"
  ```

## 3. Asimetría de Riesgo y Veto Operativo
- **Finanzas / Trading (QRT)**: Queda terminantemente prohibido conectar las inferencias de Jev o cualquier modelo a pasarelas de ejecución de órdenes (MT5, TradeStation, FIX). Las clasificaciones semánticas solo pueden alimentar tablas analíticas de investigación o ser supervisadas por un operador humano calificado (HITL).
- **Evaluación de Personas (Wheelwork)**: Toda sugerencia de correspondencia laboral debe ir anclada a fragmentos textuales acreditados. Se prohíbe el descarte autónomo de candidatos sin confirmación humana. Los datos sensibles (PII) deben anonimizarse en local antes de cualquier llamada a la API.

## 4. Mantenimiento Obligatorio de la Bitácora (`BITACORA.md`)
- Al completar un hito lógico, modificación estructural o sesión de trabajo, el agente debe registrar cronológicamente la entrada en `BITACORA.md` respetando el formato estándar (Objetivo, Cambios Realizados, Decisiones y Siguientes Pasos).

## 5. Verificación de Integridad de la Base de Conocimiento
- Antes de dar por concluida cualquier modificación a los expedientes en `docs/programa-jev/base-conocimiento/`, el agente debe ejecutar obligatoriamente la suite de validación:
  ```bash
  python docs/programa-jev/base-conocimiento/remediacion-integral/verificacion-local/test_integrity.py
  ```
- No se aceptarán cambios si no se obtiene el estado `EXITO_15_DE_15` sin defectos críticos.
