from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from core.services.complementos_audit import cleaned_data_snapshot, log_complemento_event
from donaciones.forms import UnidadMedidaForm
from donaciones.models import UnidadMedida


@login_required
def admin_donaciones(request):
    _require_admin(request.user)
    return render(request, "dashboard/admin/donaciones.html", _dashboard_context(request.user))


@login_required
def admin_complemento_unidades_medida(request):
    _require_admin(request.user)
    if request.method == "POST":
        form = UnidadMedidaForm(request.POST)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.create",
                complemento_tipo="unidad_medida",
                status="success",
                model_name="UnidadMedida",
                registro_id=instance.pk,
                before={},
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Unidad de medida creada correctamente.")
            return redirect("dashboard_admin_complemento_unidades_medida")
        log_complemento_event(
            request=request,
            event="complemento.create",
            complemento_tipo="unidad_medida",
            status="error",
            model_name="UnidadMedida",
            errors=form.errors.get_json_data(),
        )
    else:
        form = UnidadMedidaForm()
    items = UnidadMedida.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/unidades-medida/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Unidad de Medida",
            "description": "Carga unidades de medida para los items de donacion.",
            "form": form,
            "items_title": "Unidades de medida cargadas",
            "items_links": items_links,
            **_dashboard_context(request.user),
        },
    )


@login_required
def admin_complemento_unidades_medida_editar(request, unidad_medida_id):
    _require_admin(request.user)
    unidad_medida = get_object_or_404(UnidadMedida, pk=unidad_medida_id)
    if request.method == "POST":
        before = {"nombre": unidad_medida.nombre}
        form = UnidadMedidaForm(request.POST, instance=unidad_medida)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.update",
                complemento_tipo="unidad_medida",
                status="success",
                model_name="UnidadMedida",
                registro_id=instance.pk,
                before=before,
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Unidad de medida actualizada correctamente.")
            return redirect("dashboard_admin_complemento_unidades_medida")
        log_complemento_event(
            request=request,
            event="complemento.update",
            complemento_tipo="unidad_medida",
            status="error",
            model_name="UnidadMedida",
            registro_id=unidad_medida.pk,
            before=before,
            errors=form.errors.get_json_data(),
        )
    else:
        form = UnidadMedidaForm(instance=unidad_medida)
    items = UnidadMedida.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/unidades-medida/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Editar Unidad de Medida",
            "description": "Modifica una unidad de medida existente. No se elimina desde esta pantalla.",
            "form": form,
            "items_title": "Unidades de medida cargadas",
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
