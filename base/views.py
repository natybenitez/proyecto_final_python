from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from books.models import Writer, Book
from posts.models import Podcast, Blog_post
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from base.forms import User_registration_form
from django.contrib.auth.decorators import login_required
import random

# AUTH #

## Login #
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido/a '}
                return render(request, 'index.html', context = context)
            else:
                context = {'error_message':f'No hay un ningun usuario con esas credenciales'}
                form = AuthenticationForm()
                return render(request,'auth/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request,'auth/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form, 'display': 'none'}
        return render(request,'auth/login.html', context=context)

# Logout #
def logout_view(request):
    logout(request)
    return redirect('index')

# Register #
def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente ¡Bienvenido {username}!'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)


# INDEX #

def index(request):
    writer = Writer.objects.all().latest('id')
    book = Book.objects.all().latest('id')
    post = Blog_post.objects.all().latest('id')
    print(post)
    print(writer)
    context = {'writer': writer, 'book': book, 'post': post}
  
    return render(request, 'index.html', context=context)


# CONTACT #

def contact(request):       
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'contact.html')
    else:
        return redirect('login')


# SEARCH BAR #

def search_view(request):
    word_searched = request.GET['search'].lower()
    results_writers = Writer.objects.filter( Q(name=word_searched)) or Writer.objects.filter(Q(lastname=word_searched))
    results_podcasts = Podcast.objects.filter(Q(writer__name__icontains= word_searched)) or Podcast.objects.filter(Q(writer__lastname__icontains= word_searched))
    results_books = Book.objects.filter(Q(writer__name__icontains= word_searched)) or Book.objects.filter(Q(writer__lastname__icontains= word_searched))
    if results_writers.exists() or results_podcasts.exists() or results_books. exists():
        context = {'writers': results_writers,'podcasts':results_podcasts, 'books': results_books}
    else:
        context = {'errors':f'Disculpe, no se encontraron registros con la palabra:  "{word_searched}"'}
        
    return render(request, 'search.html', context=context)

# ABOUT #

def about(request):
    return render(request, 'about.html')