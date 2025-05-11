from django.shortcuts import render

# Create your views here.
def fournisseurs(request):
    return render(request, 'fournisseur/fournisseurs.html') 


