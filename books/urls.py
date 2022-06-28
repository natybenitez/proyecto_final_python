from django.urls import path, include, re_path
from books.views import writers, books, create_book, create_writer

urlpatterns = [
    
    path('books/', books, name='books'),
    path('writers/', writers, name='writers'),
    path('create-book/', create_book, name='create_book'),
    path('create-writer/', create_writer, name='create_writer'),
    #path('<slug:slug>,<int:id>/', views.article_detail, name='article'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]