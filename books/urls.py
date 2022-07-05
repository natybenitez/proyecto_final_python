from django.urls import path, include, re_path
from books.views import Writers, books, Writer_new, search_writer_view, Writer_details, Writer_delete, Writer_update


urlpatterns = [    
    path('books/', books, name='books'),
    path('writers/', Writers.as_view(), name='writers',kwargs={'message': None,}),
    path('create-writer/', Writer_new.as_view(), name='writer_new'),
    path('search-writer/', search_writer_view, name='search_writer_view'),
    path('writer-details/<int:pk>/', Writer_details.as_view(), name='writer_details'),
    path('delete-writer/<int:pk>/', Writer_delete.as_view(), name='writer_delete'),
    path('update-writer/<int:pk>/', Writer_update.as_view(), name='writer_update'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
   
]