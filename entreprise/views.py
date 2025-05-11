
from django.shortcuts import render, redirect
from .models import Entreprise
from .forms import EntrepriseForm

def creer_entreprise(request):
    entreprise = Entreprise.objects.first()
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('afficher_entreprise')
    else:
        form = EntrepriseForm(instance=entreprise)
    return render(request, 'entreprise/creer_entreprise.html', {'form': form})

def afficher_entreprise(request):
    entreprise = Entreprise.objects.first()
    return render(request, 'entreprise/afficher_entreprise.html', {'entreprise': entreprise})
