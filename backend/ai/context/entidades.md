# Entidades del Sistema

## Core

### Rol
Define el nivel de acceso dentro del sistema.

### RegistroCambio
Registra inserciones, modificaciones y otros cambios relevantes realizados en el sistema.

### ConfiguracionSistema
Permite almacenar configuraciones globales del sistema si fueran necesarias.

---

## Geografía

### Pais
- nombre
- codigo

### Provincia
- nombre
- pais

### Localidad
- nombre
- provincia

---

## Personas

### Persona
Entidad principal del sistema. Representa a cualquier persona registrada, tenga o no acceso operativo.

### Usuario
Representa a una persona con acceso al sistema.

### PersonaRol
Permite relacionar una persona o usuario con uno o más roles, en caso de requerir flexibilidad.

---

## Actividades

### Calendario
Representa el calendario general del sistema. Inicialmente orientado a actividades globales.

### Actividad
Representa una actividad registrada dentro del sistema.

### ParticipacionActividad
Relaciona personas con actividades, por ejemplo como responsables, asistentes o participantes.

### AgendaPersonal
Posible evolución futura para actividades propias de cada usuario.

---

## Donaciones

### Donacion
Registro principal de una donación realizada por una persona en una fecha determinada.

### ItemDonacion
Detalle de los elementos incluidos dentro de una donación.

---

## Comunicaciones

### Notificacion
Representa avisos o mensajes enviados por el sistema.

### CanalNotificacion
Define el medio por el cual se envía una notificación, por ejemplo email.
