from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.loginView, name="login"),
    path('zaloguj/', views.loginView, name="login"),
   path('wyloguj/', views.logoutView, name="logout"),

]

