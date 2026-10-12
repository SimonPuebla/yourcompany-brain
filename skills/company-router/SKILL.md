---
name: company-router
description: Rutea un pedido al canon y al skill aplicable antes de responder.
---

# Router

1. Leer `brain.yml` y `AGENTS.md`.
2. Identificar el trabajo y cargar sólo las fuentes necesarias.
3. Elegir un skill especializado o pedir la información mínima necesaria.
4. Si falta una fuente decisiva, devolver `blocked_unverified` con la estructura definida en `AGENTS.md`.

## Ruteo

| Pedido | Skill o agente |
| --- | --- |
| Armar el brain desde el template | `company-setup` |
| Lead, reunión comercial o calificación | `company-discovery` |
| Propuesta, cotización o revisión de propuesta | `company-proposal` |
| Reuniones de hoy, prioridades o brief | `company-daily-brief` |
| "El canon está desactualizado" o "pasá la agenda al PR" | Agente `curador` |
| Qué está vencido o por vencer | Agente `frescura` |

## Regla de seguridad

No cambiar el canon ni enviar mensajes sólo por haberlos preparado. Nada de `_inbox/` se usa como verdad: si el dato pedido sólo existe en un candidato, responder con el canon vigente o con `blocked_unverified` y avisar que hay un cambio en revisión.
