# Contribuir

Todo cambio factual requiere fuente, owner y fecha de revisión. No incorporar datos personales, correos completos, credenciales ni documentos no redactados.

## Cómo entra un cambio

Nadie edita el canon directo. Un cambio entra como candidato en `_inbox/`, lo aprueba el revisor de su ángulo en la agenda semanal y llega al canon en el PR de la semana, que mergea el owner. El detalle está en `governance/ciclo-semanal.md`.

## Verificación

`canon-check` corre en cada pull request y push a `main`. Verifica fechas de revisión vencidas, IDs duplicados de decisiones, claims aprobados sin owner, wording o source, campos obligatorios de cada candidato y rutas locales.

`python3 scripts/canon_check.py --proximos 30` avisa además qué fechas vencen en los próximos 30 días.

Antes de usar un brain ya completado en chats, automatizaciones o comunicaciones externas, correr:

```bash
python3 scripts/canon_check.py --strict
```

El modo estricto falla si quedan placeholders `[COMPLETAR]` fuera de este README y si un archivo de canon no declara owner, source y review_due.
