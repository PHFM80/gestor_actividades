from django.db import models


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre_1 = models.CharField(max_length=150, blank=True, default='')
    nombre_2 = models.CharField(max_length=150, blank=True)
    apellido_1 = models.CharField(max_length=150, blank=True, default='')
    apellido_2 = models.CharField(max_length=150, blank=True)
    tipo_documento = models.ForeignKey(
        'personas.TipoDocumento',
        on_delete=models.PROTECT,
        related_name='personas',
        null=True,
        blank=True,
    )
    numero_documento = models.CharField(max_length=30, unique=True, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True)
    localidad = models.ForeignKey(
        'geo.Localidad',
        on_delete=models.PROTECT,
        related_name='personas',
        null=True,
        blank=True,
    )
    guia = models.BooleanField(default=False)
    garante = models.BooleanField(default=False)
    fecha_recepcion = models.DateField(null=True, blank=True)
    lugar = models.CharField(max_length=150, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f'{self.apellido_1}, {self.nombre_1}'


class Usuario(models.Model):
    persona = models.OneToOneField(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='usuario',
    )
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    rol_sistema = models.ForeignKey(
        'core.RolSistema',
        on_delete=models.PROTECT,
        related_name='usuarios_persona',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
