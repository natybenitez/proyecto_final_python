from django.contrib import admin
from posts.models import Podcast

#admin.site.register(Posts)

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin): 
    list_display= ['name', 'library']
