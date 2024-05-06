from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

from blog.forms import PostForm
from blog.models import Post

"""
def index(request):
    context={'val':"Menu Acceuil"}
    return render(request,'home.html',context) 
"""

class ListePost(ListView):
    model = Post
    template_name = 'blog/liste_post.html'
    context_object_name = 'post'

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'

class CreerPost(CreateView):
    model = Post
    template_name = 'blog/creer_post.html'
    form_class = PostForm 
    success_url = reverse_lazy('liste_post') 

class ModifierPost(UpdateView):
    model = Post
    template_name = 'blog/modifier_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_post') 

class SupprimerPost(DeleteView):
    model = Post
    template_name = 'blog/supprimer_post.html'
    success_url = reverse_lazy('liste_post') 