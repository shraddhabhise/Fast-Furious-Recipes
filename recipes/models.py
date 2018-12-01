from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

'''
This class is responsible for creating database for recipes.
It has title, ingredients, content, date_posted, author fields.
'''

class Recipes(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})