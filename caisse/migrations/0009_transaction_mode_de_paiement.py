# Generated by Django 5.1.2 on 2024-11-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caisse", "0008_rename_prix_total_facturation_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="mode_de_paiement",
            field=models.CharField(
                choices=[
                    ("ES", "Espèce"),
                    ("LC", "Liquide"),
                    ("CC", "Carte de Crédit"),
                    ("CQ", "Chèque"),
                    ("CT", "Carte de Débit"),
                ],
                default="ES",
                max_length=2,
            ),
        ),
    ]
