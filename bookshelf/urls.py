# File: bookshelf/urls.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 11/24/2024
# Description: URL patterns for the bookshelf app

from django.urls import path #django.urls is a library for url management, path implements
from django.conf import settings #.conf configuration package; importing settings so file knows about project level settings
from . import views #from . = current directory, . import views imports [views.py] from current directory
from .views import * # our view class definition 
from django.contrib.auth import views as auth_views

#all of the URLs that are part of this app
urlpatterns = [
    # Profile-related URLs
    path('', views.ShowAllProfilesView.as_view(), name="book_show_all_profiles"),
    path('show_profile/<int:pk>', views.ShowProfilePageView.as_view(), name="book_show_profile"),
    path('create_profile/', views.CreateProfileView.as_view(), name="book_create_profile"),
    path('update_bio/', views.UpdateBioView.as_view(), name="update_bio"),

    # Book-related URLs
    path('show_all_books/', views.ShowAllBooksView.as_view(), name="show_all_books"),
    path('show_book/<int:pk>', views.ShowBookView.as_view(), name="show_book"),
    path('create_book/', views.CreateBookView.as_view(), name="create_book"),
    path('update_book/<int:pk>', views.UpdateBookView.as_view(), name="update_book"),
    path('show_bookshelf/<int:pk>/add_book/', views.AddBookToShelfView.as_view(), name="add_book"),

    # Bookshelf-related URLs
    path('show_bookshelf/<int:pk>', views.ShowBookshelfPageView.as_view(), name="show_bookshelf"),
    path('create_bookshelf/', views.CreateBookshelfView.as_view(), name="create_bookshelf"),
    path('delete_bookshelf/<int:pk>', views.DeleteBookshelfView.as_view(), name="delete_bookshelf"),

    # Review-related URLs
    path('update_review/<int:pk>', views.UpdateReviewView.as_view(), name="update_review"),
    path('delete_review/<int:pk>', views.DeleteReviewView.as_view(), name="delete_review"),
    path('book/<int:pk>/create_review/', views.CreateReviewView.as_view(), name='create_review'),

    # Comment-related URLs
    path('delete_comment/<int:pk>', views.DeleteCommentView.as_view(), name="delete_comment"),

    # Friend-related URLs
    path('create_friend/', views.CreateFriendView.as_view(), name="create_friend"),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='bookshelf/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='bookshelf/logged_out.html'), name="logout"),
]