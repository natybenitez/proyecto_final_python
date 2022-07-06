from django.urls import path, include, re_path
from posts.views import  interview, podcast, Blog_posts, Blog_post_new, Blog_post_details, Blog_post_update, Blog_post_delete

urlpatterns = [
    path('podcast/', podcast, name='podcast'),
    path('interview/', interview, name='interview'),
    path('blog/', Blog_posts.as_view(), name='blog', kwargs={'message': None,}), 
    path('create-blog-post/', Blog_post_new.as_view(), name='blog_post_new'),
    path('blog-post-details/<int:pk>/', Blog_post_details.as_view(), name='blog_post_details'),
    path('delete-blog-post/<int:pk>/', Blog_post_delete.as_view(), name='blog_post_delete'),
    path('update-blog-post/<int:pk>/', Blog_post_update.as_view(), name='blog_post_update'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]