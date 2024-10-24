# File: mini_fb/urls.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Description: URL patterns for the mini_fb app

from django.urls import path #django.urls is a library for url management, path implements
from django.conf import settings #.conf configuration package; importing settings so file knows about project level settings
from . import views #from . = current directory, . import views imports [views.py] from current directory
from .views import ShowAllProfilesView, ShowProfilePageView, UpdateProfileView, DeleteStatusMessageView, UpdateStatusMessageView # our view class definition 

#all of the URLs that are part of this app
urlpatterns = [
    # path(r'', views.home, name="home"), #letter r means can support regular expressions
    # path(r'about', views.about, name="about"),
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path(r'show_profile/<int:pk>', views.ShowProfilePageView.as_view(), name="show_profile"), 
    path(r'create_profile', views.CreateProfileView.as_view(), name="create_profile"),
    path(r'profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name="create_status"), 
    # path(r'profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
    path(r'profile/<int:pk>/update', views.UpdateProfileView.as_view(), name="update_profile"),
    path('status/<int:pk>/delete', DeleteStatusMessageView.as_view(), name='delete_status'),
    path('status/<int:pk>/update', UpdateStatusMessageView.as_view(), name='update_status'),
]