# Ciclo semanal del brain

El canon se itera una vez por semana. Cada iteración junta lo que cambió en las fuentes vivas, lo convierte en candidatos, lo hace revisar por la persona que corresponde y termina en un pull request que el owner del canon mergea.

Un brain que no tiene este ciclo se congela: la empresa sigue decidiendo en otras herramientas y el repositorio queda diciendo lo que era verdad el día del setup.

## Rol de cada sistema

| Sistema | Es la verdad de | No es |
| --- | --- | --- |
| CRM: `[COMPLETAR]` | Cuentas, contactos, etapas, owner, actividad y oportunidades. | Fuente de precios, claims o alcance. |
| Capa de trabajo: `[COMPLETAR: wiki, docs o gestor de proyectos]` | Trabajo en curso: estudios, borradores, tableros, notas. | Verdad aprobada. Una página de trabajo es evidencia para un candidato, nunca canon. |
| Este repositorio | Lo aprobado: qué se puede decir, vender, prometer y operar. | Depósito de trabajo en curso ni copia de otra herramienta. |

La información sube en un solo sentido: fuente viva → candidato en `_inbox/` → revisión → canon. Lo aprobado baja en un solo sentido: canon → skills → borradores y copia de lectura.

## Ángulos de revisión

Cada candidato tiene un único revisor. El revisor responde por su ángulo; no aprueba fuera de él. No inferir un ángulo por cargo: se asigna acá.

| Ángulo | Revisor | Carpetas | Fuentes vivas que se barren |
| --- | --- | --- | --- |
| Comercial y canon | `[COMPLETAR: email]` | `canon/`, `bd/`, `brand/`, `governance/` | `[COMPLETAR]` |
| Producto y delivery | `[COMPLETAR: email]` | `product/` | `[COMPLETAR]` |
| Legal, regulatorio o fiscal | `[COMPLETAR: email]` | `regulatory/` | `[COMPLETAR]` |
| Dirección y estrategia | `[COMPLETAR: email]` | `canon/company.yml` | `[COMPLETAR]` |

Agregar o quitar filas según la empresa. Un candidato cuyo ángulo no tiene revisor queda `bloqueado` y se abre en `governance/decision-log.md`.

## Clases de cambio

| Clase | Qué es | Cómo entra |
| --- | --- | --- |
| A | Hecho con fuente externa fechada que no cambia lo que la empresa promete: fecha de revisión, link roto, estado leído de un tablero, etapa del CRM, versión citada. | El agente aplica el cambio en el PR semanal, en un commit separado, con la fuente en el mensaje. |
| B | Precio, claim, alcance, disponibilidad, owner, nomenclatura o cualquier wording reutilizable. | Entra solo como candidato. Se aplica al canon después de que su revisor lo aprueba. |

Ante la duda, es clase B. El merge de ambas clases es del owner del canon.

## Principio: mínima intervención del equipo

Si revisar exige abrir otra herramienta, aprender un formato o acordarse, no ocurre. El ciclo le lleva a cada revisor una pregunta corta en un lugar donde ya trabaja y registra la respuesta por él.

- Usar el canon no requiere ninguna acción: cada chat conectado al repositorio lee `main`, así que un merge actualiza a todos.
- Revisar requiere contestar preguntas de sí o no en una sola página.
- El silencio no aprueba un cambio de clase B.

## Calendario

Hay una sola iteración por semana. Cada iteración cierra la semana anterior y abre la nueva.

| Momento | Qué pasa | Quién | Acción del equipo |
| --- | --- | --- | --- |
| Día de iteración: `[COMPLETAR]`, primero | Se lee la agenda de la semana anterior. Lo contestado se registra, se aplica al canon, se evalúa y sale el PR. | `curador`, `evaluador` | Ninguna |
| Día de iteración, después | Barrido de fuentes, informe de frescura, candidatos nuevos en `_inbox/AAAA-Www/` y agenda nueva con cada revisor etiquetado. | `curador`, `frescura`, `publicador` | Ninguna |
| Durante la semana | Cada revisor recibe el aviso y contesta sus filas. | Revisores | Escribir `Sí`, `No` u `Otro` |
| Cuando el PR está listo | Merge y publicación de la copia de lectura. | Owner del canon, `publicador` | Un merge |

