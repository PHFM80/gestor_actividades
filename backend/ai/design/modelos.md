## Entidades y campos 
# Diseño de modelos

## App: core

### RolSistema
**Descripción:** define el nivel de acceso al sistema.

**Campos sugeridos:**
- nombre
- codigo
- descripcion


### RegistroCambio
**Descripción:** registra inserciones, modificaciones y eliminaciones lógicas relevantes del sistema.

**Campos sugeridos:**
 usuario
- accion
- entidad
- entidad_id
- fecha

---

## App: geo

### Pais
**Descripción:** país normalizado del sistema.

**Campos sugeridos:**
- nombre
- codigo

### Provincia
**Descripción:** provincia o estado asociado a un país.

**Campos sugeridos:**
- nombre
- pais

### Localidad
**Descripción:** localidad asociada a una provincia.

**Campos sugeridos:**
- nombre
- provincia

---

## App: personas

### TipoDocumento
**Descripción:** catálogo de tipos de documento permitidos en el sistema.

**Campos sugeridos:**
- nombre
- codigo

### Persona
**Descripción:** entidad principal del sistema. Puede existir sin acceso como usuario.

**Campos sugeridos:**
- nombre_1
- nombre_2
- apellido_1
- apellido_2
- tipo_documento
- numero_documento
- fecha_nacimiento
- genero
- telefono
- email
- direccion
- localidad
- guia
- garante
- fecha_recepcion
- lugar
- observaciones

### Usuario
**Descripción:** representa a una persona con acceso al sistema.

**Campos sugeridos:**
- persona
- username
- password
- rol_sistema
- is_active
- is_staff
- last_login

---

## App: actividades

### TipoActividad
**Descripción:** define la actividad base o plantilla general.

**Campos sugeridos:**
- nombre
- descripcion

### Actividad
**Descripción:** ocurrencia concreta de una actividad en una fecha y hora determinadas.

**Campos sugeridos:**
- tipo_actividad
- tema
- descripcion
- fecha
- dia
- hora_inicio
- hora_fin
- lugar


### RolActividad
**Descripción:** define la función de una persona dentro de una actividad.

**Campos sugeridos:**
- nombre
- descripcion


### ActividadPersona
**Descripción:** vincula una persona con una actividad concreta según su rol.

**Campos sugeridos:**
- actividad
- persona
- rol_actividad


### InscripcionActividad
**Descripción:** registra la inscripción de una persona a un tipo de actividad.

**Campos sugeridos:**
- persona
- tipo_actividad

### AsistenciaActividad
**Descripción:** registra la asistencia real de una persona a una actividad concreta.

**Campos sugeridos:**
- actividad
- persona
- hora_llegada
- observaciones

---

## App: donaciones

### UnidadMedida
**Descripción:** catálogo de unidades de medida utilizadas en los ítems de donación.

**Campos sugeridos:**
- nombre

### Donacion
**Descripción:** registro principal de una entrega realizada por una persona en una fecha determinada.

**Campos sugeridos:**
- persona
- fecha
- observaciones

### ItemDonacion
**Descripción:** detalle de cada elemento incluido dentro de una donación.

**Campos sugeridos:**
- donacion
- descripcion
- cantidad
- unidad_medida

---

