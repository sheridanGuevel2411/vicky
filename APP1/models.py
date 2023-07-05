from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employe(models.Model):
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.nom

class Produit(models.Model):
    produit = models.CharField(max_length=100)
    description = models.TextField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.produit

class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_disponible = models.PositiveIntegerField()
    date_expiration = models.DateField()

    def __str__(self):
        return f"Stock {self.produit} - ID: {self.id}"

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    quantite_vendue = models.PositiveIntegerField()
    date_vente = models.DateField()
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vente {self.produit} - ID: {self.id}"

    def prix_unitaire(self):
        return self.produit.prix_unitaire

    def update_stock_quantity(self):
        stock = Stock.objects.get(produit=self.produit)
        stock.quantite_disponible -= self.quantite_vendue
        stock.save()

    def save(self, *args, **kwargs):
        self.montant_total = self.quantite_vendue * self.prix_unitaire()
        super().save(*args, **kwargs)
        self.update_stock_quantity()

    

