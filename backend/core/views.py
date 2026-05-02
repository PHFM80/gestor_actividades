from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from core.forms import LocalidadForm, PaisForm, ProvinciaForm, RolSistemaForm
from core.models import RolSistema
from core.services.complementos_audit import cleaned_data_snapshot, log_complemento_event
from core.services.roles_sistema import crear_rol_sistema, editar_rol_sistema
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
    require_admin(request.user)
    return render(request, "dashboard/admin/index.html", admin_context(request.user))


@login_required
def admin_complementos(request):
    require_admin(request.user)
    return render(request, "dashboard/admin/complementos.html", admin_context(request.user))


@login_required
def admin_complemento_paises(request):
    require_admin(request.user)
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.create",
                complemento_tipo="pais",
                status="success",
                model_name="Pais",
                registro_id=instance.pk,
                before={},
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Pais creado correctamente.")
            return redirect("dashboard_admin_complemento_paises")
        log_complemento_event(
            request=request,
            event="complemento.create",
            complemento_tipo="pais",
            status="error",
            model_name="Pais",
            errors=form.errors.get_json_data(),
        )
    else:
        form = PaisForm()
    items = Pais.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/paises/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Paises",
            "description": "Carga paises base para la configuracion geografica.",
            "form": form,
            "items_title": "Paises cargados",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_provincias(request):
    require_admin(request.user)
    if request.method == "POST":
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.create",
                complemento_tipo="provincia",
                status="success",
                model_name="Provincia",
                registro_id=instance.pk,
                before={},
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Provincia creada correctamente.")
            return redirect("dashboard_admin_complemento_provincias")
        log_complemento_event(
            request=request,
            event="complemento.create",
            complemento_tipo="provincia",
            status="error",
            model_name="Provincia",
            errors=form.errors.get_json_data(),
        )
    else:
        form = ProvinciaForm()
    items = Provincia.objects.select_related("pais").order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/provincias/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Provincias",
            "description": "Carga provincias asociadas a cada pais.",
            "form": form,
            "items_title": "Provincias cargadas",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_localidades(request):
    require_admin(request.user)
    if request.method == "POST":
        form = LocalidadForm(request.POST)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.create",
                complemento_tipo="localidad",
                status="success",
                model_name="Localidad",
                registro_id=instance.pk,
                before={},
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Localidad creada correctamente.")
            return redirect("dashboard_admin_complemento_localidades")
        log_complemento_event(
            request=request,
            event="complemento.create",
            complemento_tipo="localidad",
            status="error",
            model_name="Localidad",
            errors=form.errors.get_json_data(),
        )
    else:
        form = LocalidadForm()
    items = Localidad.objects.select_related("provincia").order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/localidades/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Localidades",
            "description": "Carga localidades asociadas a cada provincia.",
            "form": form,
            "items_title": "Localidades cargadas",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_paises_editar(request, pais_id):
    require_admin(request.user)
    pais = get_object_or_404(Pais, pk=pais_id)
    if request.method == "POST":
        before = {"nombre": pais.nombre, "codigo": pais.codigo}
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.update",
                complemento_tipo="pais",
                status="success",
                model_name="Pais",
                registro_id=instance.pk,
                before=before,
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Pais actualizado correctamente.")
            return redirect("dashboard_admin_complemento_paises")
        log_complemento_event(
            request=request,
            event="complemento.update",
            complemento_tipo="pais",
            status="error",
            model_name="Pais",
            registro_id=pais.pk,
            before=before,
            errors=form.errors.get_json_data(),
        )
    else:
        form = PaisForm(instance=pais)
    items = Pais.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/paises/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Editar Pais",
            "description": "Modifica un pais existente. No se elimina desde esta pantalla.",
            "form": form,
            "items_title": "Paises cargados",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_provincias_editar(request, provincia_id):
    require_admin(request.user)
    provincia = get_object_or_404(Provincia, pk=provincia_id)
    if request.method == "POST":
        before = {"nombre": provincia.nombre, "pais": provincia.pais_id}
        form = ProvinciaForm(request.POST, instance=provincia)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.update",
                complemento_tipo="provincia",
                status="success",
                model_name="Provincia",
                registro_id=instance.pk,
                before=before,
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Provincia actualizada correctamente.")
            return redirect("dashboard_admin_complemento_provincias")
        log_complemento_event(
            request=request,
            event="complemento.update",
            complemento_tipo="provincia",
            status="error",
            model_name="Provincia",
            registro_id=provincia.pk,
            before=before,
            errors=form.errors.get_json_data(),
        )
    else:
        form = ProvinciaForm(instance=provincia)
    items = Provincia.objects.select_related("pais").order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/provincias/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Editar Provincia",
            "description": "Modifica una provincia existente. No se elimina desde esta pantalla.",
            "form": form,
            "items_title": "Provincias cargadas",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_localidades_editar(request, localidad_id):
    require_admin(request.user)
    localidad = get_object_or_404(Localidad, pk=localidad_id)
    if request.method == "POST":
        before = {"nombre": localidad.nombre, "provincia": localidad.provincia_id}
        form = LocalidadForm(request.POST, instance=localidad)
        if form.is_valid():
            instance = form.save()
            log_complemento_event(
                request=request,
                event="complemento.update",
                complemento_tipo="localidad",
                status="success",
                model_name="Localidad",
                registro_id=instance.pk,
                before=before,
                after=cleaned_data_snapshot(form),
            )
            messages.success(request, "Localidad actualizada correctamente.")
            return redirect("dashboard_admin_complemento_localidades")
        log_complemento_event(
            request=request,
            event="complemento.update",
            complemento_tipo="localidad",
            status="error",
            model_name="Localidad",
            registro_id=localidad.pk,
            before=before,
            errors=form.errors.get_json_data(),
        )
    else:
        form = LocalidadForm(instance=localidad)
    items = Localidad.objects.select_related("provincia").order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/localidades/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Editar Localidad",
            "description": "Modifica una localidad existente. No se elimina desde esta pantalla.",
            "form": form,
            "items_title": "Localidades cargadas",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_roles_sistema(request):
    require_admin(request.user)
    if request.method == "POST":
        form = RolSistemaForm(request.POST)
        if form.is_valid():
            try:
                instance = crear_rol_sistema(
                    nombre=form.cleaned_data["nombre"],
                    codigo=form.cleaned_data.get("codigo"),
                    descripcion=form.cleaned_data.get("descripcion", ""),
                    activo=form.cleaned_data.get("activo", True),
                )
            except ValidationError as exc:
                if hasattr(exc, "message_dict"):
                    for field, field_errors in exc.message_dict.items():
                        for error in field_errors:
                            if field in form.fields:
                                form.add_error(field, error)
                            else:
                                form.add_error(None, error)
                else:
                    form.add_error(None, str(exc))
                log_complemento_event(
                    request=request,
                    event="complemento.create",
                    complemento_tipo="rol_sistema",
                    status="error",
                    model_name="RolSistema",
                    errors=form.errors.get_json_data(),
                )
            else:
                log_complemento_event(
                    request=request,
                    event="complemento.create",
                    complemento_tipo="rol_sistema",
                    status="success",
                    model_name="RolSistema",
                    registro_id=instance.pk,
                    before={},
                    after=cleaned_data_snapshot(form),
                )
                messages.success(request, "Rol de sistema creado correctamente.")
                return redirect("dashboard_admin_complemento_roles_sistema")
        else:
            log_complemento_event(
                request=request,
                event="complemento.create",
                complemento_tipo="rol_sistema",
                status="error",
                model_name="RolSistema",
                errors=form.errors.get_json_data(),
            )
    else:
        form = RolSistemaForm()
    items = RolSistema.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/roles-sistema/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Roles de Sistema",
            "description": "Carga los roles de acceso global al sistema.",
            "form": form,
            "items_title": "Roles cargados",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_complemento_roles_sistema_editar(request, rol_id):
    require_admin(request.user)
    rol = get_object_or_404(RolSistema, pk=rol_id)
    if request.method == "POST":
        before = {
            "nombre": rol.nombre,
            "codigo": rol.codigo,
            "descripcion": rol.descripcion,
            "activo": rol.activo,
        }
        form = RolSistemaForm(request.POST, instance=rol)
        if form.is_valid():
            try:
                instance = editar_rol_sistema(
                    rol=rol,
                    nombre=form.cleaned_data["nombre"],
                    codigo=form.cleaned_data.get("codigo"),
                    descripcion=form.cleaned_data.get("descripcion", ""),
                    activo=form.cleaned_data.get("activo", True),
                )
            except ValidationError as exc:
                if hasattr(exc, "message_dict"):
                    for field, field_errors in exc.message_dict.items():
                        for error in field_errors:
                            if field in form.fields:
                                form.add_error(field, error)
                            else:
                                form.add_error(None, error)
                else:
                    form.add_error(None, str(exc))
                log_complemento_event(
                    request=request,
                    event="complemento.update",
                    complemento_tipo="rol_sistema",
                    status="error",
                    model_name="RolSistema",
                    registro_id=rol.pk,
                    before=before,
                    errors=form.errors.get_json_data(),
                )
            else:
                log_complemento_event(
                    request=request,
                    event="complemento.update",
                    complemento_tipo="rol_sistema",
                    status="success",
                    model_name="RolSistema",
                    registro_id=instance.pk,
                    before=before,
                    after=cleaned_data_snapshot(form),
                )
                messages.success(request, "Rol de sistema actualizado correctamente.")
                return redirect("dashboard_admin_complemento_roles_sistema")
        else:
            log_complemento_event(
                request=request,
                event="complemento.update",
                complemento_tipo="rol_sistema",
                status="error",
                model_name="RolSistema",
                registro_id=rol.pk,
                before=before,
                errors=form.errors.get_json_data(),
            )
    else:
        form = RolSistemaForm(instance=rol)

    items = RolSistema.objects.order_by("nombre")
    items_links = [
        {
            "label": str(item),
            "url": f"/dashboard/admin/complementos/roles-sistema/{item.pk}/editar/",
        }
        for item in items
    ]
    return render(
        request,
        "dashboard/admin/complemento_form.html",
        {
            "title": "Editar Rol de Sistema",
            "description": "Modifica un rol existente. No se elimina desde esta pantalla.",
            "form": form,
            "items_title": "Roles cargados",
            "items_links": items_links,
            **admin_context(request.user),
        },
    )


@login_required
def admin_metricas(request):
    require_admin(request.user)
    return render(request, "dashboard/admin/metricas.html", admin_context(request.user))


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
