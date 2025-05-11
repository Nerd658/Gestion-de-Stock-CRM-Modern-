from django.contrib import admin
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'quantite', 'prix', )
    search_fields = ('nom',)  # Permet de rechercher par nom de produit

admin.site.register(Produit, ProduitAdmin)
from django.utils.translation import gettext_lazy as _

# Modifier le titre de l'interface d'administration
admin.site.site_header = _("Tableau de bord ")
