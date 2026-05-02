from django import forms
from django.core.exceptions import ValidationError

from core.models import RolSistema
from geo.models import Localidad, Pais, Provincia


def apply_bootstrap_styles(form):
    for name, field in form.fields.items():
        widget = field.widget
        widget_classes = widget.attrs.get("class", "")

        if isinstance(widget, forms.CheckboxInput):
            base_class = "form-check-input"
        elif isinstance(widget, forms.Select):
            base_class = "form-select"
        else:
            base_class = "form-control"

        if form.is_bound and name in form.errors:
            base_class = f"{base_class} is-invalid"

        widget.attrs["class"] = f"{widget_classes} {base_class}".strip()


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ["nombre", "codigo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        queryset = Pais.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise ValidationError("Ya existe un pais con ese nombre.")
        return nombre


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ["nombre", "pais"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        pais = cleaned_data.get("pais")
        if nombre and pais:
            existe = Provincia.objects.filter(nombre__iexact=nombre.strip(), pais=pais)
            if self.instance.pk:
                existe = existe.exclude(pk=self.instance.pk)
            if existe.exists():
                self.add_error("nombre", "Ya existe una provincia con ese nombre en el pais seleccionado.")
        return cleaned_data


class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = ["nombre", "provincia"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        provincia = cleaned_data.get("provincia")
        if nombre and provincia:
            existe = Localidad.objects.filter(nombre__iexact=nombre.strip(), provincia=provincia)
            if self.instance.pk:
                existe = existe.exclude(pk=self.instance.pk)
            if existe.exists():
                self.add_error("nombre", "Ya existe una localidad con ese nombre en la provincia seleccionada.")
        return cleaned_data


class RolSistemaForm(forms.ModelForm):
    class Meta:
        model = RolSistema
        fields = ["nombre", "codigo", "descripcion", "activo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_styles(self)
        self.fields["codigo"].required = False

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        codigo = cleaned_data.get("codigo")
        descripcion = cleaned_data.get("descripcion")
        if nombre is not None:
            cleaned_data["nombre"] = nombre.strip()
        if codigo is not None:
            cleaned_data["codigo"] = codigo.strip()
        if descripcion is not None:
            cleaned_data["descripcion"] = descripcion.strip()
        return cleaned_data
