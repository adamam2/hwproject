from django.db import models
from tinymce.models import HTMLField
#from django.contrib.auth.models import User

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField()
    long_description = models.TextField(null=False, blank=True, default='', verbose_name='Long Description')
    content = HTMLField(null=False, blank = True, default = '')
    AREA_CHOICES = (('Apps', 'Apps'),
        ('Cache', 'Cache'),
        ('Django', 'Django'),
        ('Docker', 'Docker'),
        ('General', 'General'),
        ('Git', 'Git'),
        ('HTML & CSS', 'HTML & CSS'),
        ('JavaScript', 'JavaScript'),
        ('jQuery', 'jQuery'),
        ('Python','Python'))
    area = models.CharField(max_length=255, choices=AREA_CHOICES, verbose_name='Area', default='APP')
    example = models.FileField(null=False, blank=True, default='')
    slug = models.SlugField(unique=True)

