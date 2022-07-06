from django.shortcuts import render
from django.urls import reverse
from posts.models import  Podcast, Blog_post, Interview
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# BLOG POSTS #

## Blog_posts list ##
class Blog_posts(ListView):
    model = Blog_post
    template_name = 'blog/blog.html'

## Blog_post details ##
class Blog_post_details(DetailView):
    model = Blog_post
    template_name = 'blog/blog_post_details.html'

## Create new Blog_post ##
class Blog_post_new(LoginRequiredMixin, CreateView):
    model = Blog_post
    template_name = 'blog/blog_post_new.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('blog_post_details', kwargs={'pk': self.object.pk}) 

## Delete Blog_post ##
class Blog_post_delete(LoginRequiredMixin, DeleteView):
    model = Blog_post
    template_name = 'blog/blog_post_delete.html'

    def get_success_url(self):
        return reverse('blog')

## Update Blog_post ##
class Blog_post_update(LoginRequiredMixin, UpdateView):
    model = Blog_post
    template_name = 'blog/blog_post_update.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('blog_post_details', kwargs={'pk': self.object.pk})

## PODCAST ##
def podcast(request):
    podcasts = Podcast.objects.all()
    context = {'podcasts': podcasts}
    return render(request, 'podcast/podcast.html', context=context)

## INTERVIEWS ##
def interview(request):
    interviews = Interview.objects.all()
    context = {'interviews': interviews}
    return render(request, 'interview/interview.html', context=context)