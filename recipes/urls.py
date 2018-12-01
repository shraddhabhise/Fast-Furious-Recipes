from django.urls import path
from . import views
from .views import (
    RecipesListView,
    RecipesDetailView,
    RecipesCreateView,
    RecipesUpdateView,
    RecipesDeleteView
)

'''
The urls and their corresponding action views are mapped below
'''
urlpatterns = [
    path('', RecipesListView.as_view(), name='recipes-home'),
    path('search/', views.search, name='recipes-search'),
    path('about/', views.about, name='recipes-about'),
    path('register/', views.about, name='register'),
    path('recipes/<int:pk>/', RecipesDetailView.as_view(), name='recipes-detail'),
    path('recipes/<int:pk>/update', RecipesUpdateView.as_view(), name='recipes-update'),
    path('recipes/<int:pk>/delete', RecipesDeleteView.as_view(), name='recipes-delete'),
    path('recipes/new/', RecipesCreateView.as_view(), name='recipes-create')


]