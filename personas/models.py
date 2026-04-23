from django.db import models
from django.conf import settings


class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    localidad = models.ForeignKey(
        'geo.Localidad',
        on_delete=models.PROTECT,
        related_name='personas',
        null=True,
        blank=True,
    )
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class PersonaRol(models.Model):
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='roles',
        null=True,
        blank=True,
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='roles_persona',
        null=True,
        blank=True,
    )
    rol = models.ForeignKey(
        'core.Rol',
        on_delete=models.PROTECT,
        related_name='asignaciones_persona',
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['persona', 'rol'],
                name='unique_persona_rol',
            ),
            models.UniqueConstraint(
                fields=['usuario', 'rol'],
                name='unique_usuario_rol',
            ),
            models.CheckConstraint(
                condition=models.Q(persona__isnull=False) | models.Q(usuario__isnull=False),
                name='personarol_requiere_persona_o_usuario',
            ),
        ]
