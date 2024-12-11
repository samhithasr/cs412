# File: bookshelf/forms.py
# Author: Sam Somavarapu (samhitha@bu.edu), 11/29/2024
# Description: The bookshelf forms.py file. Used to create:
# new Profiles, write Reviews, add Books, update Profiles, 
# edit/delete Reviews, etc.

from django import forms
from .models import *


class CreateProfileForm(forms.ModelForm):
    '''A form for users to create a new Profile.'''
    class Meta: 
        '''Associate this HTML form with the Profile data model.'''
        model = Profile
        fields = ['username', 'display_name', 'email', 'icon', 'bio']

class CreateBookForm(forms.ModelForm):
    '''A form for users to add a Book.'''
    class Meta:
        '''Associate this HTML form with the Book data model.'''
        model = Book
        fields = ['title', 'author', 'year', 'isbn', 'description', 'cover']

class CreateBookshelfForm(forms.ModelForm):
    '''A form for users to create a Bookshelf.'''
    class Meta:
        '''Associate this HTML form with the Bookshelf data model.'''
        model = Bookshelf
        fields = ['name', 'description']

class CreateFriendForm(forms.ModelForm):
    '''A form for users to create a Friend relationship.'''
    class Meta: 
        '''Associate this HTML form with the Friend data model.'''
        model = Friend
        fields = ['profile2']

class CreateReviewForm(forms.ModelForm):
    '''A form for users to create a Review.'''
    class Meta:
        '''Associate this HTML form with the Review data model.'''
        model = Review
        fields = ['text', 'star']

class CreateCommentForm(forms.ModelForm):
    '''A form for users to create a Comment.'''
    class Meta: 
        '''Associate this HTML form with the Comment data model.'''
        model = Comment
        fields = ['text']

class UpdateBioForm(forms.ModelForm):
    '''A form for users to update their Profile bio.'''
    class Meta:
        '''Associate this HTML form with the Profile data model.'''
        model = Profile
        fields = ['bio', 'display_name']

class UpdateBookForm(forms.ModelForm):
    '''A form for users to update Book details.'''
    class Meta:
        '''Associate this HTML form with the Book data model.'''
        model = Book
        fields = ['title', 'author', 'year', 'isbn', 'description', 'cover']

class UpdateReviewForm(forms.ModelForm):
    '''A form for users to update a Review.'''
    class Meta:
        '''Associate this HTML form with the Review data model.'''
        model = Review
        fields = ['text', 'star']

class AddBookForm(forms.Form):
    '''A form for users to add a Book to a Bookshelf.'''
    class Meta:
        '''Associate this HTML form with the Book data model.'''
        model = Book
        fields = ['author', 'title', 'year', 'isbn', 'description', 'cover']