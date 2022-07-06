from django.urls import path, include, re_path
from books.models import Book
from books.views import Writers, Writer_new, Writer_details, Writer_delete, Writer_update, Books, Books_details


urlpatterns = [    
    path('books/', Books.as_view(), name='books', kwargs={'message': None,}),
    path('book-details/<int:pk>/', Books_details.as_view(model=Book), name='book_details'),
    path('writers/', Writers.as_view(), name='writers', kwargs={'message': None,}),
    path('create-writer/', Writer_new.as_view(), name='writer_new'),
    path('writer-details/<int:pk>/', Writer_details.as_view(), name='writer_details'),
    path('delete-writer/<int:pk>/', Writer_delete.as_view(), name='writer_delete'),
    path('update-writer/<int:pk>/', Writer_update.as_view(), name='writer_update'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
   
]