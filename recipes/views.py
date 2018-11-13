from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

#Class based views to create forms
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
recipes=[
    {
        'ingredients': 'spinach',
        'name': 'Spinach salad',
        'content': 'Add sesame seeds, spinach, olive oil, cheese'

    },
    {
        'ingredients': 'Onions,oil,salt',
        'name': 'Onion rings',
        'content': 'Cut onion into rings, fry them in oil and add salt'

    }
]

def home(request):
    context={
        'recipes': Recipes.objects.all()
    }
    return render(request,'recipes/home.html', context)

def search(request):
    if request.method == "POST":
        sh = request.POST['srch']

        if sh:
            match = Recipes.objects.filter(Q(title__icontains=sh))

            context = {'sr': match}

            if match:
                    return render(request, 'recipes/search.html', context)
            else:
                return render(request, 'recipes/search.html')
        else:
            return render(request, 'recipes/search.html')

    return render(request, 'recipes/search.html')

class RecipesDetailView(DetailView):
    model = Recipes


class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipes
    fields = ['title', 'ingredients', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipes
    fields = ['title', 'ingredients', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class RecipesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipes
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'recipes/about.html')