# Arquitectura del sistema

## Principios generales
- El proyecto está organizado en apps Django separadas por dominio.
- Cada app debe representar un módulo funcional del sistema.
- No mezclar lógica de diferentes dominios en una misma app.
- La arquitectura debe priorizar claridad, mantenimiento y escalabilidad progresiva.
- El sistema debe poder comenzar con Django Templates y evolucionar luego a un frontend en React sin rehacer la lógica principal.

## Organización por apps
- Cada app debe contener sus propias entidades, servicios, vistas y lógica relacionada a su dominio.
- Las apps deben comunicarse de forma clara, evitando dependencias innecesarias.
- No ubicar en una app lógica que pertenece funcionalmente a otra.
- Las apps principales del sistema responden al dominio del negocio, no a criterios técnicos o visuales.

## Responsabilidades por capa

### Models
- Definen la estructura de datos y las relaciones entre entidades.
- Deben contener solo lógica simple y cercana al modelo.
- No deben contener lógica de negocio compleja.
- No deben asumir responsabilidades de integración externa.

### Views
- Manejan la entrada y salida del sistema.
- En Django Templates, preparan el contexto y renderizan respuestas.
- En endpoints API, exponen datos y acciones de forma controlada.
- No deben contener lógica de negocio.
- Solo deben validar flujo, delegar en servicios y devolver respuesta.

### Services
- Contienen la lógica de negocio del sistema.
- Centralizan reglas, validaciones funcionales y casos de uso.
- Deben ser reutilizables, claros y desacoplados de la interfaz.
- Toda operación importante del sistema debe resolverse desde servicios.

### Forms / Serializers
- Se encargan de validación de entrada y transformación de datos según el canal.
- No deben contener lógica de negocio central.
- Deben trabajar en conjunto con views y services.

### Templates
- Deben limitarse a la presentación.
- No deben resolver lógica de negocio.
- Deben reflejar información ya preparada desde la vista o servicio correspondiente.

### Integraciones
- Toda integración externa debe estar aislada.
- No mezclar lógica de integración con lógica de negocio.
- Las integraciones deben ser llamadas desde servicios, no directamente desde views.
- El sistema debe poder cambiar una integración sin afectar el dominio principal.

## Organización del código
- Cada funcionalidad debe ubicarse en el archivo correspondiente.
- Evitar archivos grandes con múltiples responsabilidades.
- Dividir el código cuando aumente en complejidad.
- Mantener una estructura predecible dentro de cada app.
- Reutilizar lógica existente antes de crear nueva.

## Reglas de crecimiento
- El sistema debe poder crecer sin necesidad de reestructuración completa.
- Agregar nuevas funcionalidades sin romper las existentes.
- Diseñar pensando primero en el dominio y luego en la interfaz.
- La lógica del negocio no debe depender de Django Templates.
- El paso futuro a React debe impactar principalmente en la capa de presentación, no en el núcleo del sistema.

## Consistencia
- Mantener nombres claros y coherentes en todo el proyecto.
- Seguir los mismos patrones en todas las apps.
- Usar convenciones homogéneas para modelos, servicios, vistas y archivos.
- Evitar duplicación de lógica y estructuras inconsistentes.

## Modificaciones
- Antes de agregar código, revisar si ya existe algo similar.
- Evitar refactorizaciones innecesarias.
- Mantener compatibilidad con el código existente.
- Todo cambio debe respetar la arquitectura definida y la responsabilidad de cada capa.