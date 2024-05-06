from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('list/',views.listProduit,name='liste'),
    path('vitrine/',views.vitrine,name='V'),
    path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
    path('nouvCommande/',views.nouveauCommande, name='nouveauComm'),
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login')
]