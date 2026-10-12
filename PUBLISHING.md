# Publicar tu company brain

Este repositorio puede publicarse como template abierto o usarse como base privada para una empresa.

## Antes de publicar un template abierto

1. Confirmar que no contiene datos de una empresa real.
2. Confirmar que no hay correos, credenciales, clientes, precios, contratos ni fuentes privadas.
3. Mantener placeholders como `[COMPLETAR]` para que otras empresas lo adapten.
4. Incluir una licencia si querés que terceros lo reutilicen con claridad.
5. Confirmar que `_inbox/` no trae candidatos reales y que `governance/ciclo-semanal.md` no trae emails, links ni IDs de una capa de trabajo real.
6. Confirmar que `automation/` no trae rutas, nombres de repositorio ni credenciales.
7. Correr `python3 scripts/canon_check.py`.

## Antes de usar un brain completado

1. Completar `brain.yml`, `canon/`, `source.md` y `governance/owners.md`.
2. Crear al menos una evaluación permitida y una evaluación bloqueada.
3. Confirmar que `AGENTS.md` define cuándo devolver `blocked_unverified`.
4. Completar revisores y referencias en `governance/ciclo-semanal.md`.
5. Correr `python3 scripts/canon_check.py --strict`.
6. Revisar manualmente que no se haya copiado información privada innecesaria.

## Regla práctica

El repositorio puede contener verdad reusable, no archivos fuente completos. Si una persona tendría que pedir permiso para reenviar un documento, correo o transcripción, ese contenido no debería copiarse entero al brain.
