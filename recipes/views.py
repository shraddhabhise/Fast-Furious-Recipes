from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

#Class based views to create forms
# code functionality reference: https://www.youtube.com/watch?v=-s7e_Fy6NRU&index=10&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

from django.views.generic import (
    ListView,
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
    '''
    :param request: request data
    :return: renders home.html
    '''
    context={
        #retrieves all the database data and store in a object
        'recipes': Recipes.objects.all()
    }
    return render(request,'recipes/home.html', context)

def search(request):
    '''
    :param request data:
    :return: renders search.html
    '''

    #if request method is post, then retrieve the data from post form
    if request.method == "POST":
        sh = request.POST['srch']
        #if post data is not empty, then filter the database objects on tittle of recipes, matching the post data
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

class RecipesListView(ListView):
    '''
    class based view to list the recipes
    listing is done based on the date posted
    On each page 3 recipes are listed
    '''
    model = Recipes
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']
    paginate_by = 3

class RecipesDetailView(DetailView):
    '''
    class based view to show the details of recipes
    when we click on recipe title, this view is resonsible to show the details of that recipe
    '''
    model = Recipes


class RecipesCreateView(LoginRequiredMixin, CreateView):
    '''
    class based view to create recipes
    '''
    model = Recipes
    fields = ['title', 'ingredients', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    class based view to update recipes
    And just showing update facility to user who has created that recipe
    '''
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
    '''
    class based view to delete the recipes
    And just showing delete facility to user who has created that recipe
    '''
    model = Recipes
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    '''
    :param request: request data
    :return: renders about.html
    '''
    return render(request, 'recipes/about.html')