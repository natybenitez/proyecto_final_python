from unicodedata import name
from django.shortcuts import render
from django.urls import reverse
from books.models import Writer, Book
from posts.models import Podcast
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



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

class Books(ListView):
    model = Book
    template_name ='books/books.html'





        