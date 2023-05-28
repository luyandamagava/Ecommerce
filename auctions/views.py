from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Listings, comments
from .models import User


def index(request):
    return render(request, "auctions/index.html",{
        "listings": Listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def newListingPage(request):
    return render(request, "auctions/newListing.html")

def newListing(request):
    if request.method == "POST":

        if request.POST["listTitle"] == '' or request.POST["listDesc"] == '' or request.POST["listBid"] == '':
            messages.error(request, 'You did not enter a value', extra_tags="all")
            return redirect(reverse('newListingPage')) 
            

        lTitle = request.POST["listTitle"]
        lDescription = request.POST["listDesc"]
        lStartingBid = int(request.POST["listBid"])
        userID = User.objects.get(id=int(request.POST["UserID"]))
        newCategory= request.POST["category"]

        newList = Listings(title=lTitle, description=lDescription, startingBid=lStartingBid, creater=userID, category=newCategory)
        newList.save()

        return index(request)

def listing(request):
    if request.method == "POST":
        listing_id = int(request.POST["listingID"])
        userID = request.POST["userID"]
        currentListing = Listings.objects.get(id=listing_id)

        if userID == 'None':
            return render(request, "auctions/listing.html", {
            "title": currentListing.title,
            "description": currentListing.description,
            "startingBid": currentListing.startingBid,
            "ID": listing_id,
            "currentListing": currentListing,
            "creater": currentListing.creater,
            "category": currentListing.category
            
        })

        else:
            user = User.objects.get(id=userID)
            watchListItems = user.watchlistItem.all()
            allComments = currentListing.allComments.all()
            
        
    
            return render(request, "auctions/listing.html", {
                "title": currentListing.title,
                "description": currentListing.description,
                "startingBid": currentListing.startingBid,
                "ID": listing_id,
                "listings": watchListItems,
                "currentListing": currentListing,
                "creater": currentListing.creater,
                "category": currentListing.category,
                "comments": allComments
                
            })
        
   

def addToWatchList(request):
    if request.method == "POST":

        listing_id = int(request.POST["listingID"])
        userID = int(request.POST["userID"])
        listings = Listings.objects.get(id=listing_id)
        user = User.objects.get(id=userID)
        listings.watchlist.add(user)

        return listing(request)

def removeFromWatchlist(request):
    if request.method == "POST":

        listing_id = int(request.POST["listingID"])
        userID = int(request.POST["userID"])
        listings = Listings.objects.get(id=listing_id)
        user = User.objects.get(id=userID)
        listings.watchlist.remove(user)

        return listing(request)


def viewWatchList(request, userID):
    user = User.objects.get(id=userID)
    watchListItems = user.watchlistItem.all()

    return render(request, "auctions/watchlistItems.html", {
        "watchlistItems": watchListItems
    })

def newBid(request):
    if request.method == "POST" and request.POST["enterBid"]!= '':
        listing_id = int(request.POST["listingID"])
        listings = Listings.objects.get(id=listing_id)
        newValue = int(request.POST["enterBid"])

        if newValue <= listings.startingBid:
            messages.error(request, 'The value entered must be greater than current bid', extra_tags='low_bid')
            return listing(request)
        
        listings.startingBid = newValue
        listings.save()

        return listing(request)
    
    messages.error(request, 'Please enter a value', extra_tags='no_new_bid')
    return listing(request)

def deleteEntry(request):

    listing_id = int(request.POST["listingID"])
    listings = Listings.objects.get(id=listing_id)
    listings.delete()

    return index(request)

def add_comment(request):
    if request.method == "POST" and request.POST["comment"] != '':
        
        listing_id = int(request.POST["listingID"])
        listings = Listings.objects.get(id=listing_id)

        userID = int(request.POST["userID"])
        user = User.objects.get(id=userID)

        comment_made = request.POST["comment"]
        comm = comments(creater=user, comment=comment_made)
        comm.save()

        listings.allComments.add(comm)
        return index(request)
    
    else:
        messages.error(request, "You did not enter a comment in the comment bar", extra_tags='no_comment')
        return listing(request)



    
