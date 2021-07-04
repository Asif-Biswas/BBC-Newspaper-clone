from django.contrib import admin
from .models import *

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)
