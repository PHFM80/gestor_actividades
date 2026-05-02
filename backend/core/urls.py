from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UsuarioLoginView.as_view(), name='login'),
    path('logout/', views.UsuarioLogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/empresa/<int:empresa_id>/', views.dashboard_select_empresa, name='dashboard_select_empresa'),
    path('dashboard/admin/', include('core.dashboard_urls')),
    path('dashboard/admin/', include('personas.urls')),
    path('dashboard/admin/', include('actividades.urls')),
    path('dashboard/admin/', include('donaciones.urls')),
]
