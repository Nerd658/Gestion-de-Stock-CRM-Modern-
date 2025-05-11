from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Vue pour la gestion des stocks
@login_required 
def gestion_stocks(request):
    return render(request, 'stocks/gestion_stocks.html')
