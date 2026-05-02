from django.urls import path

from actividades import views

urlpatterns = [
    path('actividad/', views.admin_crear_actividad, name='dashboard_admin_actividad'),
    path('complementos/roles-actividad/', views.admin_complemento_roles_actividad, name='dashboard_admin_complemento_roles_actividad'),
    path('complementos/tipos-actividad/', views.admin_complemento_tipos_actividad, name='dashboard_admin_complemento_tipos_actividad'),
]
