# Generated by Django 5.1.2 on 2024-11-09 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("caisse", "0003_facturation_transaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facturation",
            name="transaction",
        ),
    ]
