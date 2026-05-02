# Alcance general del proyecto

## Objetivo
Sistema web orientado a la gestión de personas, actividades y donaciones, con control de accesos según tipo de usuario y trazabilidad de cambios realizados en el sistema.

## Incluido en el alcance general

- Backend con Django.
- Frontend web con Django Templates.
- APIs con Django REST Framework para consumo interno, integraciones y app móvil.
- Frontend móvil con Kivy.
- Documentación general del proyecto.
- Contexto IA general, backend y frontend.
- Organización del proyecto separando raíz, backend y frontend.

## Alcance por etapas

El proyecto puede desarrollarse por etapas.

Primera etapa habitual:

- Backend Django.
- Templates web.
- Reglas de negocio.
- Modelos, vistas, formularios y panel web.

Segunda etapa habitual:

- APIs con DRF.
- Consumo de datos desde frontend móvil.
- App móvil con Kivy.

Tercera etapa habitual:

- Compilación APK/AAB.
- Firma de la app.
- Distribución o publicación en Play Store.

## Fuera del alcance por defecto

- Funcionalidades no solicitadas explícitamente.
- Reestructuración completa de proyectos ya iniciados sin necesidad real.
- Agregar tecnologías externas sin justificación.
- Mover lógica crítica de negocio al frontend móvil.

## Separación de responsabilidades

- La raíz del proyecto contiene documentación y contexto general.
- El backend contiene lógica de negocio, datos, templates web y APIs.
- El frontend móvil, cuando exista, funcionará como cliente de la API.
- La app móvil no debe contener lógica crítica de negocio.

## Criterio de evolución

El proyecto debe crecer por etapas, evitando agregar estructuras, carpetas o workflows antes de que sean necesarios.