from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class category(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return f"{self.name}"

class Listings(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=264)
    startingBid = models.IntegerField()
    watchlist = models.ManyToManyField(User, blank=True, related_name='watchlistItem')
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_listings', default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="add_to_category", default="")    

    def __str__(self):
        return f"{self.id},  Listing Title: {self.title}, Category: {self.category}"
    
class bids(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids', default=0)
    current_listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bid", default=0)
    listing_bid = models.IntegerField(default=0)

class comments(models.Model):

    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userID", default=0)
    comment = models.CharField(max_length=264)
    allComments = models.ManyToManyField(Listings, blank=True, related_name='allComments')

    def __str__(self):
        return f"Username: {self.creater} Comment: {self.comment}"
    





  