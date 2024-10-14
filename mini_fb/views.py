# File: mini_fb/views.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Description: The views file for the mini_fb application.

from django.shortcuts import render
from django.urls import reverse
from typing import Any

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import * ## import the models (e.g., Article)
from .forms import *

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
    # context_object_name = "profile"

    # overrides default get_context_data so that Foreign Key can
    # be used by site get a specific Profile's status messages
    def get_context_data(self, **kwargs: any):

        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        context['statuses'] = profile.get_status_messages()
        return context

class CreateProfileView(CreateView):
    '''A view to create a new Profile and save it to the database.'''

    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

    def get_success_url(self) -> str:
        '''Return the URL to redirect to on success.'''

        return self.object.get_absolute_url()

class CreateStatusMessageView(CreateView):
    '''A view to create a Status Message for a Profile.'''

    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        # context from superclass
        context = super().get_context_data(**kwargs)
        # Profile identified by PK from URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        # add Profile to context
        context['profile'] = profile
        return context

    def get_success_url(self) -> str:
        '''Return URL to redirect to on success.'''

        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return reverse('show_profile', kwargs={'pk': profile.pk})

    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        # print(f'CreateCommentView.form_valid(): form={form.cleaned_data}')
        # print(f'CreateCommentView.form_valid(): self.kwargs={self.kwargs}')

        # find the Profile identified by the PK from the URL pattern
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        # attach this Profile to the instance of the Comment to set its FK
        form.instance.profile = profile # like: comment.article = article

        # delegate work to superclass version of this method
        return super().form_valid(form)

    