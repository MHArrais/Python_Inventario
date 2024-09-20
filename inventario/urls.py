from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastrar/', views.cadastrar_item, name='cadastrar_item'),
    
]