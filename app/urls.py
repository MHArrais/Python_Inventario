from django.contrib import admin
from django.urls import path, include
from inventario.views import login_view, cadastrar_item, lista_itens, registrar_view, logout_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),
    path('login/', login_view, name='login'),
    path('cadastrar/', cadastrar_item, name='cadastrar_item'),
    path('lista/', lista_itens, name='lista_itens'),
    path('registrar/', registrar_view, name='registrar'),
    path('logout/', logout_login, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

]
