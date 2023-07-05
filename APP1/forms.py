from django import forms
from .models import Produit, Stock, Vente

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = {'produit','description','prix_unitaire'}


class stockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = {'produit','quantite_disponible','date_expiration'}


class approForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = {'produit','description','prix_unitaire'}

class venteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = {'produit','quantite_vendue','date_vente','montant_total','username'}