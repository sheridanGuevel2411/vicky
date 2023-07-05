from django.contrib import admin
from .models import Employe
from .models import Vente
from .models import Produit
from .models import Stock
# Register your models here.
admin.site.register(Employe)
admin.site.register(Vente)
admin.site.register(Produit)
admin.site.register(Stock)





