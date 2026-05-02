# AI - Punto de entrada general

Esta carpeta contiene el contexto general del proyecto y las reglas base que debe seguir cualquier asistente IA antes de trabajar sobre el repositorio.

## Objetivo

Antes de proponer cambios, generar código o modificar archivos, la IA debe leer este contexto general para entender:

- el stack principal del proyecto
- la organización del repositorio
- la separación entre backend y frontend móvil
- las reglas generales de trabajo
- cómo debe usar los contextos específicos

## Lectura obligatoria general

La IA debe leer primero estos archivos:

```text
ai/context/alcance_general.md
ai/context/arquitectura_general.md
ai/context/decisiones_generales.md
ai/skills/reglas.md
ai/skills/flujo_trabajo.md
ai/skills/documentacion.md
```

## Luego identificar el área de trabajo

Después de leer el contexto general, la IA debe identificar sobre qué parte del proyecto va a trabajar.

### Si el pedido afecta al backend

Debe leer también:

```text
backend/ai/README.md
```

Y luego seguir el contexto y reglas específicas definidas en:

```text
backend/ai/context/
backend/ai/skills/
```

El backend incluye:

- Django
- Django Templates
- Django REST Framework
- modelos
- vistas
- formularios
- APIs
- lógica de negocio
- persistencia
- autenticación
- validaciones

### Si el pedido afecta al frontend móvil

Debe leer también:

```text
frontend/ai/README.md
```

Y luego seguir el contexto y reglas específicas definidas en:

```text
frontend/ai/context/
frontend/ai/skills/
```

El frontend móvil incluye:

- Kivy
- pantallas móviles
- widgets
- consumo de APIs
- assets móviles
- sonidos
- Buildozer
- APK/AAB

### Si el pedido afecta a ambos

Debe leer ambos contextos específicos:

```text
backend/ai/README.md
frontend/ai/README.md
```

Y respetar la separación de responsabilidades entre backend y frontend móvil.

## Regla de prioridad

Cuando haya dudas, seguir este orden:

1. Reglas generales de `ai/`
2. Reglas específicas del área correspondiente
3. Código existente del proyecto
4. Pedido puntual del usuario

Si una regla general y una regla específica parecen entrar en conflicto, no asumir una solución automáticamente. Primero advertirlo y pedir confirmación.

## Regla principal

El backend es la fuente de verdad del sistema.

El frontend móvil Kivy funciona como cliente del backend.

No mover lógica crítica de negocio al frontend móvil.

## No duplicar contexto

La información general va en:

```text
ai/
```

La información específica del backend va en:

```text
backend/ai/
```

La información específica del frontend móvil va en:

```text
frontend/ai/
```

No duplicar documentación ni reglas entre carpetas.
