# Dashboard Admin

Este documento resume los flujos implementados en el panel admin.

**Inicio admin**
- Ruta: `/dashboard/admin/`
- Muestra una pantalla base para administradores.

**Complementos**
- Ruta base: `/dashboard/admin/complementos/`
- Altas operativas disponibles:
  - Paises: `/dashboard/admin/complementos/paises/`
  - Provincias: `/dashboard/admin/complementos/provincias/`
  - Localidades: `/dashboard/admin/complementos/localidades/`

**Validaciones**
- En provincias, no se permite repetir nombre dentro del mismo pais.
- En localidades, no se permite repetir nombre dentro de la misma provincia.

**Acceso y reglas de sesion**
- Usuarios admin (`is_staff` o `is_superuser`) acceden a dashboard admin.
- Usuarios no admin son redirigidos al dashboard de usuario (`/dashboard/`).
