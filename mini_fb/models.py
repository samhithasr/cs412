# mini_fb/models.py
# Define the data objects for our application

from django.db import models 

# This Profile model will need to include the 
# following data attributes: first name, last name, 
# city, email address, and a profile image url.

# Create your models here.

class Profile(models.Model):
    ''' Note: change docstring
    Encapsulate the idea of one Article by some Author.'''

    # data attributes of a Profile:
    first = models.TextField(blank=False)
    last = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    icon = models.URLField(blank=True)


    def __str__(self):
        '''Return a string representation of the object.'''

        return f'{self.first} {self.last} from {self.city}. Email: {self.email}'

        #quiz Q when do you need to run makemigrations command