from django.shortcuts import render
from django.template import loader
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'acceuil.html' )