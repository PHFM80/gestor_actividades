import re

from django.core.exceptions import ValidationError

from core.models import RolSistema


def crear_rol_sistema(*, nombre, codigo, descripcion="", activo=True):
    nombre_limpio = (nombre or "").strip()
    if not nombre_limpio:
        raise ValidationError({"nombre": "El nombre es obligatorio."})

    codigo_limpio = _normalizar_codigo(codigo) or _normalizar_codigo(nombre_limpio)
    if not codigo_limpio:
        raise ValidationError({"codigo": "No se pudo generar un codigo valido para el rol."})

    descripcion_limpia = (descripcion or "").strip()
    _validar_unicidad(nombre_limpio, codigo_limpio)

    rol = RolSistema.objects.create(
        nombre=nombre_limpio,
        codigo=codigo_limpio,
        descripcion=descripcion_limpia,
        activo=bool(activo),
    )
    return rol


def editar_rol_sistema(*, rol, nombre, codigo, descripcion="", activo=True):
    nombre_limpio = (nombre or "").strip()
    if not nombre_limpio:
        raise ValidationError({"nombre": "El nombre es obligatorio."})

    codigo_limpio = _normalizar_codigo(codigo) or _normalizar_codigo(nombre_limpio)
    if not codigo_limpio:
        raise ValidationError({"codigo": "No se pudo generar un codigo valido para el rol."})

    descripcion_limpia = (descripcion or "").strip()
    _validar_unicidad(nombre_limpio, codigo_limpio, rol_actual=rol)

    rol.nombre = nombre_limpio
    rol.codigo = codigo_limpio
    rol.descripcion = descripcion_limpia
    rol.activo = bool(activo)
    rol.save(update_fields=["nombre", "codigo", "descripcion", "activo"])
    return rol


def _validar_unicidad(nombre, codigo, rol_actual=None):
    existe_nombre = RolSistema.objects.filter(nombre__iexact=nombre)
    existe_codigo = RolSistema.objects.filter(codigo__iexact=codigo)
    if rol_actual is not None:
        existe_nombre = existe_nombre.exclude(pk=rol_actual.pk)
        existe_codigo = existe_codigo.exclude(pk=rol_actual.pk)
    if existe_nombre.exists():
        raise ValidationError({"nombre": "Ya existe un rol de sistema con ese nombre."})
    if existe_codigo.exists():
        raise ValidationError({"codigo": "Ya existe un rol de sistema con ese codigo."})


def _normalizar_codigo(valor):
    texto = (valor or "").strip().upper()
    texto = re.sub(r"[^A-Z0-9]+", "_", texto)
    texto = re.sub(r"_+", "_", texto).strip("_")
    return texto
