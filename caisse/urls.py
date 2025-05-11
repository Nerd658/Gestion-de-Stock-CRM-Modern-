from django.urls import path
from . import views

urlpatterns = [
    path('', views.ajouter_transaction, name='ajouter_transaction'),
]
