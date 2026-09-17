# Company Brain Template

Template abierto para convertir conocimiento operativo de una empresa en una base compartida para personas, chats y agentes.

No empezar copiando documentos completos. Primero definir qué es verdad, qué evidencia la respalda, quién puede cambiarla y qué debe bloquearse cuando falte información.

## Qué es

Un company brain es un repositorio pequeño que le dice a una persona o agente:

- Qué hechos de la empresa puede reutilizar.
- Qué claims puede decir hacia afuera.
- Dónde vive la fuente vigente de cada cosa.
- Quién puede aprobar cambios.
- Cuándo debe bloquearse en vez de inventar.

Este template está diseñado para completarse conversando con un agente. La pieza principal es el setup skill.

## Arranque

Usar primero el skill `skills/company-setup/SKILL.md`. Ese flujo funciona como una entrevista guiada: hace las preguntas mínimas para que cualquier empresa arme su propio brain sin copiar documentos completos ni inventar canon.

Resumen del setup:

1. Renombrar el repositorio y completar `brain.yml`.
2. Reemplazar cada `[COMPLETAR]` por una fuente, decisión u owner real.
3. Definir los límites en `AGENTS.md` antes de instalarlo en un chat corporativo.
4. Cargar sólo claims verificables en `canon/claim-registry.yml`.
5. Registrar conflictos en `governance/decision-log.md` y decisiones cerradas en `governance/decisiones.md`.
6. Crear un caso en `evals/` antes de automatizar un flujo sensible.

## Cómo usarlo con un agente

1. Copiar este repositorio.
2. Abrirlo en Codex, Claude u otro agente que pueda leer archivos locales.
3. Pedir: "Usa `skills/company-setup/SKILL.md` para ayudarme a armar el brain de mi empresa".
4. Responder las preguntas por etapas.
5. Revisar los cambios propuestos antes de aprobarlos.
6. Ejecutar `python3 scripts/canon_check.py --strict` cuando quieras validar una primera versión lista para uso.

## Estructura

- `canon/`: verdad reusable para empresa, oferta y claims.
- `governance/`: owners, decisiones y temas abiertos.
- `bd/`, `brand/`, `product/`, `regulatory/`: conocimiento funcional con alcance definido.
- `corporate-structure/`: información interna y reglas de publicación.
- `skills/`: instrucciones reutilizables para tareas concretas.
- `evals/`: casos con resultados verificables.
- `source.md`: fuentes vivas que no se copian al repositorio.

Este template no contiene hechos, precios, clientes, contactos, correos ni fuentes de una empresa real.
