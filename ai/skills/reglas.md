# Reglas generales para IA

## Alcance

Estas reglas aplican a todo el proyecto.

El proyecto usa:

- Django para backend.
- Django Templates para frontend web.
- Django REST Framework para APIs.
- Kivy para frontend móvil.

## Reglas principales

- Leer primero el contexto general en `ai/context/`.
- Respetar la estructura definida del proyecto.
- No duplicar información entre contexto general, backend y frontend.
- No agregar funcionalidades no solicitadas.
- No incorporar nuevas tecnologías sin justificación.
- No mover lógica crítica de negocio al frontend móvil.
- Mantener el backend como fuente de verdad.
- Mantener Kivy como cliente móvil del backend.

## Código

- No generar código sin que sea necesario.
- No modificar archivos fuera del alcance solicitado.
- Hacer cambios pequeños y concretos.
- Evitar refactors grandes sin autorización.
- Mantener separadas las dependencias del backend y frontend.

## Documentación

- Usar los `README.md` como índices.
- Usar `docs/` para documentación específica.
- Usar `ai/` para contexto operativo de IA.
- No repetir documentación ya existente en otra carpeta.

## Forma de trabajo

- Primero analizar el pedido.
- Luego proponer pasos si el cambio tiene varias partes.
- Avanzar por etapas.
- No pasar a una etapa nueva si la anterior no está clara.