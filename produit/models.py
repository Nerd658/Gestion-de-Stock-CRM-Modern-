from django.db import models
from django.utils import timezone


# Create your models here.

class Produit(models.Model) :
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True , blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Nouveau champ pour le prix d'achat
    quantite = models.PositiveIntegerField()
    date_ajout = models.DateTimeField(default=timezone.now)
    seuil_alerte = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from alertes.alertes import verifier_et_creer_alerte  # Import différé
        verifier_et_creer_alerte(self)
        
    def calculer_benefice(self): 
        return self.prix - self.prix_achat
    
    def __str__(self):
        return self.nom

    
    
