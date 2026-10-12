# Poner el brain a correr solo

El ciclo semanal y el brief diario son prompts que cualquier agente con acceso al repositorio y a los conectores puede ejecutar. Esta carpeta trae los dos, listos para programar.

| Archivo | Cuándo | Qué hace |
| --- | --- | --- |
| `ciclo-semanal.prompt.md` | Una vez por semana | Cierra la semana anterior, arma el PR, abre la semana nueva y etiqueta a los revisores. |
| `brief-diario.prompt.md` | Cada día hábil, por persona | Prepara el brief de reuniones con el skill `company-daily-brief`. |

## Antes de programar

1. **Completar `governance/ciclo-semanal.md`**: revisores, día de iteración y referencias de la agenda y de la copia de lectura. Sin eso el `publicador` se bloquea.
2. **Clonar el repositorio fuera de una carpeta sincronizada con la nube.** Un servicio de sincronización puede desalojar archivos internos de `.git` y dejar el repositorio sin poder commitear.
3. **Dar al clon una credencial de push propia**, por ejemplo una deploy key con escritura, configurada en el propio repositorio. El agente pushea ramas; nunca `main`.
4. **Reemplazar en cada prompt** los `[COMPLETAR]`: ruta del clon, nombre del repositorio y conectores.
5. **Correr cada tarea una vez a mano.** La primera corrida pide permisos para los conectores; si no se aprueban antes, la corrida automática se queda esperando.

## Dónde programarlos

- Tareas programadas del cliente de escritorio del agente: lo más simple; corren mientras la aplicación está abierta.
- Rutinas en la nube del proveedor del agente: no dependen de una computadora encendida; requieren que los conectores estén disponibles ahí.
- CI del repositorio: sirve para el `evaluador` y para `canon_check.py`; el barrido de fuentes vivas necesita conectores que el CI normalmente no tiene.

## Qué no automatizar todavía

- El merge. Es la única acción humana obligatoria del ciclo.
- El envío de mensajes. Los agentes dejan borradores.
- La escritura en el CRM, hasta haber visto varias corridas correctas del brief.

Dejar correr dos ciclos semanales completos antes de sumar otra automatización: si la agenda no se contesta, todo lo que se monte encima frena o trabaja con datos viejos.
