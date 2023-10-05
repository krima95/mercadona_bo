from django.urls import path
from . import views

urlpatterns = [
    # path('', views.products, name='index'),
    path('product/', views.home),
    path('register', views.register),
    path('login', views.my_login),

]
