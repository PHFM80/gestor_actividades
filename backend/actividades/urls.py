from django.urls import path

from actividades import views

urlpatterns = [
    path('actividad/', views.admin_crear_actividad, name='dashboard_admin_actividad'),
    path('complementos/roles-actividad/', views.admin_complemento_roles_actividad, name='dashboard_admin_complemento_roles_actividad'),
    path('complementos/roles-actividad/<int:rol_actividad_id>/editar/', views.admin_complemento_roles_actividad_editar, name='dashboard_admin_complemento_roles_actividad_editar'),
    path('complementos/tipos-actividad/', views.admin_complemento_tipos_actividad, name='dashboard_admin_complemento_tipos_actividad'),
    path('complementos/tipos-actividad/<int:tipo_actividad_id>/editar/', views.admin_complemento_tipos_actividad_editar, name='dashboard_admin_complemento_tipos_actividad_editar'),
]
