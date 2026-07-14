import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from donaciones.models import UnidadMedida


class AdminComplementosDonacionesTests(TestCase):
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
        response = self.client.get(reverse("dashboard_admin_complemento_unidades_medida"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_usuario_no_admin_recibe_403(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("dashboard_admin_complemento_unidades_medida"))
        self.assertEqual(response.status_code, 403)

    def test_unidades_medida_crear_editar_y_prevenir_duplicado(self):
        self.client.force_login(self.admin)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_unidades_medida"),
            {"nombre": "Kilogramo"},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        unidad = UnidadMedida.objects.get(nombre="Kilogramo")

        editar = self.client.post(
            reverse("dashboard_admin_complemento_unidades_medida_editar", args=[unidad.pk]),
            {"nombre": "Kilogramo Neto"},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        unidad.refresh_from_db()
        self.assertEqual(unidad.nombre, "Kilogramo Neto")

        UnidadMedida.objects.create(nombre="Litro")
        duplicado = self.client.post(
            reverse("dashboard_admin_complemento_unidades_medida_editar", args=[unidad.pk]),
            {"nombre": "Litro"},
        )
        self.assertEqual(duplicado.status_code, 200)
        self.assertContains(duplicado, "Ya existe una unidad de medida con ese nombre.")

    def test_auditoria_log_en_unidad_medida_update(self):
        self.client.force_login(self.admin)
        unidad = UnidadMedida.objects.create(nombre="Bolsa")
        with self.assertLogs("complementos_audit", level="INFO") as cm:
            self.client.post(
                reverse("dashboard_admin_complemento_unidades_medida_editar", args=[unidad.pk]),
                {"nombre": "Bolsa Grande"},
            )
        payload = json.loads(cm.output[-1].split("INFO:complementos_audit:")[1])
        self.assertEqual(payload["complemento_tipo"], "unidad_medida")
        self.assertEqual(payload["event"], "complemento.update")
        self.assertEqual(payload["estado"], "success")
