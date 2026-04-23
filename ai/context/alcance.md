# Alcance del Sistema

## Propósito
Sistema web orientado a la gestión de personas, actividades y donaciones, con control de accesos según tipo de usuario y trazabilidad de cambios realizados en el sistema.

## Incluye
- Registro y gestión de personas
- Gestión de usuarios con diferentes niveles de acceso
- Registro y gestión de actividades
- Visualización de actividades en calendario
- Actividades globales visibles para los usuarios autorizados
- Posible evolución a agendas personales por usuario
- Registro de donaciones realizadas por personas
- Historial de donaciones con fecha, donante y elementos donados
- Notificaciones por email
- Auditoría de inserciones y modificaciones relevantes

## No incluye
- Facturación
- Contabilidad completa
- Facturación fiscal
- Gestión de impuestos
- Conciliación bancaria
- Marketplace
- Multi-tenant complejo
- App móvil en la primera etapa

## Decisiones clave
- El sistema estará centrado en tres pilares: personas, actividades y donaciones
- Personas es la entidad base del sistema
- Los usuarios del sistema derivan de personas con distintos permisos
- Los roles iniciales contemplan: administrador, editor, lector y persona registrada
- La prioridad funcional inicial es la gestión de actividades globales
- El calendario es una pieza central del sistema
- Las agendas personales son una evolución futura, no un requisito inicial obligatorio
- Las donaciones deben quedar asociadas a personas y registradas con trazabilidad
- El sistema debe registrar quién crea o modifica información y cuándo lo hace
- La integración principal de notificaciones será email
- La arquitectura debe ser simple al inicio y permitir crecimiento progresivo