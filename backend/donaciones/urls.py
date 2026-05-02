from django.urls import path

from donaciones import views

urlpatterns = [
    path('donaciones/', views.admin_donaciones, name='dashboard_admin_donaciones'),
    path('complementos/unidades-medida/', views.admin_complemento_unidades_medida, name='dashboard_admin_complemento_unidades_medida'),
    path('complementos/unidades-medida/<int:unidad_medida_id>/editar/', views.admin_complemento_unidades_medida_editar, name='dashboard_admin_complemento_unidades_medida_editar'),
]
