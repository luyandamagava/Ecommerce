from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newListingPage", views.newListingPage, name="newListingPage"),
    path("newListing", views.newListing, name="newListing"),
    path("listing", views.listing, name="listing"),
    path("addToWatchList", views.addToWatchList, name="addToWatchList"),
    path("<userID>/viewWatchList", views.viewWatchList, name="viewWatchList"),
    path("removeFromWatchlist", views.removeFromWatchlist, name="removeFromWatchlist"),
    path("newBid", views.newBid, name="newBid" ),
    path("deleteEntry", views.deleteEntry, name="deleteEntry"),
    path("add_comment", views.add_comment, name="add_comment"),
    path("categorys", views.display_categorys, name="categorys")
]
