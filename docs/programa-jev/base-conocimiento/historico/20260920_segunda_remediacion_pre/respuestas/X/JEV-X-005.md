---
id: JEV-X-005
pilar: X
pregunta: "¿Qué decisiones de arquitectura son comunes a todos los proyectos y cuáles deben permanecer configurables por dominio?"
version_respuesta: 2
estado: en_revision
fecha_consulta: 2026-09-20
fecha_revision: 2026-09-20
autor: Antigravity
revisor: pendiente (Codex); autorrevision: Antigravity
notebooks_consultados:
  - id: "7051ceed-3234-4060-96c5-93e0267212c1"
    titulo: "Radar IA — Índice maestro y síntesis transversal"
    consulta_literal: "¿Qué decisiones de arquitectura son comunes a todos los proyectos y cuáles deben permanecer configurables por dominio?"
    fecha_consulta: 2026-09-20
    extracto_verificable: "La síntesis transversal de Pilar X unifica arquitectura, gobernanza y decisiones operativas para el despliegue riguroso de Jev..."
version_jev: jev-1.13.0
version_api_sdk: "typesafe_sdk 0.1.0 / POST /v1/systemone"
ambitos:
  - arquitectura_transversal
  - gobernanza_global
  - sintesis_estrategica
dependencias:
  - JEV-P01-001
  - JEV-P08-001
  - JEV-P11-001
  - JEV-P13-001
  - JEV-P15-001
  - JEV-P16-001
  - JEV-P17-001
afirmaciones:
  - CLM-0001
  - CLM-0003
  - CLM-0004
fuentes:
  - SRC-0002
  - SRC-0028
  - SRC-0029
  - SRC-0036
  - SRC-0095
nivel_evidencia: suficiente_para_el_alcance
evidencia_global: suficiente_para_el_alcance
dictamen_uso: candidato_a_piloto
---

# JEV-X-005 — Síntesis Transversal, Arquitectura y Gobernanza Integral

## 1. Respuesta directa y decisión que permite tomar
Decisiones comunes vs. configurables: Comunes a todo el ecosistema: control de versiones inmutable (`jev-1.13.0`), enmascaramiento seguro de excepciones (`type(err).__name__`), registro de auditoría con hashes criptográficos y circuito de desconexión por degradación de red. Configurables por dominio: taxonomía de categorías, criterios de evaluación, umbrales de abstención y reglas de enrutamiento a operadores humanos.

## 2. Alcance, términos y supuestos
- **Alcance Transversal:** Marco institucional y arquitectónico que gobierna todos los pilares (P01–P18).
- **Identidad del Proceso:** Autorrevisión rigurosa de Antigravity; las respuestas se mantienen en estado `en_revision` pendientes de la auditoría externa independiente por Codex.
- **Soberanía y Evidencia:** Prevalencia absoluta de contratos verificados y evidencia empírica sobre especulaciones lingüísticas.

## 3. Evidencia y contraste

| Afirmación ID | Tipo de afirmación | Fuente y localizador | Respaldo observado | Límites y advertencias |
|---|---|---|---|---|
| `CLM-0001` | `documentado_proveedor` | `SRC-0002` (Docs: /api & /models) | Especificación oficial de primitivas y tarifas ($0.042/Mtok). | No provee SLA garantizado de latencia ni ZDR sin contrato enterprise. |
| `CLM-0003` | `medido_independiente` | `SRC-0028` (scienthoon/jev-ood) | Calibración empírica y degradación fuera de dominio. | Exige pruebas de calibración locales en cada proyecto. |
| `CLM-0004` | `medido_independiente` | `SRC-0029` (yodablocks/orderby) | Inversiones en ordenamientos por cuantización a 2 decimales. | Prohíbe el uso de probabilidades para rankings continuos finos. |

## 4. Explicación técnica verificable
La plataforma centralizada asegura gobernanza y seguridad sin coartar la flexibilidad semántica requerida por cada línea de negocio.

