from django.shortcuts import render
from posts.models import Posts

# Create your views here.


def posts(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context = context)