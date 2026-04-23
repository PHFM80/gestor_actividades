from django.db import models
from django.conf import settings


class Calendario(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    calendario = models.ForeignKey(
        'actividades.Calendario',
        on_delete=models.PROTECT,
        related_name='actividades',
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    es_global = models.BooleanField(default=True)

    class Meta:
        ordering = ['fecha_inicio']

    def __str__(self):
        return self.titulo


class ParticipacionActividad(models.Model):
    actividad = models.ForeignKey(
        'actividades.Actividad',
        on_delete=models.CASCADE,
        related_name='participaciones',
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='participaciones_actividad',
        null=True,
        blank=True,
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='participaciones_actividad',
        null=True,
        blank=True,
    )
    rol_participacion = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(persona__isnull=False) | models.Q(usuario__isnull=False),
                name='participacion_requiere_persona_o_usuario',
            ),
        ]


class AgendaPersonal(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='agendas_personales',
    )
    nombre = models.CharField(max_length=150, default='Agenda personal')
    activa = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'nombre'],
                name='unique_agenda_personal_por_usuario',
            ),
        ]
