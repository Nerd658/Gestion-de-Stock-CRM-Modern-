from django.db import models
from produit.models import Produit

class Alerte(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='alertes')
    date_alerte = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)   
    quantite_restante = models.PositiveIntegerField()

    def __str__(self):
        return f"Alerte pour {self.produit.nom} - {self.date_alerte}"
