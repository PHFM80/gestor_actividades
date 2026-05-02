# Decisiones generales

## Stack definido

El proyecto se basa en:

- Django para backend.
- Django Templates para frontend web.
- Django REST Framework para APIs.
- Kivy para frontend móvil.

## Backend

Django es la fuente principal del sistema.

El backend contiene:

- lógica de negocio
- modelos
- persistencia
- autenticación
- validaciones
- APIs

## Frontend web

El frontend web se resuelve con Django Templates.

No se incorpora un framework frontend separado salvo decisión futura explícita.

## APIs

DRF se usa para exponer APIs cuando sea necesario.

Principalmente para:

- consumo desde Kivy
- integraciones externas
- separación entre frontend móvil y backend

## Frontend móvil

Kivy funciona como cliente móvil del backend.

La app Kivy no contiene lógica crítica de negocio.

Su función principal es:

- mostrar información
- enviar acciones del usuario
- consumir APIs del backend

## Organización del proyecto

Para proyectos nuevos se prefiere:

proyecto/
├── backend/
└── frontend/