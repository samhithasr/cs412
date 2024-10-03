# block/models.py
# Define the data objects for our application

from django.db import models 

# Create your models here.

class Article(models.Model):
    '''Encapsulate the idea of one Article by some Author.'''

    # data attributes of an Article:
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)


    def __str__(self):
        '''Return a string representation of the object.'''

        return f'{self.title} by {self.author}'

        #quiz Q when do you need to run makemigrations command