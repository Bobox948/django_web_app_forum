from django.contrib import admin

# Register your models here.
from .models import User, Informations, Thread, Post


class InformationsAdmin(admin.ModelAdmin):
    list_display = ("who", "gender", "birth", "image", "bio", "origin", "joined") # here I say what I want displayed in the admin pannel

class ThreadAdmin(admin.ModelAdmin):
    list_display = ("madeby", "thread_created", "title", "content", "photo", "closed")

class PostAdmin(admin.ModelAdmin):
    list_display = ("madeby", "post_created", "content", "onwhat", "who")
# Register your models here.

admin.site.register(User)
admin.site.register(Thread, ThreadAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(Informations, InformationsAdmin)



