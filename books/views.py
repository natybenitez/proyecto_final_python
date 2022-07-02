import ctypes
from django.shortcuts import render
from books.models import Writer, Book
from books.forms import Writer_form

from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

# WRITERS #
## Writers list ##
def writers(request):
    writers = Writer.objects.all()
    context = {'writers': writers}
    return render(request, 'writer.html', context=context)

## Create new writer ##
def create_writer(request):
    if request.method == 'GET':
        form = Writer_form()
        context = {'form': form}
        return render(request, 'writer_new.html', context=context)
    else:
        form = Writer_form(request.POST)
        if form.is_valid():
            new_writer = Writer.objects.create(
                name = form.cleaned_data['name'],
                lastname = form.cleaned_data['lastname'],
                twitter_url = form.cleaned_data['twitter_url'],
                instagram_url = form.cleaned_data['instagram_url'],
                web_url = form.cleaned_data['web_url'],
            )
            context = {'new_writer': new_writer}
        else:
            context = {'errors': form.errors}
        return render(request, 'writer_new.html', context=context)

## Writer details ##
def writer_details(request, pk):
    try:
        writer = Writer.objects.get(pk=pk)
        context = {'writer': writer}
        return render(request, 'writer_details.html', context=context)
    except:
        context = {'error':'El autor no existe'}
        return render(request, 'writer.html', context=context)


# BOOKS #
## Books list ##
def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context=context)

## Create new book ##
def create_book(request):
    return render(request, 'create_book.html')



def search_writer_view(request):
    word_searched = request.GET['search']
    #writer = Writer.objects.get() #cuando traigo un solo producto (por ejemplo un SKU)
    writers = Writer.objects.filter( Q(name=request.GET['search'])) or Writer.objects.filter(Q(lastname=request.GET['search']) )
    if writers.exists():
        context = {'writers': writers}
    else:
        context = {'errors':f'Disculpe no se encontraron registros con la palabra:  {word_searched}'}
        
    return render(request, 'writer_search.html', context=context)




        