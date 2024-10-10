# File: mini_fb/views.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Description: The views file for the mini_fb application.

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import * ## import the models (e.g., Article)

# class-based view
# first; last; city; email; pfp
class ShowAllProfilesView(ListView):
    '''the view to show all Profiles'''
    model = Profile # the model to display
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # context variable to use in the template

class ShowProfilePageView(DetailView):
    '''The view to show a specific Profile.'''

    model = Profile
    template_name = "mini_fb/show_profile.html"
    context_object_name = "profile"
