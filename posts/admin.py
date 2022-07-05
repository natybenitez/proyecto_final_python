from django.contrib import admin
from posts.models import Podcast, Blog_post, Interview

#admin.site.register(Posts)

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin): 
    list_display= ['name', 'writer']

@admin.register(Blog_post)
class Blog_postAdmin(admin.ModelAdmin): 
    list_display= ['title', 'author','date_published', 'status']

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin): 
    list_display= ['name', 'writer']