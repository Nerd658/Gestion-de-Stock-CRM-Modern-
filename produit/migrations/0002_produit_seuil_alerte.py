# Generated by Django 5.1.2 on 2024-11-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produit", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produit",
            name="seuil_alerte",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
