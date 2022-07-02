from django.http import HttpResponse
from django.shortcuts import render
from books.models import Writer
from posts.models import Podcast

from django.db.models import Max
import random

def index(request):
    max_pk_writer = Writer.objects.latest('id').id
    random_writer = Writer.objects.filter(pk=random.randint(1, max_pk_writer))

    max_pk_podcast = Podcast.objects.latest('id').id
    random_podcast = Podcast.objects.filter(pk=random.randint(1, max_pk_podcast))
    context = {'podcasts': random_podcast, 'writers': random_writer}
    return render(request, 'index.html',context=context)

def contact(request):
    return render(request, 'contact.html')
