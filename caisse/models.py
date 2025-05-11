from django.db import models
from produit.models import Produit

class Transaction(models.Model):
    MODE_DE_PAIEMENT_CHOICES = [
        ('ES', 'Espèce'),
        ('LC', 'Liquide'),
        ('CC', 'Carte de Crédit'),
        ('CQ', 'Chèque'),
        ('CT', 'Carte de Débit'),
    ]
    payment_number = models.AutoField(primary_key=True)
    date_transaction = models.DateTimeField(auto_now_add=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    mode_de_paiement = models.CharField(
        max_length=2,  # La longueur de la valeur de mode de paiement (choix abrégés)
        choices=MODE_DE_PAIEMENT_CHOICES,  # Liste des choix de paiement
        default='ES'  # Par défaut, le mode de paiement est 'Espèce'
    )
    
    def __str__(self):
        return f"Transaction {self.payment_number} - {self.prix_total} - {self.status} - {self.get_mode_de_paiement_display()}"

class Facturation(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_vendue = models.PositiveIntegerField()
    date_transaction = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='facturations')  # Clé étrangère vers Transaction
    
    def save(self, *args, **kwargs):
        # Calculer le prix automatiquement
        self.total = self.quantite_vendue * self.produit.prix
        # Mettre à jour le stock du produit
        self.produit.quantite -= self.quantite_vendue
        self.produit.save()
        super().save(*args, **kwargs)
        
        
    def calculer_benefice_total(self): 
        return (self.produit.prix - self.produit.prix_achat) * self.quantite_vendue # Méthode pour calculer le bénéfice total de la facturation
    
    
    def __str__(self):
        return f"Transaction de {self.quantite_vendue} {self.produit.nom}"
    
    

    