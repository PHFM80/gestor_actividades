import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from core.models import RolSistema
from geo.models import Localidad, Pais, Provincia


class AdminComplementosCoreTests(TestCase):
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

    def test_requiere_login_en_complementos_core(self):
        response = self.client.get(reverse("dashboard_admin_complemento_paises"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_usuario_no_admin_recibe_403(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("dashboard_admin_complemento_paises"))
        self.assertEqual(response.status_code, 403)

    def test_paises_crear_editar_y_prevenir_duplicado(self):
        self.client.force_login(self.admin)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_paises"),
            {"nombre": "Argentina", "codigo": "AR"},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        pais = Pais.objects.get(nombre="Argentina")
        self.assertEqual(pais.codigo, "AR")

        editar = self.client.post(
            reverse("dashboard_admin_complemento_paises_editar", args=[pais.pk]),
            {"nombre": "Argentina Federal", "codigo": "ARF"},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        pais.refresh_from_db()
        self.assertEqual(pais.nombre, "Argentina Federal")

        self.client.post(reverse("dashboard_admin_complemento_paises"), {"nombre": "Chile", "codigo": "CL"})
        duplicado = self.client.post(
            reverse("dashboard_admin_complemento_paises_editar", args=[pais.pk]),
            {"nombre": "Chile", "codigo": "ARF"},
        )
        self.assertEqual(duplicado.status_code, 200)
        self.assertContains(duplicado, "Ya existe un pais con ese nombre.")

    def test_provincias_crear_editar_y_prevenir_duplicado_por_pais(self):
        self.client.force_login(self.admin)
        pais = Pais.objects.create(nombre="Argentina Test Provincias", codigo="AR-P")

        crear = self.client.post(
            reverse("dashboard_admin_complemento_provincias"),
            {"nombre": "Cordoba", "pais": pais.pk},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        provincia = Provincia.objects.get(nombre="Cordoba", pais=pais)

        editar = self.client.post(
            reverse("dashboard_admin_complemento_provincias_editar", args=[provincia.pk]),
            {"nombre": "Córdoba", "pais": pais.pk},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        provincia.refresh_from_db()
        self.assertEqual(provincia.nombre, "Córdoba")

        Provincia.objects.create(nombre="Mendoza", pais=pais)
        duplicado = self.client.post(
            reverse("dashboard_admin_complemento_provincias_editar", args=[provincia.pk]),
            {"nombre": "Mendoza", "pais": pais.pk},
        )
        self.assertEqual(duplicado.status_code, 200)
        self.assertContains(duplicado, "Ya existe una provincia con ese nombre en el pais seleccionado.")

    def test_localidades_crear_editar_y_prevenir_duplicado_por_provincia(self):
        self.client.force_login(self.admin)
        pais = Pais.objects.create(nombre="Argentina Test Localidades", codigo="AR-L")
        provincia = Provincia.objects.create(nombre="Buenos Aires", pais=pais)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_localidades"),
            {"nombre": "La Plata", "provincia": provincia.pk},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        localidad = Localidad.objects.get(nombre="La Plata", provincia=provincia)

        editar = self.client.post(
            reverse("dashboard_admin_complemento_localidades_editar", args=[localidad.pk]),
            {"nombre": "La Plata Centro", "provincia": provincia.pk},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        localidad.refresh_from_db()
        self.assertEqual(localidad.nombre, "La Plata Centro")

        Localidad.objects.create(nombre="Quilmes", provincia=provincia)
        duplicado = self.client.post(
            reverse("dashboard_admin_complemento_localidades_editar", args=[localidad.pk]),
            {"nombre": "Quilmes", "provincia": provincia.pk},
        )
        self.assertEqual(duplicado.status_code, 200)
        self.assertContains(duplicado, "Ya existe una localidad con ese nombre en la provincia seleccionada.")

    def test_roles_sistema_crear_editar_y_codigo_automatico(self):
        self.client.force_login(self.admin)

        crear = self.client.post(
            reverse("dashboard_admin_complemento_roles_sistema"),
            {"nombre": "Operador General", "codigo": "", "descripcion": "desc", "activo": "on"},
            follow=True,
        )
        self.assertEqual(crear.status_code, 200)
        rol = RolSistema.objects.get(nombre="Operador General")
        self.assertEqual(rol.codigo, "OPERADOR_GENERAL")

        editar = self.client.post(
            reverse("dashboard_admin_complemento_roles_sistema_editar", args=[rol.pk]),
            {"nombre": "Operador Senior", "codigo": "ops sr", "descripcion": "editado", "activo": "on"},
            follow=True,
        )
        self.assertEqual(editar.status_code, 200)
        rol.refresh_from_db()
        self.assertEqual(rol.nombre, "Operador Senior")
        self.assertEqual(rol.codigo, "OPS_SR")

    def test_complementos_no_exponen_eliminacion_en_pantallas(self):
        self.client.force_login(self.admin)
        pais = Pais.objects.create(nombre="Argentina Test Edicion", codigo="AR-E")

        response_listado = self.client.get(reverse("dashboard_admin_complemento_paises"))
        self.assertEqual(response_listado.status_code, 200)
        self.assertNotContains(response_listado, ">Eliminar<", html=False)

        response_edicion = self.client.get(reverse("dashboard_admin_complemento_paises_editar", args=[pais.pk]))
        self.assertEqual(response_edicion.status_code, 200)
        self.assertNotContains(response_edicion, ">Eliminar<", html=False)

    def test_auditoria_log_create_y_error(self):
        self.client.force_login(self.admin)

        with self.assertLogs("complementos_audit", level="INFO") as cm:
            self.client.post(reverse("dashboard_admin_complemento_paises"), {"nombre": "Uruguay", "codigo": "UY"})
        payload_ok = json.loads(cm.output[-1].split("INFO:complementos_audit:")[1])
        self.assertEqual(payload_ok["event"], "complemento.create")
        self.assertEqual(payload_ok["complemento_tipo"], "pais")
        self.assertEqual(payload_ok["estado"], "success")

        Pais.objects.create(nombre="Paraguay", codigo="PY")
        with self.assertLogs("complementos_audit", level="INFO") as cm_error:
            self.client.post(reverse("dashboard_admin_complemento_paises"), {"nombre": "Paraguay", "codigo": "PYA"})
        payload_error = json.loads(cm_error.output[-1].split("INFO:complementos_audit:")[1])
        self.assertEqual(payload_error["estado"], "error")
        self.assertTrue(payload_error["errores"])

    def test_auditoria_log_update_y_diff(self):
        self.client.force_login(self.admin)
        pais = Pais.objects.create(nombre="Brasil", codigo="BR")
        with self.assertLogs("complementos_audit", level="INFO") as cm:
            self.client.post(
                reverse("dashboard_admin_complemento_paises_editar", args=[pais.pk]),
                {"nombre": "Brasil Federal", "codigo": "BRF"},
            )
        payload = json.loads(cm.output[-1].split("INFO:complementos_audit:")[1])
        self.assertEqual(payload["event"], "complemento.update")
        self.assertEqual(payload["estado"], "success")
        self.assertIn("nombre", payload["cambios"])
