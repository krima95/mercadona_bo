from django.urls import path
from . import views

# app_name = "products"

urlpatterns = [
    path('', views.home, name=""),  # /index.html

    path('register', views.register, name="register"),  # créer un compte

    path('login', views.login, name="login"),  # ecran de connexion

    path('dashboard', views.dashboard, name="dashboard"),  # tableau de bord

    path('user-logout', views.user_logout, name="logout"),

]
