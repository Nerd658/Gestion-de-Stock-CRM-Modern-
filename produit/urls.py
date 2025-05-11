from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produit, name='liste_produit'),
    path('produit/creer_un_produit/', views.creer_un_produit, name='creer_un_produit'),
    path('produit/modifier/<int:produit_id>/', views.modif_produit, name='modif_produit'),
    path('produit/supprimer/<int:produit_id>/', views.sup_produit, name='sup_produit'),
]
