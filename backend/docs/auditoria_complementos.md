# Auditoria de Complementos

Se implemento auditoria de complementos en archivo `.log` con formato JSONL.

## Ubicacion

- Archivo principal: `backend/logs/complementos.log`
- Rotacion: `10MB` por archivo, `5` backups.

## Eventos auditados

- `complemento.create`
- `complemento.update`

Se registran tanto eventos `success` como intentos fallidos `error`.

## Campos registrados por linea

- `timestamp` (UTC ISO-8601)
- `event`
- `complemento_tipo`
- `model_name`
- `registro_id`
- `usuario_id`
- `usuario_email`
- `ip`
- `request_id`
- `origen`
- `metodo`
- `estado`
- `cambios` (diff `before/after`)
- `errores` (errores de formulario/validacion cuando aplica)

## Complementos cubiertos

- Paises
- Provincias
- Localidades
- Roles de sistema
- Roles de actividad
- Tipos de actividad
- Tipos de documento
- Unidades de medida

## Notas operativas

- El log se escribe a traves del logger `complementos_audit`.
- El directorio `backend/logs/` se crea automaticamente desde `settings.py`.
- `backend/logs/` esta ignorado por Git.
