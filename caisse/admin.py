from django.contrib import admin
from .models import Facturation, Transaction

@admin.register(Facturation)
class FacturationAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite_vendue', 'date_transaction', 'total', 'transaction')  # Affiche les champs principaux
    search_fields = ('produit__nom',)  # Permet la recherche par nom de produit
    list_filter = ('date_transaction', 'transaction')  # Filtrage par date et transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('payment_number', 'date_transaction', 'prix_total', 'status', 'mode_de_paiement')  # Ajout de mode_de_paiement dans la liste
    search_fields = ('payment_number',)
    list_filter = ('date_transaction', 'status', 'mode_de_paiement')  # Filtrer par mode de paiement également
from django.utils.translation import gettext_lazy as _

# Modifier le titre de l'interface d'administration
admin.site.site_header = _("Tableau de bord ")


