# Apps

**core**
- Define el usuario personalizado (`Usuario`) basado en email.
- Define `Rol`, `RegistroCambio` y `ConfiguracionSistema`.

**geo**
- Catalogo de `Pais`, `Provincia` y `Localidad`.

**personas**
- `Persona` como entidad principal para datos personales.
- `PersonaRol` para asignar roles a persona o usuario.

**actividades**
- `Calendario` para organizar actividades.
- `Actividad` con fecha, descripcion y alcance global.
- `ParticipacionActividad` para asociar personas/usuarios a actividades.
- `AgendaPersonal` como base para evolucion personal por usuario.

**donaciones**
- `Donacion` para registrar una donacion por persona y fecha.
- `ItemDonacion` para detalle de elementos donados.

**comunicaciones**
- `CanalNotificacion` para definir medios de envio.
- `Notificacion` con estado y destinatario (persona o usuario).
