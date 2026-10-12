# Prompt: brief diario

Cada persona lo programa en su propia cuenta, con sus propios conectores. Reemplazar cada `[COMPLETAR]`.

```text
Prepará el brief diario de reuniones de [COMPLETAR: persona] en [COMPLETAR: empresa]. Esta corrida no tiene memoria de corridas anteriores.

Preparación
1. Ir al clon [COMPLETAR: ruta del clon], pasar a main y actualizar. Si falla, seguir con lo que haya y decirlo en el brief.
2. Leer AGENTS.md, brain.yml y skills/company-daily-brief/SKILL.md. Seguir ese skill; manda sobre este prompt si hay diferencia.

Fuentes: solo los conectores de la cuenta de esta persona. Calendario para las reuniones de hoy, correo para los últimos hilos con los asistentes, notas de reuniones, CRM para el estado de la cuenta. No leer ni resumir toda la bandeja.

Salida: un brief con una sección por reunión, en el formato del skill, que cierre con prioridades, seguimientos y cambios candidatos para el brain. Dejarlo como borrador.

Límites
- No enviar ningún mensaje: solo borradores.
- No escribir en el CRM, en la capa de trabajo ni en el repositorio.
- Precios, claims, alcance y disponibilidad salen solo del canon de main. Nada de _inbox/ es verdad.
- Si falta un acceso o una fuente, decirlo en el brief en lugar de completar con suposiciones.
```
