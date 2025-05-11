from django.shortcuts import render
from django.utils import timezone
from caisse.models import Transaction
from alertes.models import Alerte
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.db.models import Sum

@login_required 
def dashboard(request):
    today = timezone.now().date()
    sales_data = []
    labels = []
    transaction_counts = []

    for i in range(7):
        day = today - timezone.timedelta(days=i)
        total_sales = Transaction.objects.filter(date_transaction__date=day).aggregate(total=Sum('prix_total'))['total'] or 0
        total_transaction = Transaction.objects.filter(date_transaction__date=day).count()
        sales_data.append(float(total_sales))
        transaction_counts.append(total_transaction)
        labels.append(day.strftime('%A'))  # Nom du jour

    sales_data.reverse()
    labels.reverse()
    transaction_counts.reverse()
    # Récupérer les transactions depuis la base de données
    transactions = Transaction.objects.all().order_by('-date_transaction')[:5]  # Limiter à 5 transactions

    # Calculer le montant total des transactions pour aujourd'hui
    
    current_date = timezone.now()
    today = timezone.now().date() 
    daily_transactions = Transaction.objects.filter(date_transaction__date=today)
    monthly_transactions = Transaction.objects.filter(date_transaction__year=current_date.year , date_transaction__month=current_date.month)
    monthly_total = sum(transaction.prix_total for transaction in monthly_transactions)
    daily_total = sum(transaction.prix_total for transaction in daily_transactions)
    daily_count = daily_transactions.count()
    alerte_count = Alerte.objects.count()
    
    
    today = timezone.now().date()
    current_date = timezone.now()
    transactions_today = Transaction.objects.filter(date_transaction__date=today)
    benefice_journalier = 0
    for transaction in transactions_today:
        facturations = transaction.facturations.all()
        benefice_transaction = sum(facturation.calculer_benefice_total() for facturation in facturations)
        benefice_journalier += benefice_transaction

    return render(request, 'utilisateurs/dashboard.html', {
        'transactions': transactions,
        'daily_total': daily_total or 0,
        "daily_count" :daily_count,
        "monthly_total" :monthly_total or 0,
        "alerte_count" : alerte_count,
        'sales_data': sales_data,
        'labels': labels,
        'transaction_counts': transaction_counts, 
        'benefice_journalier' : benefice_journalier,
    })





class CustomLoginView(LoginView):
    template_name = 'utilisateurs/connexion.html'  # Chemin vers le template personnalisé
    redirect_authenticated_user = True  # Redirige si l'utilisateur est déjà connecté
    next_page = reverse_lazy('dashboard')  # Redirection après connexion réussie


def custom_logout_view(request):
    # Déconnexion immédiate sans confirmation
    logout(request)
    return redirect(reverse('login'))  # Redirige vers la page de connexion après la déconnexion
