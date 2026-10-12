# Company Brain Template

Template abierto para convertir el conocimiento operativo de una empresa en una base compartida para personas, chats y agentes, y para mantenerla al día sin que dependa de la memoria de nadie.

No empezar copiando documentos completos. Primero definir qué es verdad, qué evidencia la respalda, quién puede cambiarla y qué debe bloquearse cuando falte información.

## Qué es

Un company brain es un repositorio pequeño que le dice a una persona o agente:

- Qué hechos de la empresa puede reutilizar.
- Qué claims puede decir hacia afuera.
- Dónde vive la fuente vigente de cada cosa.
- Quién puede aprobar cambios.
- Cuándo debe bloquearse en vez de inventar.

## Qué cambia en la versión 2.0

La versión 1 dejaba un canon bien armado el día del setup. La versión 2 agrega lo que lo mantiene vivo:

| Pieza | Para qué |
| --- | --- |
| Ciclo semanal (`governance/ciclo-semanal.md`) | Una iteración por semana que detecta lo que cambió, lo hace revisar y termina en un PR. |
| Inbox de candidatos (`_inbox/`) | Lugar donde entra todo cambio propuesto antes de ser canon, con fuente y revisor. |
| Agentes (`.claude/agents/`) | `curador`, `frescura`, `evaluador` y `publicador`: los cuatro roles que operan el ciclo. |
| Agenda semanal y copia de lectura | El equipo revisa y lee el canon en la herramienta donde ya trabaja, sin abrir el repositorio. |
| Automatización (`automation/`) | Prompts listos para programar el ciclo semanal y el brief diario. |
| Glosario (`canon/glosario.md`) | Nombres aprobados, deprecados y todavía candidatos. |

## Cómo fluye una semana

```text
fuentes vivas ──> candidatos en _inbox/ ──> agenda semanal ──> PR ──> merge ──> copia de lectura
 (CRM, docs,       (fuente, revisor,        (cada revisor       (solo lo      (owner del   (el equipo lee
  reuniones)        cambio propuesto)        contesta Sí/No)     aprobado)     canon)       lo vigente)
```

Tres reglas sostienen el flujo:

- El silencio no aprueba. Lo no contestado vuelve a la agenda siguiente.
- Un candidato nunca es verdad. Solo lo mergeado en `main` se puede decir, vender o prometer.
- El equipo no abre el repositorio. Contesta donde ya trabaja; solo el owner del canon mergea.

## Arranque

Usar primero el skill `skills/company-setup/SKILL.md`. Funciona como una entrevista guiada: hace las preguntas mínimas para que cualquier empresa arme su propio brain sin copiar documentos completos ni inventar canon.

1. Copiar este repositorio y abrirlo en un agente que pueda leer archivos locales.
2. Pedir: "Usa `skills/company-setup/SKILL.md` para ayudarme a armar el brain de mi empresa".
3. Responder las preguntas por etapas y revisar los cambios propuestos antes de aprobarlos.
4. Ejecutar `python3 scripts/canon_check.py --strict` para validar una primera versión lista para uso.
5. Completar `governance/ciclo-semanal.md` y programar el ciclo con `automation/README.md`.

## Estructura

- `canon/`: verdad reusable para empresa, oferta, claims y glosario.
- `governance/`: owners, decisiones, temas abiertos y ciclo semanal.
- `_inbox/`: candidatos, agenda e informes de cada semana. No es canon.
- `bd/`, `brand/`, `product/`, `regulatory/`: conocimiento funcional con alcance definido.
- `corporate-structure/`: información interna y reglas de publicación.
- `skills/`: instrucciones reutilizables para tareas concretas.
- `.claude/agents/`: los agentes que operan el ciclo semanal.
- `automation/`: prompts para programar el ciclo y el brief diario.
- `templates/`: modelos de candidato y de agenda semanal.
- `evals/`: casos con resultados verificables.
- `source.md`: fuentes vivas que no se copian al repositorio.

## Créditos

El circuito de agentes con inbox y curador se inspira en [spine-agents](https://github.com/ch0rch/spine-agents). Este template le suma gobierno del canon: claims con estado y owner, revisión por ángulo, evaluaciones y verificación automática.

Este template no contiene hechos, precios, clientes, contactos, correos ni fuentes de una empresa real.
