# Contrato operativo

## Orden de lectura

1. `brain.yml` y `canon/`.
2. La carpeta funcional aplicable.
3. `governance/owners.md` y `governance/decision-log.md` ante un conflicto.

## Reglas no negociables

- No inventar hechos, fuentes, artículos, cifras ni resultados.
- No copiar correos completos, contactos, direcciones, credenciales, datos bancarios o documentos sin redactar.
- No presentar una hipótesis, plan o trabajo en curso como una capacidad disponible.
- Todo claim externo requiere owner, source y fecha de revisión.
- Todo dato interno restringido se consulta sólo para el propósito autorizado y nunca se publica sin aprobación.
- Las decisiones abiertas viven en `governance/decision-log.md`; las resueltas, en `governance/decisiones.md`.

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
