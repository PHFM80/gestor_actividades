# Overview

Gestor de Actividades es una aplicacion Django para administrar personas, actividades y donaciones.

**Capacidades actuales**
- Home publica con modo claro/oscuro.
- Login con validaciones y visualizacion/ocultacion de password.
- Dashboard de usuario (vista calendario base, actualmente sin items persistidos).
- Dashboard admin inicial.
- Complementos de geografia en admin: paises, provincias y localidades.
- Modelado inicial por dominio para personas, actividades, donaciones y comunicaciones.

**Entidades principales**
- `core.Usuario`, `core.Rol`, `core.RegistroCambio`, `core.ConfiguracionSistema`.
- `geo.Pais`, `geo.Provincia`, `geo.Localidad`.
- `personas.Persona`, `personas.PersonaRol`.
- `actividades.Calendario`, `actividades.Actividad`, `actividades.ParticipacionActividad`, `actividades.AgendaPersonal`.
- `donaciones.Donacion`, `donaciones.ItemDonacion`.
- `comunicaciones.CanalNotificacion`, `comunicaciones.Notificacion`.

**Rutas principales**
- Publicas:
  - `/`
  - `/login/`, `/logout/`
- Dashboard:
  - `/dashboard/`
  - `/dashboard/empresa/<empresa_id>/` (ruta legacy, hoy redirige a `/dashboard/`)
- Admin:
  - `/dashboard/admin/`
  - `/dashboard/admin/complementos/`
  - `/dashboard/admin/complementos/paises/`
  - `/dashboard/admin/complementos/provincias/`
  - `/dashboard/admin/complementos/localidades/`
