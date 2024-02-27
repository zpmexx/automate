from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('dodaj/', views.addItem, name="additem"),
    path('test/', views.test, name="test"),
    path('raport/', views.reportView, name="report"),


]

