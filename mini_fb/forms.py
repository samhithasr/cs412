# File: mini_fb/forms.py
# Author: Sam Somavarapu (samhitha@bu.edu), 10/14/2024
# Description: The mini_fb forms.py file, used to create
# new Profiles. 

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form for users to create a new Profile.'''

    # first; last; city; email; pfp
    class Meta:
        '''Associate this HTML form with the Profile data model.'''
        model = Profile
        fields = ['first', 'last', 'city', 'email', 'icon',]

class CreateStatusMessageForm(forms.ModelForm):
    '''A form for users to add Status Messages to a Profile.'''
    class Meta:
        '''Associate this HTML form with the StatusMessage data model.'''
        model = StatusMessage
        fields = ['message',]