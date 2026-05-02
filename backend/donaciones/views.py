from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

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
            form.save()
            messages.success(request, "Unidad de medida creada correctamente.")
            return redirect("dashboard_admin_complemento_unidades_medida")
    else:
        form = UnidadMedidaForm()
    items = UnidadMedida.objects.order_by("nombre")
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Unidad de Medida",
            "description": "Carga unidades de medida para los items de donacion.",
            "form": form,
            "items_title": "Unidades de medida cargadas",
            "items": items,
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
