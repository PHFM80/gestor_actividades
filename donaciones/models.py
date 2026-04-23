from django.db import models
from django.conf import settings


class Donacion(models.Model):
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.PROTECT,
        related_name='donaciones',
    )
    fecha = models.DateField()
    observacion = models.TextField(blank=True)
    registrada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='donaciones_registradas',
    )
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', '-creada_en']

    def __str__(self):
        return f'Donacion #{self.pk} - {self.persona}'


class ItemDonacion(models.Model):
    donacion = models.ForeignKey(
        'donaciones.Donacion',
        on_delete=models.CASCADE,
        related_name='items',
    )
    descripcion = models.CharField(max_length=200)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.descripcion} x {self.cantidad}'
