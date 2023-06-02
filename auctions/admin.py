from django.contrib import admin
from .models import *
#Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")



class Category_admin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Listings, ListingAdmin)
admin.site.register(category, Category_admin)
