from django.db import models


class TipoActividad(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    tipo_actividad = models.ForeignKey(
        'actividades.TipoActividad',
        on_delete=models.PROTECT,
        related_name='actividades',
        null=True,
        blank=True,
    )
    tema = models.CharField(max_length=200, blank=True, default='')
    descripcion = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True)
    dia = models.CharField(max_length=20, blank=True, default='')
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    lugar = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['fecha', 'hora_inicio']

    def __str__(self):
        return self.tema


class RolActividad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class ActividadPersona(models.Model):
    actividad = models.ForeignKey(
        'actividades.Actividad',
        on_delete=models.CASCADE,
        related_name='actividad_personas',
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='actividades',
    )
    rol_actividad = models.ForeignKey(
        'actividades.RolActividad',
        on_delete=models.PROTECT,
        related_name='actividad_personas',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['actividad', 'persona', 'rol_actividad'],
                name='unique_actividad_persona_rol',
            ),
        ]


class InscripcionActividad(models.Model):
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='inscripciones_actividad',
    )
    tipo_actividad = models.ForeignKey(
        'actividades.TipoActividad',
        on_delete=models.PROTECT,
        related_name='inscripciones',
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['persona', 'tipo_actividad'],
                name='unique_inscripcion_persona_tipo_actividad',
            ),
        ]


class AsistenciaActividad(models.Model):
    actividad = models.ForeignKey(
        'actividades.Actividad',
        on_delete=models.CASCADE,
        related_name='asistencias',
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE,
        related_name='asistencias_actividad',
    )
    hora_llegada = models.TimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)
