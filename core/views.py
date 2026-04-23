from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.utils import timezone

from core.forms import LocalidadForm, PaisForm, ProvinciaForm
from geo.models import Localidad, Pais, Provincia


def index(request):
    return render(request, "index.html")


class UsuarioLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return "/dashboard/admin/"
        return "/dashboard/"


class UsuarioLogoutView(LogoutView):
    next_page = "/"


@login_required
def dashboard(request):
    user = request.user
    if user.is_staff or user.is_superuser:
        return redirect("dashboard_admin")

    nombre = f"{user.nombre} {user.apellido}".strip()
    return render(
        request,
        "dashboard/index.html",
        {
            "welcome_name": nombre or user.email,
            "role_label": "Usuario",
            "company_name": None,
            "can_manage_horarios": False,
            "selected_date": timezone.now().date(),
            "calendar_items": [],
        },
    )


@login_required
def dashboard_select_empresa(request, empresa_id):
    messages.info(request, "La seleccion de empresa fue retirada en esta limpieza.")
    return redirect("dashboard")


@login_required
def admin_dashboard(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied
    return render(request, "dashboard/admin/index.html", admin_context(request.user))


@login_required
def admin_complementos(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied
    return render(request, "dashboard/admin/complementos.html", admin_context(request.user))


@login_required
def admin_complemento_paises(request):
    require_admin(request.user)
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pais creado correctamente.")
            return redirect("dashboard_admin_complemento_paises")
    else:
        form = PaisForm()
    items = Pais.objects.order_by("nombre")
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Paises",
            "description": "Carga paises base para la configuracion geografica.",
            "form": form,
            "items_title": "Paises cargados",
            "items": items,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_provincias(request):
    require_admin(request.user)
    if request.method == "POST":
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Provincia creada correctamente.")
            return redirect("dashboard_admin_complemento_provincias")
    else:
        form = ProvinciaForm()
    ordered_fields = [form[name] for name in ["pais", "nombre"] if name in form.fields]
    items = Provincia.objects.select_related("pais").order_by("nombre")
    items_payload = [{"label": str(item), "parent_id": item.pais_id} for item in items]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Provincias",
            "description": "Carga provincias asociadas a cada pais.",
            "form": form,
            "field_ordered": ordered_fields,
            "items_title": "Provincias cargadas",
            "items_payload": items_payload,
            "filter_select_id": form["pais"].id_for_label,
            "filter_empty_text": "Selecciona un pais para ver provincias cargadas.",
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_localidades(request):
    require_admin(request.user)
    if request.method == "POST":
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Localidad creada correctamente.")
            return redirect("dashboard_admin_complemento_localidades")
    else:
        form = LocalidadForm()
    ordered_fields = [form[name] for name in ["provincia", "nombre"] if name in form.fields]
    items = Localidad.objects.select_related("provincia").order_by("nombre")
    items_payload = [{"label": str(item), "parent_id": item.provincia_id} for item in items]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Localidades",
            "description": "Carga localidades asociadas a cada provincia.",
            "form": form,
            "field_ordered": ordered_fields,
            "items_title": "Localidades cargadas",
            "items_payload": items_payload,
            "filter_select_id": form["provincia"].id_for_label,
            "filter_empty_text": "Selecciona una provincia para ver localidades cargadas.",
            **admin_context(request.user),
        },
    )


def require_admin(user):
    if not (user.is_staff or user.is_superuser):
        raise PermissionDenied


def admin_context(user):
    nombre = f"{user.nombre} {user.apellido}".strip()
    return {
        "welcome_name": nombre or user.email,
        "role_label": "Administrador del sistema",
        "company_name": None,
    }
