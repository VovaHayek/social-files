from django.contrib import admin

from .models import userPost, CustomUser

admin.site.register(CustomUser)
admin.site.register(userPost)