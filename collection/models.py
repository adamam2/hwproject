from django.db import models

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    area = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
