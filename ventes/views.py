from django.shortcuts import render
from produit.models import Produit
from caisse.models import Facturation, Transaction
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def ventes(request):
    produits = Produit.objects.all()
    benefices = []
    benefice_total_ventes = 0
    chiffre_affaires_total = 0

    facturations = Facturation.objects.select_related('produit').all()
    for produit in produits:
        benefice = produit.calculer_benefice()
        benefices.append({
            'nom': produit.nom,
            'prix': produit.prix,
            'prix_achat': produit.prix_achat,
            'benefice': benefice
        })
    for facturation in facturations:
        benefice_total_ventes += float(facturation.calculer_benefice_total())
        
    transactions = Transaction.objects.all()
    for transaction in transactions:
        chiffre_affaires_total += float(transaction.prix_total)

    # Récupérer les 5 dernières transactions
    dernieres_transactions = Transaction.objects.all().order_by('-date_transaction')[:5]

    # Calculer le bénéfice de chaque transaction
    transactions_with_benefice = []
    for transaction in dernieres_transactions:
        facturations = transaction.facturations.all()
        benefice_transaction = sum(facturation.calculer_benefice_total() for facturation in facturations)
        transactions_with_benefice.append({
            'payment_number': transaction.payment_number,
            'date_transaction': transaction.date_transaction,
            'prix_total': transaction.prix_total,
            'benefice': benefice_transaction,
            'status': transaction.status,
           
        })
    
    today = timezone.now().date()
    current_date = timezone.now()
    transactions_today = Transaction.objects.filter(date_transaction__date=today)
    transactions_month = Transaction.objects.filter(date_transaction__month=current_date.month)

    benefice_journalier = 0
    for transaction in transactions_today:
        facturations = transaction.facturations.all()
        benefice_transaction = sum(facturation.calculer_benefice_total() for facturation in facturations)
        benefice_journalier += benefice_transaction
        
    benefice_mensuelle = 0
    for transaction in transactions_month:
        facturations = transaction.facturations.all()
        benefice_transaction = sum(facturation.calculer_benefice_total() for facturation in facturations)
        benefice_mensuelle += benefice_transaction

    
    labels = []          # Liste pour stocker les dates des 7 derniers jours
    sales_data = []      # Liste pour stocker les ventes totales par jour
    benefice_data = []   # Liste pour stocker les bénéfices totaux par jour
    today = timezone.now().date()

    for i in range(7):  # Boucle sur les 7 derniers jours
        # Calculer la date du jour en cours (i jours avant aujourd'hui)
        day = today - timedelta(days=i)
        # Ajouter la date formatée au format 'YYYY-MM-DD' à la liste labels
        labels.append(day.strftime('%Y-%m-%d'))
        
        # Filtrer les transactions du jour
        transactions_day = Transaction.objects.filter(date_transaction__date=day)
        
        # Calculer les ventes du jour
        sales_day = sum(
            float(transaction.prix_total) for transaction in transactions_day
        )
        
        # Calculer les bénéfices du jour
        benefice_day = sum(
            sum(float(
                facturation.calculer_benefice_total())
                for facturation in transaction.facturations.all()
            ) for transaction in transactions_day
        )
        
        # Ajouter les ventes et bénéfices du jour aux listes respectives
        sales_data.append(sales_day)
        benefice_data.append(benefice_day)

    # Inverser l'ordre des listes pour avoir les jours du plus ancien au plus récent
    labels.reverse()
    sales_data.reverse()
    benefice_data.reverse()

    return render(request, 'ventes/ventes.html', {
        'benefices': benefices,
        'benefice_total_ventes': benefice_total_ventes,
        'chiffre_affaires_total': chiffre_affaires_total,
        'transactions': transactions_with_benefice,
        'benefice_journalier' : benefice_journalier,
        'sales_data': sales_data,
        'benefice_data': benefice_data,
        'labels': labels,
        'benefice_mensuelle' : benefice_mensuelle
    })
    
    

