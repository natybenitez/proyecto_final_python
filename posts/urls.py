from django.urls import path, include, re_path
from posts.views import posts, podcast

urlpatterns = [
    
    path('posts/', posts, name='posts'),
    path('podcast/', podcast, name='podcast'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]