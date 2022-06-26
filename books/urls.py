from django.urls import path, include, re_path
from books.views import writers, books

urlpatterns = [
    path('', writers, name='writers'),
    path('', books, name='books'),
    #path('<slug:slug>,<int:id>/', views.article_detail, name='article'),
    #re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]