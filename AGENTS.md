# Contrato operativo

Este archivo rige todo trabajo con IA en este repositorio. Leer antes de redactar, cotizar, investigar o recomendar una decisión.

## Orden de lectura

1. `brain.yml` y `canon/`.
2. La carpeta funcional aplicable.
3. `governance/owners.md` y `governance/decision-log.md` ante un conflicto.
4. `canon/glosario.md` ante un término que no esté en los archivos anteriores.

## Reglas no negociables

- No inventar hechos, fuentes, artículos, cifras ni resultados.
- No copiar correos completos, contactos, direcciones, credenciales, datos bancarios o documentos sin redactar.
- No presentar una hipótesis, plan o trabajo en curso como una capacidad disponible.
- Todo claim externo requiere owner, source y fecha de revisión.
- Todo dato interno restringido se consulta sólo para el propósito autorizado y nunca se publica sin aprobación.
- Las decisiones abiertas viven en `governance/decision-log.md`; las resueltas, en `governance/decisiones.md`.
- Personalizar voz y contexto está permitido; precios, alcance, disponibilidad, evidencia y condiciones no se personalizan.

## Estados y parada segura

Usar los estados definidos en el canon. Si faltan hechos, evidencia vigente, owner o autorización, devolver exactamente:

```text
blocked_unverified
motivo: <una línea, qué impide continuar>
falta: <lista de hechos, fuentes o confirmaciones concretas que se necesitan>
owner: <email del owner que puede destrabarlo, según governance/owners.md>
cola: <ID de governance/decision-log.md si aplica, si no "ninguna">
siguiente_paso: <la acción mínima que destraba>
```

Un agente que recibe esta salida no continúa la cadena: la propaga con su contexto agregado.

## Skills

Usar un `SKILL.md` de `skills/` cuando el trabajo coincida con su propósito. Ante una tarea ambigua, usar primero `company-router`.

## Ciclo semanal, inbox y agentes

El canon se itera una vez por semana según `governance/ciclo-semanal.md`. Los agentes de `.claude/agents/` (`curador`, `frescura`, `evaluador`, `publicador`) abren el PR semanal; ninguno mergea ni envía mensajes.

- Toda diferencia entre una fuente viva y el canon entra como candidato en `_inbox/`, con el formato de `_inbox/README.md` y un único revisor.
- `_inbox/` no es canon. Nunca citar un candidato como fuente de precio, claim, alcance o disponibilidad; un término marcado `candidato` en el glosario no se usa frente a un cliente.
- Un agente escribe fuera de `_inbox/` sólo para un cambio de clase A o para aplicar un candidato aprobado por su revisor.
- El CRM es la verdad de cuentas y pipeline; la capa de trabajo es trabajo en curso; este repositorio es lo aprobado.

## Cambios al canon

Todo cambio de precio, claim, alcance o disponibilidad necesita fuente, owner y fecha de revisión. El owner del canon definido en `governance/owners.md` es el único que mergea.
