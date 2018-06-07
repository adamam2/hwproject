from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    long_description = models.TextField(null=False, blank=True, default='')
    area = models.CharField(max_length=255)
    example = models.FileField(null=False, blank=True, default='')
    slug = models.SlugField(unique=True)


# TODO Build a Commands Data Model
# TODO Review Pep 8 documentation
# TODO Document spinning up a project using the command line

# class Piechart(models.Model):
    # labels = models.CharField(max_length=255)
    # values = models.DecimalField(..., max_digits=100, decimal_places=2)
