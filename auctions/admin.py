from django.contrib import admin
from .models import *
#Register your models here.
@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = ("username", "id")
    
@admin.register(Listings)
class Listing_admin(admin.ModelAdmin):
    list_display = ("title", "description", "id")

@admin.register(category)
class Category_admin(admin.ModelAdmin):
    list_display = ("name", "id")

@admin.register(bids)
class Bid_admin(admin.ModelAdmin):
    list_display = ('user', 'current_listing', 'listing_bid', "id")

@admin.register(comments)
class Comment_admin(admin.ModelAdmin):
    list_display = ( 'comment', 'creater', "id")


