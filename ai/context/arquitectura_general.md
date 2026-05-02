# Arquitectura general

## Stack base

El proyecto usa como arquitectura general:

- Backend con Django.
- Frontend web con Django Templates.
- APIs con Django REST Framework.
- Frontend móvil con Kivy.

## Separación principal

El backend es la fuente de verdad del sistema.

El frontend móvil Kivy funciona como cliente del backend.

## Estructura recomendada para proyectos nuevos

proyecto/
├── README.md
├── ai/
├── backend/
│   ├── README.md
│   ├── docs/
│   ├── ai/
│   ├── manage.py
│   ├── config/
│   └── apps/
└── frontend/
    ├── README.md
    ├── docs/
    ├── ai/
    ├── main.py
    ├── buildozer.spec
    └── assets/


## Organización de README, docs y ai

El proyecto usa archivos `README.md` como índices principales de cada nivel.

### Raíz del proyecto

El `README.md` de la raíz funciona como índice general del proyecto.

Debe orientar hacia:

- contexto IA general en `ai/`
- documentación del backend en `backend/README.md`
- documentación del frontend en `frontend/README.md`

### Carpeta `ai/` general

El archivo `ai/README.md` funciona como índice del contexto IA general.

Debe orientar hacia:

- `ai/context/`
- `ai/skills/`

El contexto IA general no debe repetir detalles específicos del backend ni del frontend.

### Backend

El archivo `backend/README.md` funciona como índice del backend.

Debe orientar hacia:

- `backend/docs/`
- `backend/ai/`

El archivo `backend/ai/README.md` funciona como índice del contexto IA específico del backend.

### Frontend

El archivo `frontend/README.md` funciona como índice del frontend móvil.

Debe orientar hacia:

- `frontend/docs/`
- `frontend/ai/`

El archivo `frontend/ai/README.md` funciona como índice del contexto IA específico del frontend.

### Regla general

Los `README.md` no deben contener documentación extensa.

Deben funcionar como índices, guías rápidas y puntos de entrada.

La documentación detallada debe modularizarse dentro de las carpetas `docs/`.

El contexto operativo para IA debe modularizarse dentro de las carpetas `ai/context/` y `ai/skills/`.