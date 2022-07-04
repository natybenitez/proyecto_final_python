from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from books.models import Writer
from posts.models import Podcast

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
                context = {'message':f'Bienvenido '}
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


def index(request):
    min_pk_writer = Writer.objects.all().order_by('id')[1].id
    print(min_pk_writer)
    max_pk_writer = Writer.objects.latest('id').id
    random_writer = Writer.objects.filter(pk=random.randint(min_pk_writer, max_pk_writer))

    max_pk_podcast = Podcast.objects.latest('id').id
    random_podcast = Podcast.objects.filter(pk=random.randint(1, max_pk_podcast))
    context = {'podcasts': random_podcast, 'writers': random_writer}
    return render(request, 'index.html',context=context)

# @login_required
# def contact(request):
#     return render(request, 'contact.html')

def contact(request):       
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'contact.html')
    else:
        return redirect('login')