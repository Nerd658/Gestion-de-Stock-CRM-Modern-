"""
URL configuration for gestion_stock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('utilisateurs.urls')),
    path('stocks/', include('stocks.urls')),  # Application des stocks
    path('clients/', include('clients.urls')),  # Application des clients
    path('fournisseur/', include('fournisseur.urls')),  # Application des fournisseurs
    path('ventes/', include('ventes.urls')),  # Application des ventes
    path('caisse/', include('caisse.urls')),  # Application de la caisse
    path('alertes/', include('alertes.urls')),  # Application des alertes
    path('produit/', include('produit.urls')),  # Application des alertes
    path('entreprise/', include('entreprise.urls')),
]
