# Tests de Complementos

Este documento resume la cobertura de tests para complementos y su organizacion por dominio.

## Estructura por dominio

- `core/tests/test_complementos.py`
- `actividades/tests/test_complementos.py`
- `personas/tests/test_complementos.py`
- `donaciones/tests/test_complementos.py`

Cada app usa paquete `tests/` con `__init__.py` para discovery estandar de Django.

## Cobertura funcional

1. Acceso y permisos
- Requiere autenticacion (`login_required`).
- Usuario no admin recibe `403` en rutas de complementos.

2. Alta y edicion
- Se prueba creacion y posterior modificacion de cada complemento soportado.

3. Validaciones de unicidad
- Se prueban escenarios de duplicado por nombre/codigo o por combinacion (segun modelo).
- Se valida que la edicion no falle por comparar contra el propio registro.

4. Regla de no eliminacion en UI
- Se verifica que las pantallas de complementos no muestren accion `Eliminar`.

5. Auditoria en log
- Se validan eventos de auditoria en logger `complementos_audit`.
- Se prueban casos `success` y `error`.
- Se valida presencia de campos clave (`event`, `complemento_tipo`, `estado`, `cambios/errores`).

## Ejecucion

Desde `backend/`:

```powershell
.\venv\Scripts\python.exe manage.py test
```

Resultado actual validado: suite en verde.
