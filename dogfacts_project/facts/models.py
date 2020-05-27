from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Fact(models.Model):
    text = models.TextField()
    DOG = "Dog"
    types = [(DOG, "dog"),]
    type = models.CharField(choices=types, default=DOG, max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)