Lo que no se contestó vuelve a aparecer en la agenda siguiente, con el revisor etiquetado otra vez. A la segunda semana sin respuesta se abre en `governance/decision-log.md` con su revisor como owner.

## Dónde se revisa

| Quién | Dónde | Qué hace |
| --- | --- | --- |
| Revisores | Agenda semanal en la capa de trabajo | Cada uno contesta las filas donde está etiquetado. |
| Owner del canon | Plataforma de git | Ve el diff del PR semanal y mergea. |

### Estructura en la capa de trabajo

| Objeto | Qué es | Referencia |
| --- | --- | --- |
| `Agenda semanal` | Base con una fila por semana. La fila es el documento de la agenda. | `[COMPLETAR: link o ID]` |
| `Canon vigente` | Copia de lectura de lo aprobado. Se pisa en cada publicación. | `[COMPLETAR: link o ID]` |

Propiedades de la fila: semana (`AAAA-Www`), estado, candidatos, sin responder, revisores, link al PR y versión.

Cuerpo de la fila: una tabla por revisor con las columnas ID, Responde, Pregunta, Por qué se pregunta, Decisión y Nota. El modelo está en `templates/agenda-semanal.md`.

### Etiquetado

Cada fila de las tablas menciona al usuario del revisor en la columna `Responde`. La herramienta le avisa; nadie más tiene que avisarle.

- Se etiqueta al publicar la agenda y cada vez que se le agrega un cambio.
- Una fila ya contestada no se vuelve a etiquetar.
- Si un revisor no tiene usuario en la capa de trabajo, su cambio queda `bloqueado`.

### De la agenda al PR

El PR se genera en la iteración siguiente, sin que nadie lo pida.

| Estado | Quién lo pone | Qué significa |
| --- | --- | --- |
| `En revisión` | `publicador`, al publicar | El equipo está contestando. |
| `Revisada` | Owner del canon, opcional | Cierre anticipado: pide pasar la agenda al PR sin esperar a la iteración. |
| `En PR` | `curador` | Lo contestado está aplicado y evaluado; falta el merge. |
| `Mergeada` | `publicador`, después del merge | La versión nueva está en la copia de lectura. |

Reglas del pasaje:

- `Sí` pasa el candidato a `aprobado`; `No`, a `rechazado` con la Nota como motivo. `Otro`, una celda vacía o una respuesta ambigua lo dejan `propuesto`.
- Solo vale la decisión escrita en una fila donde `Responde` es esa persona.
- La respuesta se registra en el candidato bajo `## Respuesta del revisor`, citando dónde y cuándo se dio.
- Una Nota que cambia el valor propuesto se aplica tal como está escrita; si no alcanza para saber qué escribir en el canon, el candidato queda `bloqueado`.
- Si no hubo ninguna respuesta, no se abre PR de decisiones; los cambios de clase A salen igual.

## Agentes

Viven en `.claude/agents/`. Ninguno mergea ni envía mensajes. No reemplazan a los skills: los usan.

| Agente | Cuándo corre | Escribe en |
| --- | --- | --- |
| `curador` | Día de iteración; antes si el owner lo pide | `_inbox/`; canon solo para clase A o candidato aprobado |
| `frescura` | Día de iteración | `_inbox/AAAA-Www/informe-frescura.md` |
| `evaluador` | Al armar el PR y ante cualquier PR que toque `canon/`, `skills/` o `AGENTS.md` | `_inbox/AAAA-Www/informe-evals.md` |
| `publicador` | Día de iteración y después de cada merge | Solo la agenda semanal y la copia de lectura |

Cómo programarlos está en `automation/README.md`.

## Cierre de la semana

Al mergear, los candidatos `aplicado` y `rechazado` se eliminan de `_inbox/`; el historial de git los conserva. Toda decisión de clase B aplicada se registra en `governance/decisiones.md` con ID nuevo, owner y evidencia.
