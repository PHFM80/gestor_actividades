from django import forms

from core.forms import apply_bootstrap_styles
from donaciones.models import UnidadMedida


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ["nombre"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if UnidadMedida.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe una unidad de medida con ese nombre.")
        return nombre
