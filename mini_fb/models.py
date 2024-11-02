# File: mini_fb/models.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Define the data objects for the mini_fb application.

from django.db import models 
from django.urls import reverse
from django.contrib.auth.models import User # imports Django user account(s)

# import time

# This Profile model will need to include the 
# following data attributes: first name, last name, 
# city, email address, and a profile image url.

# Create your models here.

class Profile(models.Model):
    '''
    Encapsulate the idea of one Profile.
    Provide fields needed for Profile.'''

    user = models.ForeignKey(User, on_delete=models.CASCADE) # change to the orphan one maybe?

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

    def get_friends(self):
        '''Return a list of Friends' Profiles.'''

        # Collect cases where self is Profile 1 and Profile 2 for a Friend
        ifProfile1 = Friend.objects.filter(profile1=self)
        ifProfile2 = Friend.objects.filter(profile2=self)

        # Create a list from ifProfile1 and ifProfile2
        friends = [f.profile2 for f in ifProfile1] + [f.profile1 for f in ifProfile2]
        return friends

    def add_friend(self, other):
        '''Add a Friend to this Profile.'''

        # Checks to prevent self-friending
        if (self == other):
            return

        # Checks to see if a friendship exists between self and other
        friendExists = Friend.objects.filter(profile1=self,profile2=other).exists() or \
        Friend.objects.filter(profile1=other,profile2=self).exists()

        # if the friendship exists, return; else, create new friendship
        if friendExists:
            return
        else:
            Friend(profile1=self,profile2=other).save()

    def get_friend_suggestions(self):
        '''Return a list of Profiles suggested to be Friends with.'''

        # list of profiles without self
        withoutSelf = Profile.objects.exclude(pk=self.pk)

        # lists of friends
        friends1 = Friend.objects.filter(profile1=self)
        friends2 = Friend.objects.filter(profile2=self)

        # get primary keys for friends
        ids = set(friend.profile2.pk for friend in friends1) | set(friend.profile1.pk for friend in friends2)

        # exclude friends from suggestions
        suggested = withoutSelf.exclude(pk__in=ids)

        return suggested

    def get_news_feed(self):
        '''Return StatusMessages from self (profile)'s friends, and self.'''

        # that profile's status messages
        selfStatuses = self.get_status_messages()

        # Friends
        friends1 = Friend.objects.filter(profile1=self)
        friends2 = Friend.objects.filter(profile2=self)

        # statuses = [self.get_status_messages()] + [status for friend in friends1 ]
        statuses = StatusMessage.objects.none()
        statuses = statuses | selfStatuses

        # Loops through lists of friends and adds statuses
        for friend in friends1:
            statuses = friend.profile2.get_status_messages() | statuses
        for friend in friends2:
            statuses = friend.profile1.get_status_messages() | statuses

        # Returns in reverse time order
        return statuses.order_by('-published')

class StatusMessage(models.Model):
    '''
    Encapsulate idea of a StatusMessage for a Profile.
    Provide fields needed.
    '''
    message = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    # profile = Profile.objects.get(pk=self.kwargs['pk'])

    # Creates a one-to-many relationship between Profile and StatusMessage
    # on_delete=models.CASCADE: deletes all StatusMessages associated with a Profile 
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the StatusMessage.'''
        return f'"{self.message}"'

    def get_images(self):
        '''Return a QuerySet of all Images on this StatusMessage.'''

        # use the ORM to retrieve Images for which the FK is this StatusMessage
        return Image.objects.filter(statusMessage=self)

class Image(models.Model):
    '''
    Encapsulates the idea of an image file, rather than a URL, that 
    is stored in the Django media directory.
    '''

    statusMessage = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    '''
    Encapsulates the idea of a Friend, which Profiles can have. 
    Connects Profiles to other Profiles. Provides fields needed
    for the Friend model.
    '''

    profile1 = models.ForeignKey("Profile", related_name="profile1",on_delete=models.DO_NOTHING)
    profile2 = models.ForeignKey("Profile", related_name="profile2",on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.profile1.first} {self.profile1.last} & {self.profile2.first} {self.profile2.last}"

