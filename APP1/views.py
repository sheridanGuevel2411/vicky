from itertools import product
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from APP1.models import Produit, Stock,Vente
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import stockForm,approForm,venteForm
from django.db.models import F
from django.db import models
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
@login_required(login_url='logine')
def Index(request):
    emp = User.objects.all()
    context = {'emp':emp}
    return render(request, 'index.html', context)


def Ajout(request):
    if request.method == "POST":
        data = request.POST
        if data.get('password') == data.get('password1'):
            toto = User.objects.create_user(username = data.get('username'), email = data.get('email'), password = data.get('password'))
            toto.save()
            return redirect('pers')
        else:
            return redirect('pers')    
    return render(request,"pesonnel.html")

def Edit(request):
    emp = User.objects.all()
    context = {'emp':emp}
    return render(request, 'personnel.html', context)
    

def Update(request,id):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        Password = request.POST.get('pasword')
        emp = User (id = id, nom = nom, email = email, Password= Password) 
        emp.save()
        return redirect('pers') 
    return render(request, 'personnel.html')

def Delete(request,id):
    emp = User.objects.filtrer(id = id).delete()
    context = {'emp':emp,}
    return redirect(request, 'personnel.html', context)

def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('logine') 
    return render(request, 'login.html')

def création(request):
    if request.method == "POST":
        data = request.POST
        if data.get('password') == data.get('password1'):
            toto = User.objects.create_user(username = data.get('username'), email = data.get('email'), password = data.get('password'))
            toto.save()
            return redirect('logine')
        else:
            return redirect('création')    
    return render(request,"création.html")

def deconnexion(request):
    logout(request)
    return redirect('logine')


#foction table stock



#foction table produit

#def Ajoutproduit(request):
 #   if request.method == "POST":
 #       nom_produit  = request.POST.get('nom_produit')
  #      description = request.POST.get('description')
   #     prix_unitaire= request.POST.get('date_expiration')
    #    pr = Produit(nom_produit = nom_produit, description = description, prix_unitaire= prix_unitaire) 
     #   pr.save()
      #  return redirect('ADDproduit')
    #return render(request,'create_produit.html')s

#foncction table produit pour faire l'approvisionnement



def Editp(request):
    form = Produit.objects.all()
    context = {'form':form}
    return render(request, 'produit.html', context)

#page personnel

def personnel(request):
    emp = User.objects.all()
    context = {'emp':emp}
    return render(request, 'personnel.html', context)



def Editst(request):
    form = Stock.objects.all()
    context = {'form':form}
    return render(request, 'stock.html', context)



# fonction d'ajout et affichage du stock.
def add_stock(request):
    if request.method == 'POST':
        fm = stockForm(request.POST)
        if fm.is_valid():
           ab = fm.cleaned_data['produit']
           cd = fm.cleaned_data['quantite_disponible']
           ef = fm.cleaned_data['date_expiration']
           reg = Stock(produit=ab, quantite_disponible =cd,date_expiration =ef)
           reg.save()
           fm = stockForm()   
    else:
        fm = stockForm()  
    stoc = Stock.objects.all() 
    return render(request, 'stock.html', {'form':fm, 'sto':stoc})

# fonction d'ajout et affichage de l'approvisionnement.
def add_appro(request):
    if request.method == 'POST':
        fm = approForm(request.POST)
        if fm.is_valid():
           np = fm.cleaned_data['produit']
           ds = fm.cleaned_data['description']
           pu = fm.cleaned_data['prix_unitaire']
           reg = Produit(produit=np, description =ds, prix_unitaire =pu)
           reg.save()
           fm = approForm()   
    else:
        fm = approForm()  
    pro = Produit.objects.all() 
    return render(request, 'produit.html', {'form':fm, 'prod':pro})

# Fonction pour la suppression
def delete_prod(request,id):
    if request.method == 'POST':
        produit=Produit.objects.get(pk=id)
        produit.delete()
        return redirect('/ajoutpro/')
        






# fonction de vente.

def add_vente(request):
    if request.method == 'POST':
        fm = venteForm(request.POST)
        if fm.is_valid():
           np = fm.cleaned_data['produit']
           us = fm.cleaned_data['username']
           at = fm.cleaned_data['quantite_vendue']
           dv = fm.cleaned_data['date_vente']
           tt = fm.cleaned_data['montant_total']
           reg = Vente(produit=np, username =us, quantite_vendue =at,date_vente=dv,montant_total=tt)
           reg.save()
           fm = venteForm()   
    else:
        fm = venteForm()  
    vent = Vente.objects.all() 
    return render(request, 'vente.html', {'form':fm, 'ven':vent})


# fonction d'ajout  vente.



# Modification approvisionnement


def update(request,pk):
    data=Produit.objects.get(pk=pk)
    if request.method=="POST":
        toto=request.POST
        data.produit=toto.get('produit')
        data.description=toto.get('description')
        data.prix_unitaire=toto.get('prix_unitaire')
        data.save()
        return redirect('/ajoutpro/')
    return render(request,'updateappro.html',{'data':data})
# Modification vente

#    return render(request,'updatevente.html',{'data':data})


# Modification stock


#ajouter une vente
def modifier_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    
    if request.method == 'POST':
        stock_updated=request.POST 
        produit=stock_updated.get('produit')
        qt=stock_updated.get('quantite_disponible')
        date_exp=stock_updated.get('date_expiration')

        # stock.produit=produit
        stock.produit=produit
        stock.quantite_disponible = qt
        stock.date_expiration = date_exp
        stock.save()
        return redirect('/ajout/')  # Rediriger vers une page appropriée après la modification

    return render(request, 'updatestock.html', {'stock': stock})



def ajouter_vente(request, article_id):
    produit = get_object_or_404(Stock, id=article_id)

    if request.method == 'POST':
        form = stockForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            
            if produit.quantite_disponible >= vente.quantite_vendue:
                vente.produit = produit
                vente.montant_total = vente.quantite_vendue * vente.prix_unitaire
                vente.save()
                
                produit.quantite_total -= vente.quantite_vendue
                produit.save()
                
                return redirect('addvente')
            else:
                form.add_error('quantite_vendue', 'Quantité insuffisante en stock.')
    else:
        form = stockForm()
    
    return render(request, 'vente.html', {'form': form})

#modifier une vente
def modifier_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)

    if request.method == 'POST':
        form = venteForm(request.POST, instance=vente)
        if form.is_valid():
            vente = form.save(commit=False)
            vente.montant_total = vente.quantite_vendue * vente.prix_unitaire
            vente.save()
            vente.update_stock_quantity()
            return redirect('addvente', vente_id=vente.id)
    else:
        form = venteForm(instance=vente)

    return render(request, 'updatevente.html', {'form': form})




def updatepers(request,pk):
    data=User.objects.get(pk=pk)
    if request.method=="POST":
        toto=request.POST
        data.nom=toto.get('username')
        data.prenom=toto.get('email')
        data.adresse=toto.get('password')
        data.save()

    return render(request,'updatepersonnel.html',{'data':data})
