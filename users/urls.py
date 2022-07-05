from django.urls import path, include, re_path
from users.views import  edit_profile
urlpatterns = [
    path('edit-profile/', edit_profile, name='edit_profile'),   
]