# Arquitectura general del proyecto

## Enfoque general

El proyecto se organiza separando responsabilidades entre backend, frontend web y frontend móvil.

La arquitectura base del proyecto es:

- Backend con Django.
- Frontend web con Django Templates.
- APIs con Django REST Framework.
- Frontend móvil con Kivy.

El backend es la fuente principal de datos, reglas de negocio y validaciones críticas.

## Estructura general recomendada

Para proyectos nuevos:


proyecto/
├── README.md
├── ai/
│   ├── README.md
│   ├── context/
│   └── skills/
│
├── backend/
│   ├── README.md
│   ├── docs/
│   ├── ai/
│   ├── manage.py
│   ├── config/
│   └── apps/
│
└── frontend/
    ├── README.md
    ├── docs/
    ├── ai/
    ├── main.py
    ├── buildozer.spec
    └── assets/