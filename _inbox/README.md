# Inbox de candidatos

Zona de entrada del canon. Nada de lo que está acá es verdad aprobada: un skill nunca cita un archivo de `_inbox/` como fuente de precio, claim, alcance o disponibilidad.

## Estructura

```text
_inbox/
  AAAA-Www/
    C-AAAA-Www-NN.md        un candidato por archivo
    agenda-weekly.md        copia de las preguntas publicadas en la agenda de la semana
    informe-frescura.md     salida del agente frescura
    informe-evals.md        salida del agente evaluador
```

## Formato de un candidato

El modelo está en `templates/candidato.md`.

```markdown
---
id: C-2026-W01-01
titulo: Una línea que el revisor entienda sin abrir el archivo
clase: B
angulo: comercial
revisor: persona@empresa.com
destino: canon/offering.yml
fuente: https://...
fecha_fuente: 2026-01-05
detectado: 2026-01-05
estado: propuesto
---

## Qué dice el canon
## Qué dice la fuente
## Cambio propuesto
## Qué falta para aprobar
```

- `clase`: `A` o `B`, según `governance/ciclo-semanal.md`.
- `estado`: `propuesto`, `aprobado`, `rechazado`, `aplicado` o `bloqueado`.
- `fuente` y `fecha_fuente` son obligatorias. Sin fuente fechada no hay candidato.
- `revisor` sale de `governance/ciclo-semanal.md`; no se infiere por cargo.

## Reglas

- Resumir la fuente; no copiar correos, transcripts, datos de clientes ni datos personales.
- Un candidato describe una sola diferencia y un solo archivo de destino.
- El cambio propuesto es concreto: qué línea o campo cambia y a qué valor.
- Solo el revisor decide `aprobado` o `rechazado`. El `curador` registra esa respuesta en una sección `## Respuesta del revisor` que cita dónde y cuándo se dio. Sin esa cita el estado no cambia.
- Solo el `curador` pasa un candidato a `aplicado`, en el mismo commit que toca el canon.

`scripts/canon_check.py` valida los campos obligatorios de cada candidato.
