# Django - Reglas de trabajo

## Enfoque general
- Usar Django como framework principal del backend.
- Organizar el proyecto en apps separadas por dominio.
- Mantener desacoplada la lógica del negocio de la capa de presentación.
- Preparar el backend para una futura evolución de Django Templates a React.

## Apps
- Cada app debe representar un dominio o módulo funcional claro.
- No mezclar lógica de distintos dominios en una misma app.
- Ubicar modelos, vistas, formularios, servicios y templates en la app correspondiente.

## Models
- Representan entidades y relaciones del dominio.
- Mantener en los modelos solo lógica simple y cercana a sus datos.
- No colocar lógica de negocio compleja en los modelos.

## Views
- Manejan request/response y orquestan el flujo.
- No deben contener lógica de negocio.
- Deben delegar las operaciones importantes en servicios.

## Services
- Centralizan la lógica de negocio.
- Deben ser claros, reutilizables y alineados al dominio.
- Toda operación importante debe resolverse desde servicios.

## Forms
- Usar forms para validación de entrada en flujos con Django Templates.
- No colocar en forms la lógica de negocio central.

## Templates
- Deben ocuparse solo de presentación.
- No colocar lógica de negocio en templates.
- Mantener estructura clara y reutilizable.

## URLs
- Definir urls por app.
- Mantener nombres claros y consistentes.

## Admin
- Usar Django Admin como herramienta de soporte interno.
- No usar el admin como solución principal del sistema.

## Signals
- Evitar signals para lógica de negocio central.
- Preferir servicios explícitos para procesos importantes.

## Integraciones externas
- No llamar integraciones externas desde views o templates.
- Toda integración debe pasar por servicios o capas específicas.

## Cambios
- Revisar la estructura existente antes de modificar.
- Respetar la organización actual del proyecto.
- Hacer cambios acotados, claros y consistentes.