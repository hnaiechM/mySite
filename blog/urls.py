from django.urls import path,include
from .views import ListePost
from .views import DetailPost
from .views import CreerPost
from .views import ModifierPost
from .views import SupprimerPost

urlpatterns = [
path('', ListePost.as_view() , name='Liste_post'),
path('<int:pk>', ListePost.as_view() , name='Liste_post'),
path('<int:pk>/', DetailPost.as_view(), name='detail_post'),
path('<int:pk>/', CreerPost.as_view(), name='creer_post'),
path('ajouter/', CreerPost.as_view(), name='creer_post'), 
path('<int:pk>/modifier/', ModifierPost.as_view(), name='modifier_post'), 
path('<int:pk>/supprimer/', SupprimerPost.as_view(), name='supprimer_post'), 

]






