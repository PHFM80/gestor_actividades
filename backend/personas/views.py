from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from core.services.complementos_audit import cleaned_data_snapshot, log_complemento_event
from personas.forms import TipoDocumentoForm
from personas.models import TipoDocumento


@login_required
def admin_cargar_personas(request):
    _require_admin(request.user)
    return render(request, "dashboard/admin/cargar_personas.html", _dashboard_context(request.user))


@login_required
def admin_cargar_usuarios(request):
    _require_admin(request.user)
    return render(request, "dashboard/admin/cargar_usuarios.html", _dashboard_context(request.user))


@login_required
def admin_complemento_tipos_documento(request):
    _require_admin(request.user)
    if request.method == "POST":
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.create",
                complemento_tipo="tipo_documento",
                status="success",
                model_name="TipoDocumento",
                registro_id=instance.pk,
                before={},
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Tipo de documento creado correctamente.")
            return redirect("dashboard_admin_complemento_tipos_documento")
        log_complemento_event(
            request=request,
            event="complemento.create",
            complemento_tipo="tipo_documento",
            status="error",
            model_name="TipoDocumento",
            errors=form.errors.get_json_data(),
        )
    else:
        form = TipoDocumentoForm()
    items = TipoDocumento.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/tipos-documento/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Tipo de Documento",
            "description": "Carga los tipos de documento habilitados.",
            "form": form,
            "items_title": "Tipos de documento cargados",
            "items_links": items_links,
            **_dashboard_context(request.user),
        },
    )


@login_required
def admin_complemento_tipos_documento_editar(request, tipo_documento_id):
    _require_admin(request.user)
    tipo_documento = get_object_or_404(TipoDocumento, pk=tipo_documento_id)
    if request.method == "POST":
        before = {"nombre": tipo_documento.nombre, "codigo": tipo_documento.codigo}
        form = TipoDocumentoForm(request.POST, instance=tipo_documento)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.update",
                complemento_tipo="tipo_documento",
                status="success",
                model_name="TipoDocumento",
                registro_id=instance.pk,
                before=before,
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Tipo de documento actualizado correctamente.")
            return redirect("dashboard_admin_complemento_tipos_documento")
        log_complemento_event(
            request=request,
            event="complemento.update",
            complemento_tipo="tipo_documento",
            status="error",
            model_name="TipoDocumento",
            registro_id=tipo_documento.pk,
            before=before,
            errors=form.errors.get_json_data(),
        )
    else:
        form = TipoDocumentoForm(instance=tipo_documento)
    items = TipoDocumento.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/tipos-documento/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Editar Tipo de Documento",
            "description": "Modifica un tipo de documento existente. No se elimina desde esta pantalla.",
            "form": form,
            "items_title": "Tipos de documento cargados",
            "items_links": items_links,
            **_dashboard_context(request.user),
        },
    )


def _require_admin(user):
    if not (user.is_staff or user.is_superuser):
        raise PermissionDenied


def _dashboard_context(user):
    nombre = f"{user.nombre} {user.apellido}".strip()
    return {
        "welcome_name": nombre or user.email,
        "role_label": "Administrador del sistema",
        "company_name": None,
    }
