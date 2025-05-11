from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_stocks, name='gestion_stocks'),
]