### Principios Rectores del Ecosistema
1. **Separación de Responsabilidades:** Contrato de salida (API) != Política de decisión (Cliente determinista).
2. **Mínimo Privilegio y Privacidad:** Anonimización local en CPU antes de emitir tráfico de red hacia proveedores externos.
3. **Economía de Escala Disciplinada:** El ahorro de tokens no debe dilapidarse en sobrecostes de revisión humana o supervisión técnica.
4. **Trazabilidad Criptográfica:** Toda decisión conserva su huella SHA-256 de entrada, versión de modelo y metadatos de procedencia.

## 5. Ejemplo trabajado y contraejemplo
- **Arquitectura de Referencia del Decision Gateway en Python:**
```python
import logging
import hashlib
import time
from typesafe_sdk import TypeSafeClient, Choice

logger = logging.getLogger("JEV-X-005")

class DecisionGateway:
    def __init__(self, model_version: str = "jev-1.13.0"):
        self.client = TypeSafeClient(model=model_version)
        
    def procesar_decision(self, texto_entrada: str, pregunta: str, criterios: dict) -> dict:
        start_time = time.perf_counter()
        hash_entrada = hashlib.sha256(texto_entrada.encode("utf-8")).hexdigest()
        try:
            res = self.client.system_one(
                state=texto_entrada[:1500],
                questions={"decision": Choice(instructions=pregunta, criteria=criterios)}
            )
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            ans = res.answers["decision"]
            return {
                "hash_entrada": hash_entrada,
                "decision": ans.choice,
                "confidence": ans.confidence,
                "latencia_ms": round(elapsed_ms, 2),
                "estado": "exito_verificado"
            }
        except Exception as err:
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            logger.error(f"Fallo en DecisionGateway: {type(err).__name__} tras {elapsed_ms:.2f}ms (detalles omitidos por seguridad)")
            return {
                "hash_entrada": hash_entrada,
                "decision": "abstencion_fallback",
                "confidence": 0.0,
                "latencia_ms": round(elapsed_ms, 2),
                "estado": "fallback_operativo"
            }
```
- **Contraejemplo:** Acoplar la lógica de trading o contratación directamente a las llamadas de red sin pasar por un gateway con circuit breaker: provoca fallos catastróficos ante micro-cortes de conexión.

## 6. Aplicación a nuestros desarrollos
- **Gobierno de la Plataforma:** Despliegue de un microservicio centralizado que administra credenciales, cuotas y telemetría de TypeSafe.
- **Auditoría de Cumplimiento:** Registro periódico de métricas de fiabilidad, equidad y ahorro neto en todas las divisiones operativas.

## 7. Fallos, límites y controles
- **Modo de fallo:** Confianza ciega en salidas del modelo sin verificación de procedencia documental.
- **Control:** Auditoría estricta obligatoria y veto de despliegue sin suite de pruebas unitarias y pruebas contrafactuales.

## 8. Validación propuesta
- **Simulación extremo a extremo:** Ejecutar 500 solicitudes cruzadas entre los componentes de QRT, Wheelwork y herramientas personales.
- **Criterio de aceptación:** 100% de las excepciones capturadas de forma segura, cero fugas de PII y latencia p95 < 450 ms.

## 9. Recomendación y pendientes
- **Dictamen:** `en_revision` (autorrevision completada; revision_externa: pendiente a cargo de Codex).
- **Próxima acción:** Publicar la Guía Maestra consolidada y presentar el informe final de remediación para revisión externa.
- **Responsable:** Arquitecto Principal de Soluciones de IA / Tech Lead.

## 10. Fuentes y trazabilidad
- `SRC-0002`: TypeSafe AI Documentation (/introduction, /api, /models).
- `SRC-0028`: scienthoon, *jev-ood-calibration* (2026-09-19).
- `SRC-0029`: yodablocks, *jev-orderby-bench* (2026-09-19).
- `SRC-0036`: TypeSafe Python SDK Reference.
- `SRC-0095`: CloudZero, *Análisis de costes de inferencia y hardware LPU/GPU* (2026).
- **Registro de consulta NotebookLM:** Cuaderno Pilar X (`7051ceed-3234-4060-96c5-93e0267212c1`), consulta registrada el 2026-09-20, archivo de evidencia: `base-conocimiento/remediacion-integral/consultas/JEV-X-005.json`.
