from django.contrib import admin
from posts.models import Posts, Podcast

admin.site.register(Posts)

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin): 
    list_display= ['name', 'library']
