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
    lastname = models.CharField(max_length=100)
    #image = models.ImageField(default='profile-pic-default.jpg', upload_to='profile_pics')
    bio = RichTextField(blank=False, help_text="Agrega información sobre este/a autor/a")
    country = CountryField(blank=False)

    twitter_url = models.CharField(help_text= "Ingresa # si el escritor/a no posee una cuenta",
                                    max_length=250, default="#",
                                   blank=True, null=True,
                                   )
    instagram_url = models.CharField(max_length=250, default="#",
                                     blank=True, null=True,
                                     help_text= "Ingresa # si el escritor/a no posee una cuenta")
    
    web_url = models.URLField(blank=True, verbose_name="Web Oficial")

    
    class Meta:
        unique_together = ('name', 'lastname',)
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return "%s %s" % (self.name, self.lastname)

    

class Book(models.Model):
    book_name = models.CharField(max_length=500)
    year_published = models.IntegerField()
    publisher = models.CharField(max_length=100, null=False, blank=False)
    #writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    #category= forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
    #category = models.ForeignKey('app_books.Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self):
        return self.book_name


