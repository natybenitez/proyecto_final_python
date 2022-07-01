from django.contrib import admin
from books.models import Category, Writer, Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): # para verlo mas prolijo en el admin
    list_display= ['name', 'is_approved']

admin.site.register(Writer)

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display= ['book_name', 'year_published', 'publisher']

