from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('dodaj/', views.addItem, name="additem"),

]

