from django.db import models

# Create your models here.
from django.db import models

class Entreprise(models.Model):
    nom = models.CharField(max_length=255)
    ifu = models.CharField(max_length=20, unique=True)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    site_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nom
