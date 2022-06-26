from django.contrib import admin
from books.models import Category, Writer, Book

admin.site.register(Category)
admin.site.register(Writer)
admin.site.register(Book)
