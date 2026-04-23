from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UsuarioLoginView.as_view(), name='login'),
    path('logout/', views.UsuarioLogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/empresa/<int:empresa_id>/', views.dashboard_select_empresa, name='dashboard_select_empresa'),
    path('dashboard/admin/', views.admin_dashboard, name='dashboard_admin'),
    path('dashboard/admin/complementos/', views.admin_complementos, name='dashboard_admin_complementos'),
    path('dashboard/admin/complementos/paises/', views.admin_complemento_paises, name='dashboard_admin_complemento_paises'),
    path('dashboard/admin/complementos/provincias/', views.admin_complemento_provincias, name='dashboard_admin_complemento_provincias'),
    path('dashboard/admin/complementos/localidades/', views.admin_complemento_localidades, name='dashboard_admin_complemento_localidades'),
]
