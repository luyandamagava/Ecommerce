from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listings(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=264)
    startingBid = models.IntegerField()
    watchlist = models.ManyToManyField(User, blank=True, related_name='watchlistItem')
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserID", default=0)

    def __str__(self):
        return f"{self.id} Listing Title: {self.title} Description: {self.description} Current Bid: {self.currentBid}"
    
class bids(models.Model):
    
    title = models.CharField(max_length=64)
    currentPrice = models.IntegerField()

    def __str__(self):
        return f"{ self.title}: Current Price {self.currentPrice}"

class comments(models.Model):

    username = models.CharField(max_length=64)
    comment = models.CharField(max_length=264)

    def __str__(self):
        return f"Username: {self.username} \n Comment: {self.comment}"
