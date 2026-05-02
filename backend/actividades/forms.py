from django import forms

from actividades.models import RolActividad, TipoActividad
from core.forms import apply_bootstrap_styles


class RolActividadForm(forms.ModelForm):
    class Meta:
        model = RolActividad
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if RolActividad.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un rol de actividad con ese nombre.")
        return nombre


class TipoActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if TipoActividad.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un tipo de actividad con ese nombre.")
        return nombre
