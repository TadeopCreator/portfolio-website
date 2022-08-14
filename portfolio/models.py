from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=150)
    description = CharField(max_length=500)
    image = ImageField(upload_to='portfolio/images', blank=True)
    url = URLField(blank=True)
    year = models.IntegerField(blank=True, null=True) 
    tags = CharField(max_length=100, blank=True)
    featured = models.BooleanField(default=False, blank=True)
