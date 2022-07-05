from django.contrib import admin

from users.models import User_profile

#admin.site.register(User_profile)

@admin.register(User_profile)
class User_profileAdmin(admin.ModelAdmin): 
    list_display= ['user']
