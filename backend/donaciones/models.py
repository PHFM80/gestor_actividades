from django.db import models


class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Donacion(models.Model):
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.PROTECT,
        related_name='donaciones',
    )
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-fecha']

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
    unidad_medida = models.ForeignKey(
        'donaciones.UnidadMedida',
        on_delete=models.PROTECT,
        related_name='items_donacion',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.descripcion} x {self.cantidad}'
