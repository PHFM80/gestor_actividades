# Templates

Este documento describe las vistas HTML y el orden de carga de assets.

**Estructura y herencia**
```
base.html
├── index.html
│   └── login.html
└── dashboard/base.html
    ├── dashboard/index.html
    ├── dashboard/seleccionar_empresa.html
    └── dashboard/admin/*
```

- `templates/base.html`
  - Base global.
  - Carga Bootstrap, tipografia, themes y `static/css/base.css`.
  - Incluye boton de modo claro/oscuro.
- `templates/index.html`
  - Home publica simplificada para gestion de actividades.
  - Carga `static/css/index.css` y `static/js/index.js`.
- `templates/login.html`
  - Login con mensajes de error y toggle de password.
- `templates/dashboard/base.html`
  - Layout del dashboard.
  - Sidebar con estado activo dinamico segun ruta.
  - Incluye acceso admin a `Complementos`.
  - Carga `static/css/dashboard.css` y `static/js/dashboard.js`.
- `templates/dashboard/seleccionar_empresa.html`
  - Vista legacy (actualmente la ruta redirige a `/dashboard/`).
- `templates/dashboard/admin/complemento*.html`
  - Carga de catalogos geograficos (paises, provincias, localidades).
- `templates/dashboard/admin/index.html`
  - Pantalla inicial del dashboard admin.

**Orden de assets**
1. Bootstrap CSS.
2. `static/css/themes/theme-light.css`.
3. `static/css/themes/theme-dark.css`.
4. `static/css/base.css`.
5. CSS especifico (`index.css`, `dashboard.css`).
6. Bootstrap JS (bundle).
7. `static/js/base.js`.
8. JS especifico (`index.js`, `dashboard.js`).

**Comportamientos relevantes de frontend**
- Theme persistente via `localStorage` (`gt-theme`).
- Filtros dinamicos en:
  - Complementos (provincias/localidades).
- Dependencias geograficas en formularios de complementos:
  - Pais -> Provincia -> Localidad.
- El dashboard de usuario renderiza un calendario base sin turnos persistidos.

**Rutas relacionadas**
- Publico: `/`, `/login/`, `/logout/`.
- Dashboard usuario: `/dashboard/`, `/dashboard/empresa/<id>/`.
- Dashboard admin: `/dashboard/admin/`, `/dashboard/admin/complementos/`, `/dashboard/admin/complementos/paises/`, `/dashboard/admin/complementos/provincias/`, `/dashboard/admin/complementos/localidades/`.
