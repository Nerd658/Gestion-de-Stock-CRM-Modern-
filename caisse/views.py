from django.http import JsonResponse
from django.shortcuts import render
from .models import Produit, Facturation, Transaction
import json
from django.contrib.auth.decorators import login_required
@login_required 
def ajouter_transaction(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire sous forme de JSON
        data = json.loads(request.body)
        cart_items = data.get('cart', [])  # Liste des éléments du panier
        total_amount = data.get('totalAmount', 0)  # Montant total envoyé par le script JS
        methode_paiement = data.get('methodePaiement', 'ES')  # Mode de paiement envoyé par le script JS (par défaut 'ES')
        success = True  # Indicateur de succès
        messages_list = []  # Liste des messages pour les retours

        # Créer une nouvelle transaction
        new_transaction = Transaction(
            prix_total=total_amount,
            mode_de_paiement=methode_paiement,  # Ajout du mode de paiement à la transaction
            status=True  # Ou définir le statut en fonction de votre logique
        )
        new_transaction.save()  # Sauvegarde initiale de la transaction

        # Processus de sauvegarde des transactions
        for item in cart_items:
            try:
                produit = Produit.objects.get(id=item['produit_id'])  # Récupérer le produit par son ID
                quantite_vendue = item['quantite_vendue']  # Quantité vendue

                if produit.quantite >= quantite_vendue:
                    # Créer la facturation liée à la transaction
                    facturation = Facturation(
                        produit=produit,
                        quantite_vendue=quantite_vendue,
                        transaction=new_transaction  # Lier à la nouvelle transaction
                    )
                    facturation.save()  # Cela mettra à jour le prix total et le stock automatiquement
                    messages_list.append(f"Transaction pour le produit {produit.nom} ajoutée avec succès.")
                else:
                    success = False
                    messages_list.append(f"Stock insuffisant pour le produit {produit.nom}.")
            except Produit.DoesNotExist:
                success = False
                messages_list.append("Produit non trouvé.")
            except KeyError as e:
                success = False
                messages_list.append(f"Clé manquante dans l'élément du panier: {str(e)}")

        # Si toutes les transactions sont réussies
        if success:
            return JsonResponse({"success": True, "message": "Facture validée et transactions ajoutées avec succès!"}, status=200)
        else:
            new_transaction.delete()  # Supprimer la transaction si une erreur se produit
            return JsonResponse({"success": False, "message": "Erreur lors de la validation de la facture.", "details": messages_list}, status=400)
    
    # Pour les requêtes GET, afficher le formulaire
    produits = Produit.objects.all()  # Récupérer tous les produits
    mode_de_paiement_choices = dict(Transaction.MODE_DE_PAIEMENT_CHOICES) # Récupérer les choix de paiement disponibles
    print(mode_de_paiement_choices)

    return render(request, 'caisse/ajouter_transaction.html', {
        'produits': produits,
        'mode_de_paiement_choices': mode_de_paiement_choices  # Passer les choix de paiement au template
    })
