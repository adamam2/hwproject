from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    area = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #this only allows 1 user per concept. # TODO find how to allow multiple users to own/edit
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        blank=True, null=True) #this tells the db to allow blanks during migrate


# TODO Build a Commands Data Model
# TODO Review Pep 8 documentation
# TODO Document spinning up a project using the command line

# class Piechart(models.Model):
    # labels = models.CharField(max_length=255)
    # values = models.DecimalField(..., max_digits=100, decimal_places=2)
