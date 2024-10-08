# File: mini_fb/urls.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Description: URL patterns for the mini_fb app

from django.urls import path #django.urls is a library for url management, path implements
from django.conf import settings #.conf configuration package; importing settings so file knows about project level settings
from . import views #from . = current directory, . import views imports [views.py] from current directory
from .views import ShowAllProfilesView # our view class definition 

#all of the URLs that are part of this app
urlpatterns = [
    # path(r'', views.home, name="home"), #letter r means can support regular expressions
    # path(r'about', views.about, name="about"),
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
]