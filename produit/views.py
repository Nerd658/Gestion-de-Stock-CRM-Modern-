from django.shortcuts import render 
from django.shortcuts import redirect
from .models import Produit 
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required 
def creer_un_produit(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')
        seuil_alerte = request.POST.get("seuil_alerte")
        prix_achat = request.POST.get("prix_achat")
        
        
        if nom and prix and quantite:
            Produit.objects.create(
                nom=nom,
                description=description,  # Ajout de la description ici
                prix=prix,
                quantite=quantite,
                seuil_alerte=seuil_alerte,
                prix_achat=prix_achat
                
            )
        return redirect('liste_produit')
    
    return render(request, 'produit/creer_produit.html')

@login_required 
def modif_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    
    if request.method == 'POST':
        nom = request.POST.get('nom', produit.nom)  # Utilise la valeur actuelle par défaut
        description = request.POST.get('description', produit.description)  # Idem pour description
        prix = request.POST.get('prix', produit.prix)  # Idem pour prix
        quantite = int(request.POST.get('quantite', produit.quantite))  # Conversion en entier
        seuil_alerte = int(request.POST.get("seuil_alerte", produit.seuil_alerte)) 
        prix_achat = float(request.POST.get("prix_achat", produit.prix_achat)) 
        
        # Mise à jour des attributs du produit
        produit.nom = nom
        produit.description = description
        produit.prix = prix
        produit.quantite = quantite
        produit.seuil_alerte = seuil_alerte
        produit.prix_achat = prix_achat
        
        
        
        produit.save()
        return redirect('liste_produit')
    
    return render(request, 'produit/modif_produit.html', {'produit': produit}) 


@login_required 
def sup_produit(request, produit_id) :
    produit = get_object_or_404(Produit, id=produit_id)
    
    if request.method == 'POST' :
        produit.delete()
        return redirect('liste_produit')
    
    return render(request, 'produit/sup_produit.html', {'produit': produit})




@login_required 
def liste_produit(request):
    produits = Produit.objects.all()  # Récupère tous les produits
    total_produits = produits.count()  # Compte total des produits
    valeur_stock = f"{int(sum([p.quantite * p.prix for p in produits]))}"  # Calcule la valeur du stock
    query = request.GET.get('q')
    
    if query :
        produits = produits.filter(
            Q(nom__icontains=query) |
            Q(description__icontains=query)
        )

    
    for produit in produits :
        produit.prix_total = f"{int(produit.quantite*produit.prix)}"
        
    return render(request, 'produit/liste_produit.html', {
        'produits': produits,
        'total_produits': total_produits,
        'valeur_stock': valeur_stock
    })