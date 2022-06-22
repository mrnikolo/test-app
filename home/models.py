from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('home:detail', args=(self.id, self.slug))
