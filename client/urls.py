from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name="home"),
    path('clients/', views.Clients, name="clients")
]
