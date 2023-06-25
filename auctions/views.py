from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Listings, comments, category, bids
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
        new_category = request.POST["category"]
        all_categories = category.objects.all()
        new_category_object = ""
        categories_list = []


        for new_list in all_categories:
            categories_list.append(new_list.name)

        if new_category in categories_list:
            new_category_object = category.objects.get(name=new_category)

        else:
            new_category_object = category(name=new_category)
            new_category_object.save()



        newList = Listings(title=lTitle, description=lDescription, startingBid=lStartingBid, creater=userID, category=new_category_object)
        newList.save()
        new_bid = bids(user=userID, current_listing=newList, listing_bid=lStartingBid)
        new_bid.save()

        return HttpResponseRedirect(reverse("index"))

def listing(request):
    if request.method == "POST":
        listing_id = int(request.POST["listingID"])
        userID = request.POST["userID"]
        currentListing = Listings.objects.get(id=listing_id)
        allComments = currentListing.allComments.all()
        highest_bidder = bids.objects.get(listing_bid=currentListing.startingBid)

        if userID == 'None':
            return render(request, "auctions/listing.html", {
            "title": currentListing.title,
            "description": currentListing.description,
            "startingBid": currentListing.startingBid,
            "ID": listing_id,
            "currentListing": currentListing,
            "creater": currentListing.creater,
            "category": currentListing.category,
            "comments": allComments,
            "bidder": highest_bidder

        })

        else:
            user = User.objects.get(id=userID)
            watchListItems = user.watchlistItem.all()

            return render(request, "auctions/listing.html", {
                "title": currentListing.title,
                "description": currentListing.description,
                "startingBid": currentListing.startingBid,
                "ID": listing_id,
                "listings": watchListItems,
                "currentListing": currentListing,
                "creater": currentListing.creater,
                "category": currentListing.category,
                "comments": allComments,
                "bidder": highest_bidder

            })



def addToWatchList(request):
    if request.method == "POST":

        listing_id = int(request.POST["listingID"])
        userID = int(request.POST["userID"])
        currentListing = Listings.objects.get(id=listing_id)
        user = User.objects.get(id=userID)
        currentListing.watchlist.add(user)
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

def removeFromWatchlist(request):
    if request.method == "POST":

        listing_id = int(request.POST["listingID"])
        userID = int(request.POST["userID"])
        currentListing = Listings.objects.get(id=listing_id)
        user = User.objects.get(id=userID)
        currentListing.watchlist.remove(user)
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
        new_value = int(request.POST["enterBid"])
        user_id = int(request.POST['userID'])
        user = User.objects.get(id=user_id)
        new_bid_object = ""
        


        if new_value <= listings.startingBid:
            messages.error(request, 'The value entered must be greater than current bid', extra_tags='low_bid')
            return listing(request)

        listings.startingBid = new_value
        listings.save()


        try:
            new_bid_object = bids.objects.get(user=user, current_listing=listings)

        except bids.DoesNotExist:
            new_bid_object = bids(user=user, current_listing=listings, listing_bid=new_value)

        else:
            new_bid_object.listing_bid = new_value

        finally:
            new_bid_object.save()
            
        return listing(request)

    messages.error(request, 'You did not enter a value in the bids', extra_tags='no_new_bid')
    return listing(request)

def deleteEntry(request):

    listing_id = int(request.POST["listingID"])
    listings = Listings.objects.get(id=listing_id)
    listings.delete()

    return HttpResponseRedirect(reverse("index"))

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
        return HttpResponseRedirect(reverse("index"))

    else:
        messages.error(request, "You did not enter a comment in the comment bar", extra_tags='no_comment')
        return listing(request)


def display_categorys(request):
    categorys = category.objects.all()

    return render(request, "auctions/categorys.html", {
        "categorys": categorys
    })

def unique_category(request, category_name):
    current_category = category.objects.get(name=category_name)
    category_items = current_category.add_to_category.all()

    return render(request, "auctions/unique_category.html", {
        "categroy_items": category_items,
        "current_category":category_name
    })


def close_entry(request):

    listing_id = int(request.POST["listingID"])
    listings = Listings.objects.get(id=listing_id)
    bidder = bids.objects.get(listing_bid=listings.startingBid)

    messages.success(request, f"Thank you! {bidder.user.username.upper()} you won the {listings.title.upper()}", extra_tags='no_comment')
    listings.delete()


    return HttpResponseRedirect(reverse("index"))