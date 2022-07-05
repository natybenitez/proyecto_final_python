from django.contrib import admin
from posts.models import Podcast, Article, Interview

#admin.site.register(Posts)

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin): 
    list_display= ['name', 'writer']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): 
    list_display= ['title', 'author','date_published', 'status']

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin): 
    list_display= ['name', 'writer']