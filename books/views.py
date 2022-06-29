from django.shortcuts import render
from books.models import Writer, Book
from books.forms import Writer_form

from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def writers(request):
    writers = Writer.objects.all()
    context = {'writers': writers}
    return render(request, 'writers.html', context=context)

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context=context)

def create_book(request):
    return render(request, 'create_book.html')

def create_writer(request):
    if request.method == 'GET':
        form = Writer_form()
        context = {'form': form}
        return render(request, 'create_writer.html', context=context)
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
        return render(request, 'create_writer.html', context=context)

# def search_writer_view(request):
#     print(request.GET)
#     #writer = Writer.objects.get() #cuando traigo un solo producto (por ejemplo un SKU)
#     writers = Writer.objects.filter(name__icontains=request.GET['search'])
#     context = {'writers': writers}
#     return render(request, 'search_writer.html', context=context)

def search_writer_view(request):
    print(request.GET)
    #writer = Writer.objects.get() #cuando traigo un solo producto (por ejemplo un SKU)
    writers = Writer.objects.filter( Q(name=request.GET['search'])) or Writer.objects.filter(Q(lastname=request.GET['search']) )
    print(writers)
    context = {'writers': writers}
    return render(request, 'search_writer.html', context=context)
        