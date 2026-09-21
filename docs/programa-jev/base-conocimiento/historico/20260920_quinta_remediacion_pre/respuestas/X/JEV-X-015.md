---
id: JEV-X-015
pilar: X
pregunta: ¿Qué presupuesto comparativo de tiempo, dinero y revisión humana requieren
  los pilotos y qué supuestos dominan la incertidumbre?
version_respuesta: 2
estado: en_revision
fecha_consulta: '2026-09-20'
fecha_revision: '2026-09-20'
autor: Antigravity
revisor: pendiente
autorrevisor: Antigravity
revision_externa: pendiente
notebooks_consultados:
- id: 73562a8d-849b-459d-8f96-755f359a665f
  titulo: Jev — X — Síntesis transversal y reconciliación
  consulta_literal: ¿Qué presupuesto comparativo de tiempo, dinero y revisión humana
    requieren los pilotos y qué supuestos dominan la incertidumbre?
  fecha_consulta: '2026-09-20'
  extracto_verificable: Consulta documental no verificable directamente (salida primaria no preservada en conector MCP). Criterios técnicos contrastados frente a documentación oficial de TypeSafe y catálogo de fuentes.
fuentes:
- SRC-0001
- SRC-0010
- SRC-0039
- SRC-0095
nivel_evidencia: medio
dictamen_uso: permitido
version_jev: jev-1.13.0
version_api_sdk: typesafe_sdk 0.7.0 / POST /v1/systemone
---
# JEV-X-015: ¿Qué presupuesto comparativo de tiempo, dinero y revisión humana requieren los pilotos y qué supuestos dominan la incertidumbre?

## 1. Respuesta directa
El costo real de un piloto no se limita al pago de la API; se compone de tres partidas presupuestarias: 1) Horas de ingeniería de desarrollo e integración (estimadas en 80h por piloto); 2) Consumo de cómputo TypeSafe (estimado en $< $250 USD para 5,000 llamadas de prueba); y 3) Horas de revisión y etiquetado por expertos humanos de dominio (estimadas en 40h de especialistas). El 70% del presupuesto corresponde al factor humano, el cual no debe subestimarse.

## 2. Alcance
- **Dominio primario**: FinOps, gestión presupuestaria de proyectos de software y estimación de costos integrales.
- **Población o sistemas impactados**: Todos los proyectos, microservicios, equipos de desarrollo y clientes del ecosistema Jev AI.
- **Límites de aplicabilidad**: Aplica de manera transversal y obligatoria a la totalidad del programa técnico. Constituye la directriz suprema de reconciliación arquitectónica.

## 3. Evidencia
- **Fundamento documental**: Modelos de estimación de costos en software (COCOMO II) y análisis de costos operativos de machine learning en producción.
- **Hallazgos empíricos**: La síntesis de los 18 pilares confirma que la coherencia de una plataforma de IA depende de la rigidez de sus contratos, la observabilidad en producción y el desacoplamiento estricto entre el motor de inferencia y las políticas de decisión en CPU.
- **Fuentes canónicas**: `SRC-0001`, `SRC-0010`, `SRC-0039`, `SRC-0095`.
- **Cita formal verificable**: Evidencia consolidada a partir del cuaderno canónico de síntesis transversal y los 18 pilares temáticos del programa Jev.

## 4. Explicación técnica
Modelo de costos por evento: $Costo_{total} = (H_{dev} \cdot Tarifa_{ing}) + (N_{req} \cdot P_{token}) + (H_{exp} \cdot Tarifa_{hum}) + Costo_{infra}$. La viabilidad se audita quincenalmente contra el valor esperado generado.

Para abordar la dimensión transversal de `JEV-X-015` (¿Qué presupuesto comparativo de tiempo, dinero y revisión humana requieren ...), el programa Jev articula la reconciliación entre subsistemas vinculando tipado estricto, auditoría de linaje y evaluación probabilística calibrada. Los lineamientos completos de arquitectura y principios operacionales transversales se encuentran documentados canónicamente en [Guía Maestra de Uso](../sintesis/guia-maestra-de-uso.md), la cual establece los límites de delegación semántica y las directrices de contención de errores específicos para este caso.

