# File: bookshelf/models.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 11/19/2024
# Define the data objects for the bookshelf application.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    Encapsulate the idea of a user Profile. 
    Provide necessary fields.
    '''

    # ForeignKey to the Django User class, allows for authentication/log in/etc.
    user = models.ForeignKey(User, related_name='bookshelf_user', on_delete=models.CASCADE)

    username = models.CharField(max_length=20, blank=False)
    display_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=120, blank=False)
    created = models.DateField(auto_now=True)
    icon = models.ImageField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.display_name} (@{self.username})'

class Bookshelf(models.Model):
    '''
    Encapsulates a Bookshelf. Contains a 
    ForeignKey to Profile; each Bookshelf
    has one Profile, one Profile can have
    many Bookshelves. Each Bookshelf tracks 
    Books for one user.
    '''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    name = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    # # In place of many-to-many; books can be on multiple shelves and shelves have multiple books
    # shelves = models.ForeignKey(Shelves, on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return [titles of books in this shelf]

    def __str__(self):
        return f'{self.name} (@{self.profile.username})'

    def get_books(self):
        '''Return the books in this Bookshelf.'''
        return Shelves.objects.filter(shelf=self)

class Author(models.Model):
    '''
    Encapsulates an Author. Contains:
    First name, last name.
    '''
    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.first} {self.last}'

class Book(models.Model):
    '''
    Encapsulates a Book. Contains:
    Author (ForeignKey), published year,
    ISBN, title, description, genre.
    '''

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    isbn = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(blank=True)
    # Genre as a dropdown box? 

    def __str__(self):
        return f'{self.title} by {self.author}'

class Shelves(models.Model):
    '''
    Contains ForeignKey relationships in place of
    Many-to-Many relationships. Basically: adds a 
    Book to a Shelf. 
    '''
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    shelf = models.ForeignKey(Bookshelf, on_delete=models.DO_NOTHING)
    added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.book.title} in {self.shelf.name} (@{self.shelf.profile.username})'

class Friend(models.Model):
    '''
    Encapsulates the idea of a Friend, which Profiles can have. 
    Connects Profiles to other Profiles. Provides fields needed
    for the Friend model.
    '''
    profile1 = models.ForeignKey(Profile, related_name="profile1",on_delete=models.DO_NOTHING)
    profile2 = models.ForeignKey(Profile, related_name="profile2",on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.profile1.username} & {self.profile2.username}"

class Review(models.Model):
    '''
    Encapsulates the idea of a Review for a book.
    ForeignKey to Book.
    '''
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    star = models.IntegerField() # Is there a way to make this 1-5

    def __str__(self):
        return f'Review for {self.book.title} by {self.profile.username}'

class Comment(models.Model):
    '''
    Encapsulates the idea of a Comment for a Bookshelf.
    ForeignKey to Bookshelf and Profile.
    '''
    bookhelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()


    def __str__(self):
        return f'Comment by {self.profile.username} on {self.bookshelf.name}'
