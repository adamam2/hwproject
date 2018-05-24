from django.db import models

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    area = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


# TODO Build a Commands Data Model
# TODO Review Pep 8 documentation
# TODO Document spinning up a project using the command line

class Piechart(models.Model):
    labels = models.CharField(max_length=255)
    values = models.DecimalField(..., max_digits=100, decimal_places=2)