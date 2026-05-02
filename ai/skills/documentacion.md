# Criterios de documentación

## Regla general

La documentación debe estar separada por responsabilidad.

- La raíz orienta el proyecto completo.
- El backend documenta lo propio de Django, Templates y DRF.
- El frontend documenta lo propio de Kivy, assets y compilación móvil.
- La carpeta `ai/` guarda contexto operativo para IA.

## README

Los archivos `README.md` funcionan como índices y guías rápidas.

No deben contener documentación extensa.

Deben orientar hacia:

- carpetas `docs/`
- carpetas `ai/`
- archivos importantes del proyecto

## Docs

Las carpetas `docs/` contienen documentación humana más detallada.

Se usan para explicar:

- decisiones técnicas
- instalación
- uso del proyecto
- estructura
- flujos
- APIs
- compilación
- despliegue

## AI

Las carpetas `ai/` contienen contexto para asistentes IA.

Se usan para explicar:

- contexto del proyecto
- reglas de trabajo
- criterios técnicos
- decisiones tomadas

## No duplicar

No repetir la misma información en varios lugares.

Si una información pertenece al backend, debe estar en `backend/docs/` o `backend/ai/`.

Si pertenece al frontend móvil, debe estar en `frontend/docs/` o `frontend/ai/`.

Si aplica a todo el proyecto, debe estar en la raíz.