from django.contrib import admin
from django.urls import path, include, re_path
from base.views import index, contact, login_view, logout_view, register_view, search_view, about

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('search/', search_view, name='search_view'),
    path('about/', about, name='about'),
    path('', include('books.urls')),
    path('', include('posts.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
