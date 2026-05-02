from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio.')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        if not usuario.username:
            usuario.username = email
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=30, unique=True)
    localidad = models.ForeignKey(
        'geo.Localidad',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='usuarios',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'dni', 'telefono']
    objects = UsuarioManager()

    def __str__(self):
        return self.email


class RolSistema(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class RegistroCambio(models.Model):
    class Accion(models.TextChoices):
        INSERCION = 'insercion', 'Insercion'
        MODIFICACION = 'modificacion', 'Modificacion'
        ELIMINACION = 'eliminacion', 'Eliminacion'
        OTRO = 'otro', 'Otro'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cambios_registrados',
    )
    accion = models.CharField(max_length=20, choices=Accion.choices, default=Accion.OTRO)
    entidad = models.CharField(max_length=100, blank=True, default='')
    entidad_id = models.CharField(max_length=100, blank=True, default='')
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.entidad}:{self.entidad_id} - {self.accion}'


class ConfiguracionSistema(models.Model):
    clave = models.CharField(max_length=100, unique=True)
    valor = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clave
