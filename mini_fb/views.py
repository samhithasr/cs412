# models/views.py
# define the views for the blog app
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import * ## import the models (e.g., Article)

# class-based view
# first; last; city; email; pfp
class ShowAllView(ListView):
    '''the view to show all Articles'''
    model = Profile # the model to display
    template_name = 'blog/show_all.html'
    context_object_name = 'profiles' # context variable to use in the template