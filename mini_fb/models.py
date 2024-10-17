# File: mini_fb/models.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Define the data objects for the mini_fb application.

from django.db import models 
from django.urls import reverse
# import time

# This Profile model will need to include the 
# following data attributes: first name, last name, 
# city, email address, and a profile image url.

# Create your models here.

class Profile(models.Model):
    '''
    Encapsulate the idea of one Profile.
    Provide fields needed for Profile.'''

    # data attributes of a Profile:
    first = models.TextField(blank=False)
    last = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    icon = models.URLField(blank=True)


    def __str__(self):
        '''Return a string representation of the object.'''

        return f'{self.first} {self.last} from {self.city}.'

    def get_status_messages(self):
        '''Return a list of all status messages associated with a Profile.'''

        return StatusMessage.objects.filter(profile=self).order_by('-published')

    def get_absolute_url(self):
        '''Return URL to access the new profile.'''
        return reverse('show_profile', kwargs={'pk': self.pk})
        #quiz Q when do you need to run makemigrations command

class StatusMessage(models.Model):
    '''
    Encapsulate idea of a StatusMessage for a Profile.
    Provide fields needed.
    '''
    message = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    # profile = Profile.objects.get(pk=self.kwargs['pk'])
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the StatusMessage.'''
        return f'"{self.message}"'


