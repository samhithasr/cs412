# File: mini_fb/views.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Description: The views file for the mini_fb application.

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from typing import Any

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import * ## import the models (e.g., Article)
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin # allows for user authentication
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login 
import random

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
    # be used by site get a specific Profile's status messages and friends
    def get_context_data(self, **kwargs: any):

        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        context['statuses'] = profile.get_status_messages()
        context['friends'] = profile.get_friends()
        return context

class CreateProfileView(CreateView):
    '''A view to create a new Profile and save it to the database.'''

    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

    def get_success_url(self) -> str:
        '''Return the URL to redirect to on success.'''

        return self.object.get_absolute_url()

class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    '''A view to create a Status Message for a Profile.'''

    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')

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

        # save the status message to database
        sm = form.save()

        # read the file from the form:
        files = self.request.FILES.getlist('files')

        # loop over the uploaded files and create an Image object for each
        for file in files:
            # create a new Image object
            img = Image(statusMessage = sm, image_file = file)
            # save Image object to database
            img.save()

        # delegate work to superclass version of this method
        return super().form_valid(form)

# Comment to edit out later: LoginRequiredMixin
# override dispatch in order to authenticate for
# proper user
class UpdateProfileView(LoginRequiredMixin, UpdateView) :
    '''A view to update the existing Profile.'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"   

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')   

    def get_success_url(self):
        '''Return the URL to redirect to after successfully updating the profile.'''

        # After updating, redirect to the profile's detail page
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return reverse('show_profile', kwargs={'pk': profile.pk})

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    '''A view to delete an existing StatusMessage.'''

    model = StatusMessage
    template_name = "mini_fb/delete_status_form.html"
    context_object_name = 'status'

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')

    def get_success_url(self):
        '''Return the URL to redirect to after successfully updating the profile.'''

        # After updating, continue showing the Profile page.
        profile = self.object.profile
        return reverse('show_profile', kwargs={'pk': profile.pk})

class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    '''A view to update an existing StatusMessage.'''

    model = StatusMessage
    form_class = UpdateStatusForm
    template_name = "mini_fb/update_status_form.html"
    context_object_name = 'status'      

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')

    def get_success_url(self):
        '''Return the URL to redirect to after successfully updating the StatusMessage.'''

        # After updating, redirect to the profile's detail page
        profile = self.object.profile
        return reverse('show_profile', kwargs={'pk': profile.pk})
    
class CreateFriendView(LoginRequiredMixin, View):
    '''A view to create a friendship between two Profiles.'''

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')
        
    def dispatch(self, request, *args, **kwargs):
        '''Override dispatch to get info based on URL.'''
        p1 = get_object_or_404(Profile, pk=kwargs['pk'])
        p2 = get_object_or_404(Profile, pk=kwargs['other_pk'])

        p1.add_friend(p2)
        return redirect('show_profile', pk=p1.pk)

class ShowFriendSuggestionsView(DetailView):
    '''A view to show suggestions of Friends.'''

    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        # context from superclass
        context = super().get_context_data(**kwargs)
        # Profile identified by PK from URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        # Get friend suggestions
        context['suggestions'] = profile.get_friend_suggestions()

        return context

class ShowNewsFeedView(DetailView):
    '''A view to show a Profile's news feed.'''

    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        # context from superclass
        context = super().get_context_data(**kwargs)
        # profile from URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        # Get news feed
        context['statuses'] = profile.get_news_feed()

        return context