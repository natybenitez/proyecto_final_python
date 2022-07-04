from django.shortcuts import render
from posts.models import  Podcast

# def posts(request):
#     posts = Posts.objects.all()
#     context = {'posts': posts}
#     return render(request, 'posts.html', context = context)

def podcast(request):
    podcasts = Podcast.objects.all()
    context = {'podcasts': podcasts}
    return render(request, 'podcast.html', context=context)

