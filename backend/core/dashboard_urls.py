from django.urls import path

from core import views

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard_admin'),
    path('metricas/', views.admin_metricas, name='dashboard_admin_metricas'),
    path('complementos/', views.admin_complementos, name='dashboard_admin_complementos'),
    path('complementos/roles-sistema/', views.admin_complemento_roles_sistema, name='dashboard_admin_complemento_roles_sistema'),
    path('complementos/roles-sistema/<int:rol_id>/editar/', views.admin_complemento_roles_sistema_editar, name='dashboard_admin_complemento_roles_sistema_editar'),
    path('complementos/paises/', views.admin_complemento_paises, name='dashboard_admin_complemento_paises'),
    path('complementos/paises/<int:pais_id>/editar/', views.admin_complemento_paises_editar, name='dashboard_admin_complemento_paises_editar'),
    path('complementos/provincias/', views.admin_complemento_provincias, name='dashboard_admin_complemento_provincias'),
    path('complementos/provincias/<int:provincia_id>/editar/', views.admin_complemento_provincias_editar, name='dashboard_admin_complemento_provincias_editar'),
    path('complementos/localidades/', views.admin_complemento_localidades, name='dashboard_admin_complemento_localidades'),
    path('complementos/localidades/<int:localidad_id>/editar/', views.admin_complemento_localidades_editar, name='dashboard_admin_complemento_localidades_editar'),
]
