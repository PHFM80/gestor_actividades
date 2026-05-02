from django.urls import path

from donaciones import views

urlpatterns = [
    path('donaciones/', views.admin_donaciones, name='dashboard_admin_donaciones'),
    path('complementos/unidades-medida/', views.admin_complemento_unidades_medida, name='dashboard_admin_complemento_unidades_medida'),
]
