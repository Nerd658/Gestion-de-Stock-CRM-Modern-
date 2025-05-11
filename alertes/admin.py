from django.contrib import admin

# Register your models here.
from alertes.models import Alerte

admin.site.register(Alerte)

from django.utils.translation import gettext_lazy as _

# Modifier le titre de l'interface d'administration
admin.site.site_header = _("Tableau de bord ")