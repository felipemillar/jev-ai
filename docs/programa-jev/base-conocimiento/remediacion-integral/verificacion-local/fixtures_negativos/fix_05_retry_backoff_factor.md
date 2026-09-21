---
id: JEV-NEG-005
pilar: P01
pregunta: "¿Prueba de RetryPolicy con backoff_factor?"
version_respuesta: 2
estado: en_revision
---
# JEV-NEG-005: RetryPolicy backoff_factor

```python
from typesafe_sdk import RetryPolicy
r = RetryPolicy(backoff_factor=1.5)
```
