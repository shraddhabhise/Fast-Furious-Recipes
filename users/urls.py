from django.urls import path
from . import views

#url mapping for register view

urlpatterns = [
    path('register/', views.register, name='register'),
]