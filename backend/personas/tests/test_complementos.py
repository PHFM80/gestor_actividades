from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from personas.models import TipoDocumento


class AdminComplementosPersonasTests(TestCase):
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
        response = self.client.get(reverse("dashboard_admin_complemento_tipos_documento"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_usuario_no_admin_recibe_403(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("dashboard_admin_complemento_tipos_documento"))
        self.assertEqual(response.status_code, 403)

    def test_tipos_documento_crear_editar_y_prevenir_duplicados(self):
        self.client.force_login(self.admin)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_tipos_documento"),
            {"nombre": "DNI", "codigo": "DNI"},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        tipo = TipoDocumento.objects.get(nombre="DNI")

        editar = self.client.post(
            reverse("dashboard_admin_complemento_tipos_documento_editar", args=[tipo.pk]),
            {"nombre": "Documento Nacional", "codigo": "DOCNAC"},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        tipo.refresh_from_db()
        self.assertEqual(tipo.nombre, "Documento Nacional")

        TipoDocumento.objects.create(nombre="Pasaporte", codigo="PASS")
        duplicado_nombre = self.client.post(
            reverse("dashboard_admin_complemento_tipos_documento_editar", args=[tipo.pk]),
            {"nombre": "Pasaporte", "codigo": "DOCNAC"},
        )
        self.assertEqual(duplicado_nombre.status_code, 200)
        self.assertContains(duplicado_nombre, "Ya existe un tipo de documento con ese nombre.")

        duplicado_codigo = self.client.post(
            reverse("dashboard_admin_complemento_tipos_documento_editar", args=[tipo.pk]),
            {"nombre": "Documento Nacional", "codigo": "PASS"},
        )
        self.assertEqual(duplicado_codigo.status_code, 200)
        self.assertContains(duplicado_codigo, "Ya existe un tipo de documento con ese codigo.")
