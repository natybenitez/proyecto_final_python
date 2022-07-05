from unicodedata import name
from django.shortcuts import render
from django.urls import reverse
from books.models import Writer, Book
from posts.models import Podcast
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


# WRITERS #

## Writers list ##
class Writers(ListView):
    model = Writer
    template_name ='writers/writer.html'

## Writer details ##
class Writer_details(DetailView):
    model = Writer
    template_name = 'writers/writer_details.html'

## Create new writer ##
class Writer_new(LoginRequiredMixin, CreateView):
    model = Writer
    template_name = 'writers/writer_new.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('writer_details', kwargs={'pk': self.object.pk}) # writer_details es el name del path definida en urls

## Delete writer ##
class Writer_delete(DeleteView):
    model = Writer
    template_name = 'writers/writer_delete.html'

    def get_success_url(self):
        return reverse('writers')

## Update writer ##
class Writer_update(UpdateView):
    model = Writer
    template_name = 'writers/writer_update.html'
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
    word_searched = request.GET['search'].lower()
    results_writers = Writer.objects.filter( Q(name=word_searched)) or Writer.objects.filter(Q(lastname=word_searched))
    results_podcast = Podcast.objects.filter(Q(writer__name__icontains= word_searched)) or Podcast.objects.filter(Q(writer__lastname__icontains= word_searched))
    
    print(name)
    #books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
    print(results_podcast)
    
    if results_writers.exists() or results_podcast.exists():
        context = {'writers': results_writers,'podcast':results_podcast }
    else:
        context = {'errors':f'Disculpe, no se encontraron registros con la palabra:  "{word_searched}"'}
        
    return render(request, 'writer_search.html', context=context)




        