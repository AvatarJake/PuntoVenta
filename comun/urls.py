from django.urls import path
from django.contrib.auth import views as auth_views

from comun.views import Home, Informes, Informe_Productos, Informe_Compras, Informe_Ventas


urlpatterns = [
	path('',Home.as_view(), name='home'),
	path('base/informes',Informes.as_view(), name='informes'),
	path('base/imprimir_productos',Informe_Productos.as_view(), name='listado'),
	path('base/imprimir_compras',Informe_Compras.as_view(), name='listado_compras'),
	path('base/imprimir_ventas',Informe_Ventas.as_view(), name='listado_ventas'),

	
	#path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),
	#	name='login'),
	#path('logout/',auth_views.LogoutView.as_view(template_name='bases/login.html'),
	#	name='logout'),
]