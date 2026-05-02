# Arquitectura

Este documento resume la arquitectura actual basada en lo que existe en el codigo.

**Estructura de apps**
- `core`: usuario personalizado, roles, configuraciones y trazabilidad.
- `geo`: pais, provincia y localidad.
- `personas`: entidad persona y asignacion de roles.
- `actividades`: calendario, actividades, participaciones y agenda personal.
- `donaciones`: donacion e items de donacion.
- `comunicaciones`: canales y notificaciones.

**Relaciones clave (modelo)**
- `Usuario` (core) referencia opcionalmente `Localidad` (geo).
- `Persona` (personas) referencia opcionalmente `Localidad` (geo).
- `PersonaRol` vincula `Rol` con `Persona` o con `Usuario`.
- `Actividad` pertenece a `Calendario`.
- `ParticipacionActividad` vincula `Actividad` con `Persona` o con `Usuario`.
- `Donacion` pertenece a `Persona` y puede registrar `registrada_por` (`Usuario`).
- `ItemDonacion` pertenece a `Donacion`.
- `Notificacion` pertenece a `CanalNotificacion` y puede tener destinatario `Persona` o `Usuario`.
- `RegistroCambio` permite guardar trazabilidad de inserciones/modificaciones.

**Flujos existentes**
- Alta de datos base con `seed_initial_data` (geografia inicial).
- Gestion de catalogos geograficos desde dashboard admin.

**Pendiente (cuando exista)**
- Conectar dashboards con los nuevos modelos de actividades/donaciones.
- Integraciones reales de notificaciones.
- Diagrama de despliegue.
