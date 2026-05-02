from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from actividades.forms import RolActividadForm, TipoActividadForm
from actividades.models import RolActividad, TipoActividad


@login_required
def admin_crear_actividad(request):
    _require_admin(request.user)
    return render(request, "dashboard/admin/crear_actividad.html", _dashboard_context(request.user))


@login_required
def admin_complemento_roles_actividad(request):
    _require_admin(request.user)
    if request.method == "POST":
        form = RolActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rol de actividad creado correctamente.")
            return redirect("dashboard_admin_complemento_roles_actividad")
    else:
        form = RolActividadForm()
    items = RolActividad.objects.order_by("nombre")
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "RolActividad",
            "description": "Carga funciones posibles para las personas dentro de actividades.",
            "form": form,
            "items_title": "Roles de actividad cargados",
            "items": items,
            **_dashboard_context(request.user),
        },
    )


@login_required
def admin_complemento_tipos_actividad(request):
    _require_admin(request.user)
    if request.method == "POST":
        form = TipoActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de actividad creado correctamente.")
            return redirect("dashboard_admin_complemento_tipos_actividad")
    else:
        form = TipoActividadForm()
    items = TipoActividad.objects.order_by("nombre")
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Tipo de Actividad",
            "description": "Carga tipos base de actividad para reutilizar en el sistema.",
            "form": form,
            "items_title": "Tipos de actividad cargados",
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
