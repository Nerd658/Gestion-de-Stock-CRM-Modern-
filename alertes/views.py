from django.shortcuts import render
from .models import Alerte
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required 
def alertes(request):
    alertes = Alerte.objects.all().order_by('-date_alerte')
    alerte_count = Alerte.objects.count()
    try:  
        dernier_alerte = Alerte.objects.latest('date_alerte')
    except Alerte.DoesNotExist :
        dernier_alerte = None
    return render(request, 'alertes/alertes.html', {'alertes': alertes, "alerte_count" :alerte_count, "dernier_alerte" : dernier_alerte})