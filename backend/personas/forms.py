from django import forms

from core.forms import apply_bootstrap_styles
from personas.models import TipoDocumento


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ["nombre", "codigo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        codigo = cleaned_data.get("codigo")
        nombre_qs = TipoDocumento.objects.filter(nombre__iexact=nombre.strip()) if nombre else TipoDocumento.objects.none()
        codigo_qs = TipoDocumento.objects.filter(codigo__iexact=codigo.strip()) if codigo else TipoDocumento.objects.none()
        if self.instance.pk:
            nombre_qs = nombre_qs.exclude(pk=self.instance.pk)
            codigo_qs = codigo_qs.exclude(pk=self.instance.pk)
        if nombre_qs.exists():
            self.add_error("nombre", "Ya existe un tipo de documento con ese nombre.")
        if codigo_qs.exists():
            self.add_error("codigo", "Ya existe un tipo de documento con ese codigo.")
        return cleaned_data
