from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class comments(models.Model):

    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userID", default=0)
    comment = models.CharField(max_length=264)

    def __str__(self):
        return f"Username: {self.creater} \n Comment: {self.comment}"


class Listings(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=264)
    startingBid = models.IntegerField()
    watchlist = models.ManyToManyField(User, blank=True, related_name='watchlistItem')
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_listings', default=0)
    category = models.CharField(max_length=64, default=None)
    comment = models.ManyToManyField(comments, blank=True, related_name='comments')

    def __str__(self):
        return f"{self.id} Listing Title: {self.title} Description: {self.description} Current Bid: {self.currentBid}"
    
class bids(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids', default=0)
    currentPrice = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bid", default=0)

  