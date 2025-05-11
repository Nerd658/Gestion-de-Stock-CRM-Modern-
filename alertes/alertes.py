from django.utils import timezone
from .models import Alerte
from produit.models import Produit

def verifier_et_creer_alerte(produit):
    if produit.quantite < produit.seuil_alerte:
        # Créer ou mettre à jour une alerte si le stock est en dessous du seuil
        alerte, created = Alerte.objects.get_or_create(
            produit=produit,
            defaults={'message': f"Le stock de {produit.nom} est inférieur au seuil d'alerte.",
                      'quantite_restante': produit.quantite}
        )
        if not created:
            alerte.quantite_restante = produit.quantite  # Mettre à jour la quantité restante
            alerte.save()
    else:
        # Supprimer les alertes si le stock est suffisant
        Alerte.objects.filter(produit=produit).delete()
