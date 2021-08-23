from postdrfapp.models import CustomUser, Post
from django.contrib import admin
from postdrfapp import *
# Register your models here.


admin.site.register(Post)
admin.site.register(CustomUser)