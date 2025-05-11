from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventes, name='ventes'),
    # path('afficher-benefices/', views.afficher_benefices, name='afficher_benefices'),
]
