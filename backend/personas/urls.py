from django.urls import path

from personas import views

urlpatterns = [
    path('personas/', views.admin_cargar_personas, name='dashboard_admin_personas'),
    path('usuarios/', views.admin_cargar_usuarios, name='dashboard_admin_usuarios'),
    path('complementos/tipos-documento/', views.admin_complemento_tipos_documento, name='dashboard_admin_complemento_tipos_documento'),
]
