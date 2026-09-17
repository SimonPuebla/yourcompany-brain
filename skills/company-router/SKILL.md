---
name: company-router
description: Rutea un pedido al canon y al skill aplicable antes de responder.
---

# Router

1. Leer `brain.yml` y `AGENTS.md`.
2. Identificar el trabajo y cargar sólo las fuentes necesarias.
3. Elegir un skill especializado o pedir la información mínima necesaria.
4. Si falta una fuente decisiva, devolver `blocked_unverified` con la estructura definida en `AGENTS.md`.
