from django.contrib import admin
from django.db.models import fields
from .models import Url
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('num', 'url')
    list_display_links = ('num', 'url')

admin.site.register(Url, UrlAdmin)