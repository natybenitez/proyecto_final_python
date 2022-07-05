from django.contrib import admin
from books.models import Category, Writer, Book, Publisher

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): # para verlo mas prolijo en el admin
    list_display= ['name', 'is_approved']

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['name','lastname', 'web_url']

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display= ['title', 'writer', 'year_published',]

admin.site.register(Publisher)