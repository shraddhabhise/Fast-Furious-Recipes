from django.urls import path
from . import views
from .views import (
    RecipesDetailView,
    RecipesCreateView,
    RecipesUpdateView,
    RecipesDeleteView
)

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('search/', views.search, name='recipes-search'),
    path('about/', views.about, name='recipes-about'),
    path('register/', views.about, name='register'),
    path('recipes/<int:pk>/', RecipesDetailView.as_view(), name='recipes-detail'),
    path('recipes/<int:pk>/update', RecipesUpdateView.as_view(), name='recipes-update'),
    path('recipes/<int:pk>/delete', RecipesDeleteView.as_view(), name='recipes-delete'),
    path('recipes/new/', RecipesCreateView.as_view(), name='recipes-create')


]