from django.urls import path,include
from .views import CategoryAPIView
from .views import ProduitAPIView
from . import views
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('list/',views.listProduit,name='liste'),
    path('vitrine/',views.vitrine,name='V'),
    path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
    path('nouvCommande/',views.nouveauCommande, name='nouveauComm'),
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),
]