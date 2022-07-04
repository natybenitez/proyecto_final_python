import ctypes
from django.shortcuts import render
from django.urls import reverse
from books.models import Writer, Book
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
#from django.contrib import messages
#from books.forms import Writer_form
#from django.http import HttpResponse



# Create your views here.

# WRITERS #
## Writers list ##
class Writers(ListView):
    model = Writer
    template_name ='writer.html'

## Writer details ##
class Writer_details(DetailView):
    model = Writer
    template_name = 'writer_details.html'

## Create new writer ##
class Writer_new(LoginRequiredMixin, CreateView):
    model = Writer
    template_name = 'writer_new.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('writer_details', kwargs={'pk': self.object.pk}) # writer_details es el name del path definida en urls

## Delete writer ##
class Writer_delete(DeleteView):
    model = Writer
    template_name = 'writer_delete.html'

    def get_success_url(self):
        return reverse('writers')

## Update writer ##
class Writer_update(UpdateView):
    model = Writer
    template_name = 'writer_update.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('writer_details', kwargs={'pk': self.object.pk})

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




        