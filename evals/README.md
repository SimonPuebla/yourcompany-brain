# Evaluaciones

Cada caso vive en una carpeta con `input.md` y `expected.md`. `expected.md` tiene `## Debe contener` y `## No debe contener`, con ítems verificables uno por línea.

Los casos reales se describen por hechos de negocio anonimizados. No incluir nombres de contacto, cuerpos de correo, direcciones ni datos personales. Un resultado `blocked_unverified` o `KO` vale tanto como un cierre.

Crear al menos:

- Un caso permitido, donde el agente responda usando canon aprobado.
- Un caso bloqueado, donde falte evidencia, owner o autorización.
- Un caso donde el dato sólo exista en un candidato de `_inbox/` y el agente no lo trate como aprobado.

El agente `evaluador` corre todos los casos antes de cada PR semanal.
