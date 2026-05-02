from django.db import models
from django.conf import settings


class CanalNotificacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Notificacion(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        ENVIADA = 'enviada', 'Enviada'
        FALLIDA = 'fallida', 'Fallida'

    canal = models.ForeignKey(
        'comunicaciones.CanalNotificacion',
        on_delete=models.PROTECT,
        related_name='notificaciones',
    )
    destinatario_persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='notificaciones',
        null=True,
        blank=True,
    )
    destinatario_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notificaciones',
        null=True,
        blank=True,
    )
    asunto = models.CharField(max_length=200, blank=True)
    mensaje = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    enviada_en = models.DateTimeField(null=True, blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada_en']
        constraints = [
            models.CheckConstraint(
                condition=models.Q(destinatario_persona__isnull=False)
                | models.Q(destinatario_usuario__isnull=False),
                name='notificacion_requiere_destinatario',
            ),
        ]
