---
name: company-setup
description: Entrevista guiada para que una empresa convierta este template vacio en su propio company brain.
---

# Company Setup

## Proposito

Guiar a una empresa, paso a paso, desde un repositorio vacio hasta una primera version operable de su company brain. Este skill debe hacer preguntas, ordenar respuestas, detectar faltantes y convertir lo validado en canon, fuentes, owners, limites y evaluaciones.

El objetivo no es llenar todo el repositorio. El objetivo es crear una base minima confiable: que el agente sepa que puede decir, que no puede decir, donde verificarlo y quien puede cambiarlo.

## Como usarlo

Actua como facilitador de setup. No asumas que la persona sabe como estructurar un canon. Haz pocas preguntas por vez, espera respuestas, resume lo entendido y propone exactamente que archivos completar.

Cuando una respuesta sea narrativa, separa:

- Hechos verificables.
- Claims comerciales.
- Hipotesis.
- Decisiones pendientes.
- Fuentes necesarias.
- Owners necesarios.

No conviertas una respuesta en canon si falta fuente, owner o alcance.

## Lecturas requeridas

1. `README.md`
2. `brain.yml`
3. `AGENTS.md`
4. `source.md`
5. `governance/owners.md`
6. `canon/company.yml`
7. `canon/offering.yml`
8. `canon/claim-registry.yml`

Leer otros archivos solo cuando el setup toque esa area: `bd/`, `brand/`, `product/`, `regulatory/` o `corporate-structure/`.

## Entrevista de setup

### 1. Identidad de la empresa

Preguntar:

- Como se llama la empresa legalmente?
- Como se presenta comercialmente?
- En una frase verificable, que hace?
- Para quien trabaja?
- En que paises o jurisdicciones opera?
- Quien es owner del canon de empresa?
- Donde esta la fuente primaria de esta informacion?

Actualizar:

- `brain.yml`
- `canon/company.yml`

Bloquear si:

- La empresa no tiene una fuente primaria.
- La frase principal incluye claims no probados.
- No hay owner que pueda aprobar cambios.

### 2. Fuentes vivas

Preguntar:

- Donde vive la verdad comercial?
- Donde vive la verdad de producto o servicio?
- Donde viven precios, paquetes y condiciones?
- Donde viven contratos, politicas legales o compliance?
- Donde viven datos de clientes, soporte o operaciones?
- Que fuentes no deben copiarse completas al repositorio?
- Quien puede autorizar acceso a cada fuente?

Actualizar:

- `source.md`
- `governance/owners.md`

Bloquear si:

- Una fuente es privada y no hay permiso explicito.
- Una decision depende de una fuente que no esta disponible.

### 3. Owners y reglas de cambio

Preguntar:

- Quien aprueba cambios comerciales?
- Quien aprueba cambios de producto o servicio?
- Quien aprueba claims publicos?
- Quien aprueba temas legales, fiscales o regulatorios?
- Que cambios puede hacer un agente sin aprobacion?
- Que cambios siempre requieren aprobacion humana?

Actualizar:

- `governance/owners.md`
- `AGENTS.md`
- `governance/decision-log.md`

Bloquear si:

- Hay un area sensible sin owner.
- El agente podria publicar o prometer algo sin aprobacion clara.

### 4. Oferta y alcance

Preguntar:

- Que productos o servicios existen hoy?
- Que esta disponible, en beta, discontinuado o solo en discovery?
- Que incluye cada oferta?
- Que no incluye?
- Que condiciones cambian por cliente, pais, plan o contrato?
- Donde esta la fuente vigente de precios y alcance?

Actualizar:

- `canon/offering.yml`
- `product/service-matrix.yml`
- `canon/claim-registry.yml` si aparecen claims externos.

Bloquear si:

- El precio o alcance depende de condiciones no documentadas.
- Una oferta no tiene status claro.

### 5. Claims permitidos

Preguntar:

