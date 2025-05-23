# Generated by Django 5.1.2 on 2024-11-01 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("produit", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Facturation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantite_vendue", models.PositiveIntegerField()),
                ("date_transaction", models.DateTimeField(auto_now_add=True)),
                ("prix_total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "produit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produit.produit",
                    ),
                ),
            ],
        ),
    ]
