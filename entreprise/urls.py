from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.creer_entreprise, name='creer_entreprise'),
    path('afficher/', views.afficher_entreprise, name='afficher_entreprise'),
]
