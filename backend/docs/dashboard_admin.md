# Dashboard Admin

Este documento resume los flujos implementados en el panel admin.

**Inicio admin**
- Ruta: `/dashboard/admin/`
- Muestra una pantalla base para administradores.

**Complementos**
- Ruta base: `/dashboard/admin/complementos/`
- Altas y edicion operativas disponibles:
  - Paises: `/dashboard/admin/complementos/paises/`
    - Edicion: `/dashboard/admin/complementos/paises/<id>/editar/`
  - Provincias: `/dashboard/admin/complementos/provincias/`
    - Edicion: `/dashboard/admin/complementos/provincias/<id>/editar/`
  - Localidades: `/dashboard/admin/complementos/localidades/`
    - Edicion: `/dashboard/admin/complementos/localidades/<id>/editar/`
  - Roles de sistema: `/dashboard/admin/complementos/roles-sistema/`
    - Edicion: `/dashboard/admin/complementos/roles-sistema/<id>/editar/`
  - Roles de actividad: `/dashboard/admin/complementos/roles-actividad/`
    - Edicion: `/dashboard/admin/complementos/roles-actividad/<id>/editar/`
  - Tipos de actividad: `/dashboard/admin/complementos/tipos-actividad/`
    - Edicion: `/dashboard/admin/complementos/tipos-actividad/<id>/editar/`
  - Tipos de documento: `/dashboard/admin/complementos/tipos-documento/`
    - Edicion: `/dashboard/admin/complementos/tipos-documento/<id>/editar/`
  - Unidades de medida: `/dashboard/admin/complementos/unidades-medida/`
    - Edicion: `/dashboard/admin/complementos/unidades-medida/<id>/editar/`

**Validaciones**
- En provincias, no se permite repetir nombre dentro del mismo pais.
- En localidades, no se permite repetir nombre dentro de la misma provincia.
- En el resto de complementos, no se permite repetir segun su criterio de unicidad.

**Eliminacion**
- No se expone flujo de eliminacion en las pantallas de complementos.

**Acceso y reglas de sesion**
- Usuarios admin (`is_staff` o `is_superuser`) acceden a dashboard admin.
- Usuarios no admin son redirigidos al dashboard de usuario (`/dashboard/`).
