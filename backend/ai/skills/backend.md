# Backend - Criterios de desarrollo

## Enfoque general
- Pensar siempre en un sistema real en producción.
- Priorizar claridad, mantenibilidad y evolución progresiva.
- Evitar soluciones innecesariamente complejas.
- Implementar solo lo necesario para el requerimiento actual.

## Criterios de diseño
- Priorizar soluciones simples, entendibles y consistentes con el proyecto.
- No anticipar problemas que todavía no existen.
- Evitar sobreingeniería.
- Diseñar pensando primero en el dominio y luego en la implementación.
- Favorecer cambios pequeños, controlados y fáciles de revisar.

## Reutilización
- Reutilizar código existente antes de crear nuevo.
- Evitar duplicación de lógica.
- Si una regla o proceso se repite, evaluar su extracción a servicios u otros componentes reutilizables.

## Organización del backend
- Respetar la división del sistema en apps Django por dominio.
- Ubicar cada cambio en la app correspondiente según su responsabilidad.
- No mezclar lógica de distintos dominios en una misma app.
- Mantener funciones, clases y módulos pequeños y enfocados.
- Dividir archivos cuando aumenten demasiado en tamaño o responsabilidad.

## Modelado
- Pensar primero en los datos antes que en la lógica.
- Mantener consistencia en nombres, relaciones y estructuras.
- Diseñar modelos alineados al dominio del negocio.
- Evitar modelos sobrecargados con responsabilidades que no les corresponden.
- La lógica compleja no debe vivir en los modelos.

## Lógica de negocio
- La lógica de negocio debe estar centralizada en servicios.
- Las views no deben contener reglas de negocio.
- Los modelos pueden tener lógica simple y cercana a sus propios datos.
- Toda operación importante del sistema debe pasar por una capa clara de negocio.

## Views y endpoints
- Las views deben limitarse a orquestar flujo, validar entrada y devolver respuesta.
- No deben resolver lógica de negocio compleja.
- Deben apoyarse en servicios para acciones importantes.
- Lo mismo aplica tanto para Django Templates como para futuras APIs.

## Formularios, serializers y validaciones
- Usar formularios o serializers para validar datos de entrada según el canal.
- No duplicar validaciones sin necesidad.
- Separar validación de entrada de lógica de negocio.
- Mantener mensajes y reglas consistentes.

## Integraciones externas
- Toda integración externa debe estar aislada del dominio principal.
- No llamar integraciones externas directamente desde views.
- Las integraciones deben invocarse desde servicios.
- El sistema debe poder cambiar una integración sin afectar la lógica central.

## Cambios en el sistema
- Realizar cambios acotados y controlados.
- Evitar modificar múltiples partes del sistema sin necesidad.
- No romper funcionalidad existente.
- Antes de cambiar, revisar impacto en modelos, servicios, vistas, templates y flujos relacionados.

## Lectura del proyecto
- Analizar el código existente antes de proponer cambios.
- Adaptarse al estilo, estructura y convenciones del proyecto.
- Revisar si ya existe una solución similar antes de implementar una nueva.

## Escalabilidad
- Diseñar para crecimiento progresivo, no para complejidad anticipada.
- Preparar el backend para que la capa de presentación pueda evolucionar de Django Templates a React sin rehacer la lógica del sistema.
- Mantener desacoplado el dominio de la interfaz.

## Principios de diseño
- Aplicar principios SOLID cuando aporten claridad real.
- Mantener responsabilidad única por módulo o clase.
- Favorecer componentes reutilizables y desacoplados.
- Evitar dependencias innecesarias entre módulos.
- No aplicar patrones o principios si agregan complejidad sin beneficio claro.