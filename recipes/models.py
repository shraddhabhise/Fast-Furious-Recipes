from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipes(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})