"""
URL configuration for devoir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path
from APP1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Index, name='home'),
    path('ADD',views.Ajout, name='AJT'),          
    path('edit',views.Edit, name='modif'),
    path('update/<str:id>',views.Update, name='upd'),
    path('delete/<str:id>', views.Delete, name='del'),
#ajout personnel
    path('pers',views.personnel, name='pers'),
    #modification personnel
    path('update/<pk>',views.updatepers, name='updpers'),

    path('ADp',views.Editp, name='Editp'),

    path('ajout/',views.add_stock, name='addstock'),
    path('updatest/<stock_id>/', views.modifier_stock, name='urlst'),
    path('ADst',views.Editst, name='Editst'),

#affichage des vente
   path('ajoutven/',views.add_vente, name='addvente'),
    #ajout des vente
    path('vente', views.ajouter_vente, name='ajouter_vente'),
    #modification des vente
    path('vent/<int:vente_id>/', views.modifier_vente, name='modifier_vente'),
   #path(' upatatev/<vente_id>/', views.modifier_vente, name='urlven'),
   #modification approvisionnement
   path('upatate/<pk>/', views.update, name='url2'),
   #ajout des approvisonnement
    path('ajoutpro/',views.add_appro, name='addappro'),
    path('delete_produit/<id>202321',views.delete_prod, name='delete_produit'),

    path('',views.connexion, name='logine'),
    path('reg',views.création,name='création'),
    path('logout', views.deconnexion, name='urllogout'),


]
  

  


