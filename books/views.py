from django.shortcuts import render
from books.models import Writer, Book

# Create your views here.


def writers(request):
    writers = Writer.objects.all()
    context = {'writers': writers}
    return render(request, 'writers.html', context=context)

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context=context)
