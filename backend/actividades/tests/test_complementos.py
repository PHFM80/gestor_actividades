from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from actividades.models import RolActividad, TipoActividad


class AdminComplementosActividadesTests(TestCase):
    def setUp(self):
        self.admin = self._crear_usuario(is_staff=True)
        self.user = self._crear_usuario(email="user@example.com", dni="200", telefono="200")

    def _crear_usuario(self, **overrides):
        data = {
            "email": "admin@example.com",
            "password": "Pass1234!",
            "nombre": "Admin",
            "apellido": "User",
            "dni": "100",
            "telefono": "100",
            "is_staff": False,
            "is_superuser": False,
        }
        data.update(overrides)
        password = data.pop("password")
        return get_user_model().objects.create_user(password=password, **data)

    def test_requiere_login(self):
        response = self.client.get(reverse("dashboard_admin_complemento_roles_actividad"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_usuario_no_admin_recibe_403(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("dashboard_admin_complemento_roles_actividad"))
        self.assertEqual(response.status_code, 403)

    def test_roles_actividad_crear_editar_y_prevenir_duplicado(self):
        self.client.force_login(self.admin)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_roles_actividad"),
            {"nombre": "Coordinador", "descripcion": "coordina"},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        rol = RolActividad.objects.get(nombre="Coordinador")

        editar = self.client.post(
            reverse("dashboard_admin_complemento_roles_actividad_editar", args=[rol.pk]),
            {"nombre": "Coordinador General", "descripcion": "coordina todo"},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        rol.refresh_from_db()
        self.assertEqual(rol.nombre, "Coordinador General")

        RolActividad.objects.create(nombre="Asistente", descripcion="asiste")
        duplicado = self.client.post(
            reverse("dashboard_admin_complemento_roles_actividad_editar", args=[rol.pk]),
            {"nombre": "Asistente", "descripcion": "dup"},
        )
        self.assertEqual(duplicado.status_code, 200)
        self.assertContains(duplicado, "Ya existe un rol de actividad con ese nombre.")

    def test_tipos_actividad_crear_editar_y_prevenir_duplicado(self):
        self.client.force_login(self.admin)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_tipos_actividad"),
            {"nombre": "Capacitacion", "descripcion": "formacion"},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        tipo = TipoActividad.objects.get(nombre="Capacitacion")

        editar = self.client.post(
            reverse("dashboard_admin_complemento_tipos_actividad_editar", args=[tipo.pk]),
            {"nombre": "Capacitación Técnica", "descripcion": "formacion tecnica"},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        tipo.refresh_from_db()
        self.assertEqual(tipo.nombre, "Capacitación Técnica")

        TipoActividad.objects.create(nombre="Voluntariado", descripcion="acciones")
        duplicado = self.client.post(
            reverse("dashboard_admin_complemento_tipos_actividad_editar", args=[tipo.pk]),
            {"nombre": "Voluntariado", "descripcion": "dup"},
        )
        self.assertEqual(duplicado.status_code, 200)
        self.assertContains(duplicado, "Ya existe un tipo de actividad con ese nombre.")
