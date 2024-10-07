# File: mini_fb/models.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Define the data objects for the mini_fb application.

from django.db import models 

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

        return f'{self.first} {self.last} from {self.city}. Email: {self.email}'

