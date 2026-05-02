# Complementos del Dashboard Admin

Este documento describe los cambios recientes sobre complementos en el dashboard admin.

## Objetivo

- Mantener los complementos como catalogos administrables por usuarios admin.
- Habilitar alta y edicion para todos los complementos operativos.
- Evitar eliminacion desde UI en esta capa.

## Cambios implementados

1. Se agrego edicion para complementos que antes solo tenian alta:
- Paises
- Provincias
- Localidades
- Roles de actividad
- Tipos de actividad
- Tipos de documento
- Unidades de medida

2. `RolSistema` ya tenia edicion y se mantuvo.

3. Se estandarizo el listado en UI con accion `Editar` para todos los casos anteriores.

4. Se corrigieron validaciones de formularios para que en modo edicion no tomen el propio registro como duplicado:
- `PaisForm`
- `ProvinciaForm`
- `LocalidadForm`
- `RolActividadForm`
- `TipoActividadForm`
- `TipoDocumentoForm`
- `UnidadMedidaForm`

## Rutas

- `/dashboard/admin/complementos/paises/`
- `/dashboard/admin/complementos/paises/<id>/editar/`
- `/dashboard/admin/complementos/provincias/`
- `/dashboard/admin/complementos/provincias/<id>/editar/`
- `/dashboard/admin/complementos/localidades/`
- `/dashboard/admin/complementos/localidades/<id>/editar/`
- `/dashboard/admin/complementos/roles-sistema/`
- `/dashboard/admin/complementos/roles-sistema/<id>/editar/`
- `/dashboard/admin/complementos/roles-actividad/`
- `/dashboard/admin/complementos/roles-actividad/<id>/editar/`
- `/dashboard/admin/complementos/tipos-actividad/`
- `/dashboard/admin/complementos/tipos-actividad/<id>/editar/`
- `/dashboard/admin/complementos/tipos-documento/`
- `/dashboard/admin/complementos/tipos-documento/<id>/editar/`
- `/dashboard/admin/complementos/unidades-medida/`
- `/dashboard/admin/complementos/unidades-medida/<id>/editar/`

## Regla de eliminacion

- No se agregaron endpoints de borrado en estas pantallas.
- La eliminacion no se expone desde UI de complementos.