- Que frases puede decir la empresa publicamente?
- Que frases son verdaderas solo bajo condiciones?
- Que frases son internas o no publicables?
- Que claims necesitan fuente externa, legal o regulatoria?
- Que claims estan prohibidos por riesgo, exageracion o falta de evidencia?

Actualizar:

- `canon/claim-registry.yml`
- `brand/voice.md`
- `regulatory/README.md` si corresponde.

Cada claim debe tener:

- `id`
- `status`
- `audience`
- `wording_es`
- `wording_en`
- `conditions`
- `owner`
- `source`
- `review_due`

Bloquear si:

- El claim promete resultados sin evidencia.
- El claim depende de una aprobacion o norma no verificada.
- No queda claro para que audiencia aplica.

### 6. Voz y comunicacion

Preguntar:

- Como debe sonar la empresa?
- Que tono debe evitar?
- Que palabras o promesas estan prohibidas?
- Que ejemplos representan bien la voz?
- Que canales usaran este brain: emails, propuestas, soporte, ventas, documentos internos?

Actualizar:

- `brand/voice.md`
- Skills especializados que usen comunicacion externa.

Bloquear si:

- La voz contradice claims aprobados.
- El canal requiere informacion privada sin permiso.

### 7. Uso comercial

Preguntar solo si la empresa usara el brain para ventas:

- Quienes son los ICPs?
- Que triggers indican oportunidad?
- Que criterios definen una oportunidad calificada?
- Que etapas usa el pipeline?
- Que evidencia minima se necesita antes de avanzar una etapa?
- Que mensajes o promesas no deben usarse en ventas?

Actualizar:

- `bd/icps.md`
- `bd/discovery-playbook.md`
- `bd/pipeline.md`

Bloquear si:

- El ICP es una opinion sin evidencia.
- Una etapa comercial no tiene criterio de entrada y salida.

### 8. Riesgo legal, fiscal o regulatorio

Preguntar solo si aplica:

- Que temas legales, fiscales o regulatorios aparecen en el negocio?
- Que jurisdicciones importan?
- Que fuentes primarias deben usarse?
- Que temas requieren abogado, contador u owner especializado?
- Que debe responder el agente cuando falte verificacion?

Actualizar:

- `regulatory/README.md`
- `governance/owners.md`
- `AGENTS.md`
- `canon/claim-registry.yml` para claims condicionados.

Bloquear si:

- La respuesta podria crear una conclusion legal, fiscal o regulatoria sin fuente primaria y owner autorizado.

### 9. Evaluaciones

Preguntar:

- Dame una pregunta que el agente deberia poder responder con el canon.
- Dame una pregunta que el agente deberia bloquear por falta de evidencia.
- Dame una pregunta donde el agente podria equivocarse por exagerar un claim.

Actualizar:

- `evals/`

Cada evaluacion debe incluir:

- Input.
- Fuentes esperadas.
- Respuesta esperada.
- Condicion de bloqueo si aplica.

## Validacion final

Antes de declarar listo el setup:

1. Ejecutar `scripts/canon_check.py`.
2. Revisar que no queden `[COMPLETAR]` en archivos marcados como listos.
3. Confirmar que cada claim externo tenga fuente, owner, status, audiencia y fecha de revision.
4. Confirmar que `AGENTS.md` diga que hacer cuando falte evidencia.
5. Confirmar que haya al menos una evaluacion de respuesta permitida y una de bloqueo.

## Salida esperada

Al terminar, devolver:

- Version inicial del brain.
- Archivos completados.
- Preguntas respondidas.
- Preguntas pendientes.
- Fuentes vivas registradas.
- Owners faltantes.
- Claims aprobados.
- Claims condicionados o bloqueados.
- Riesgos antes de usarlo en chats, automatizaciones o comunicaciones externas.

## Condiciones de parada

Parar y devolver `blocked_unverified` si falta cualquiera de estos elementos para una decision externa:

- Fuente primaria.
- Owner autorizado.
- Fecha de revision.
- Alcance del claim.
- Permiso para usar informacion privada.

No completes placeholders con supuestos. No transformes documentos largos en canon sin separar hechos, owner, fuente y vigencia.
