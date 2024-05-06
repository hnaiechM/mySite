#from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from .models import Produit
from django.shortcuts import render, redirect
from .forms import FournisseurForm
from django.shortcuts import render, HttpResponseRedirect
from .models import Produit
from .forms import ProduitForm 
from .forms import CommandeForm 
from .models import Fournisseur
from .models import Commande
from django.contrib.auth.decorators import login_required
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login
@login_required
def home(request):
  products= Produit.objects.all()
  context={'products':products}
  return render( request,'magasin/mesProduits.html ',context )

def listProduit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide
    return render(request, 'magasin/majProduits.html', {'form': form})

def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})

def acceuil(request):
    return render(request,'acceuil.html' )

def nouveauFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = FournisseurForm()
        fournisseurs = Fournisseur.objects.all()
        return render(request, 'magasin/fournisseur.html', {'form': form, 'fournisseurs': fournisseurs})
    #return render(request, 'magasin/fournisseur.html', {'form': form})

def nouveauCommande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/nouvCommande/')  # Rediriger vers la page de création après soumission réussie
    else:
        form = CommandeForm()

    commandes = Commande.objects.all()
    return render(request, 'magasin/nouvelleCommande.html', {'form': form, 'commandes': commandes})

def login(request) :
    #Teste si le formulaire a été envoyé
    if request .method=="POST" :
        form = AuthenticationForm(request .POST)
        if form . is_valid() :
            user_email = form.cleaned_data['email']
            logged_user = User.objects.get(courriel=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect ('/index')
        else:
            form = AuthenticationForm()
    return render('registration/login.html ' , {'form' : form})

def logout_view(request):
   logout(request)


def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
    else :
        form = UserRegistrationForm()
        return render(request,'registration/register.html',{'form' : form})