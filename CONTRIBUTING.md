# Contribuir

Todo cambio factual requiere fuente, owner y fecha de revisión. No incorporar datos personales, correos completos, credenciales ni documentos no redactados.

`canon-check` corre en cada pull request y push a `main`. Verifica fechas de revisión vencidas e IDs duplicados de decisiones.

Antes de usar un brain ya completado en chats, automatizaciones o comunicaciones externas, correr:

```bash
python3 scripts/canon_check.py --strict
```

El modo estricto falla si quedan placeholders `[COMPLETAR]` fuera de este README y si un archivo de canon no declara owner, source y review_due.
