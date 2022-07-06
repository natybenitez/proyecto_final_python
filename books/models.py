from django.db import models
from slugify import slugify
from datetime import datetime
from django_countries.fields import CountryField
from django import forms

#from django.urls import reverse

# Third party app imports
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

class Writer(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    lastname = models.CharField(max_length=100, verbose_name='apellido')
    bio = RichTextField(blank=False, verbose_name='biografía')
    country = CountryField(blank=False, verbose_name='país')   
    web_url = models.URLField(blank=True, verbose_name="web oficial")
    image = models.ImageField(upload_to = 'writers-gallery', default='default.jpg', verbose_name='fotografía')  
    
    class Meta:
        unique_together = ('name', 'lastname',)
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return "%s %s" % (self.name, self.lastname)

    
class Book(models.Model):
    title = models.CharField(max_length=500, verbose_name='título')
    writer = models.ForeignKey('Writer', on_delete=models.CASCADE, related_name='books', default=None)
    year_published = models.IntegerField(verbose_name='año de publicación')
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, related_name='books', default=None)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT, related_name='books', default=None)
    summary = RichTextField(blank=False, verbose_name='resumen', default="")
    image = models.ImageField(upload_to = 'books-cover-gallery', default='no-cover-available.jpg', verbose_name='cover')

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self):
        return "%s " % (self.title)


class Publisher(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'editorial'
        verbose_name_plural = 'editoriales'
    def __str__(self):
        return self.name