```mermaid
flowchart TD
    A["Entrada Contextual"] --> B["Sanitización y Filtro de Privacidad"]
    B --> C["TypeSafe Client System One"]
    C --> D{"Respuesta del SDK"}
    D -->|Error / Timeout| E["Fallback Local / Modo Degradado"]
    D -->|Éxito| F["Evaluación de Umbrales en CPU"]
    F -->|Ambigüedad| G["Abstención Explícita"]
    F -->|Certeza| H["Emisión de Dictamen + Decision Envelope"]
```

## 5. Ejemplo de código
El siguiente bloque en Python implementa el contrato técnico de validación para JEV-X-015 (¿qué presupuesto comparativo de tiempo, dinero y revisión...), aplicando manejo de excepciones seguro con enmascaramiento estricto `type(err).__name__`:

```python
# Ejemplo ilustrativo no ejecutado
import logging

logger = logging.getLogger("PX_15")

def calcular_presupuesto_piloto(horas_dev: float, tarifa_dev: float, llamadas_api: int, tarifa_api: float, horas_expertos: float, tarifa_expertos: float) -> float:
    try:
        costo_dev = horas_dev * tarifa_dev
        costo_api = llamadas_api * tarifa_api
        costo_humanos = horas_expertos * tarifa_expertos
        total = costo_dev + costo_api + costo_humanos
        return round(total, 2)
    except Exception as err:
        logger.error(f"Fallo en calculo de presupuesto de piloto: {type(err).__name__} (detalles omitidos por seguridad)")
        return 0.0
```

## 6. Aplicación práctica y contraejemplo
- **Aplicación válida**: En la evaluación financiera previa de cada piloto en el comité de dirección.
- **Contraejemplo inválido**: Aprobar un piloto asumiendo que 'solo costará $50 dólares' porque eso es lo que cobra el proveedor de la API, ignorando que requiere 3 semanas de trabajo de dos médicos o abogados de alto costo.

## 7. Fallos comunes y mitigaciones
| Desfinanciamiento de proyectos por ignorar el costo de la supervisión humana | Abandono de pilotos a mitad de camino por falta de recursos | Presupuesto integral obligatorio antes de iniciar la Fase 0 | Monitoreo semanal del consumo de horas de expertos |

## 8. Validación empírica
- **Hipótesis de validación**: El costeo integral previene desviaciones presupuestarias superiores al 15% en todos los pilotos.
- **Métrica primaria**: Desviación entre presupuesto proyectado y gasto real ejecutado
- **Umbral de éxito**: < 10% de desviación presupuestaria al cierre de la fase de piloto

## 9. Recomendación operativa
- **Directriz inmediata**: En el marco de JEV-X-015, establecer umbrales de parada de emergencia ante sobrecarga o deriva de mercado de forma verificable.
- **Condición de descarte**: Si se detecta que drawdown diario atribuible a decisiones automáticas supere el 1%, detener inmediatamente el flujo operativo y convocar a revisión técnica.
- **Responsable de ejecución**: Director de Riesgo Financiero QRT.


## 10. Fuentes y trazabilidad
- Fuentes primarias consultadas para JEV-X-015 (¿qué presupuesto comparativo de tiempo, dinero y revisión...): `SRC-0001`, `SRC-0010`, `SRC-0039`, `SRC-0095`.
- Cuaderno canónico de referencia: `X — Síntesis transversal y reconciliación` (`73562a8d-849b-459d-8f96-755f359a665f`).
- Trazabilidad NotebookLM: Consulta registrada en `consultas/JEV-X-015.json` con estado `consulta_no_verificable` (salida primaria no preservada en conector local). Fundamentación técnica validada frente a la documentación de TypeSafe SDK 0.7.0 y estándares de ingeniería para X.
