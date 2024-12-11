# File: bookshelf/views.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 11/28/2024

from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin # allows for user authentication


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import * ## import the models (e.g., Article)
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin # allows for user authentication
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login 
import random

# Create your views here.
# views:
# Create:
#     - CreateProfileView
#     - CreateBookView
#         - Check if book already exists
#     - CreateReviewView
#     - CreateBookShelfView
#     - CreateFriendView    

# Show/Read:
#     - ShowProfilePageView
#     - ShowBookshelfPageView
#     - ShowBookPageView
#     - ShowReviewsPageView
#     - Done: ShowAllProfilesView

# Update:
#     - UpdateBioView
#         - Update Profile bio
#     - UpdateBookView
#         - Update any of the Book fields
#     - UpdateReviewView
#         - Update Review

# Delete:
#     - DeleteReviewView
#         - Delete a review for a book (only by user who wrote it)
#     - DeleteCommentView
#         - Delete a comment for a shelf (user and shelf owner)

class ShowAllProfilesView(ListView):
    '''View to show all Profiles'''
    model = Profile
    template_name = 'bookshelf/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    '''The view to show a specific Profile.'''
    model = Profile
    template_name = 'bookshelf/show_profile.html'
    
    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['reviews'] = profile.get_reviews()
        context['bookshelves'] = profile.get_bookshelves()

        return context

class ShowAllBooksView(ListView):
    '''View to show all Books'''
    model = Book
    template_name = 'bookshelf/show_all_books.html'
    context_object_name = 'books'

class ShowBookView(DetailView):
    '''The view to show a specific Book.'''
    model = Book
    template_name = 'bookshelf/show_book.html'

    def get_context_data(self, **kwargs: any):
        '''Override the get_context_data method to add extra context for the book details.'''
        context = super().get_context_data(**kwargs)  # Inherit context from the superclass
        book = Book.objects.get(pk=self.kwargs['pk'])  # Retrieve the specific book using the primary key from the URL
        context['reviews'] = book.get_reviews()  # Get all reviews associated with the book
        context['shelves'] = book.get_shelves()  # Get all shelves that contain the book

        return context


class ShowBookshelfPageView(DetailView):
    '''The view to show a specific Bookshelf.'''
    model = Bookshelf
    template_name = 'bookshelf/show_bookshelf.html'

    def get_context_data(self, **kwargs: any):
        '''Override the get_context_data method to add context data specific to the bookshelf details.'''
        context = super().get_context_data(**kwargs)  # Inherit context from the superclass
        bookshelf = Bookshelf.objects.get(pk=self.kwargs['pk'])  # Retrieve the specific bookshelf using its primary key from the URL
        context['comments'] = bookshelf.get_comments()  # Get all comments associated with the bookshelf
        context['books'] = bookshelf.get_books()  # Get all books in the bookshelf

        return context  


class CreateReviewView(LoginRequiredMixin, CreateView):
    '''A view to create a Review for a Book.'''

    form_class = CreateReviewForm
    template_name = "bookshelf/create_review_form.html"

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')

    def get_context_data(self, **kwargs) -> dict[str, any]:
        # context from superclass
        context = super().get_context_data(**kwargs)
        # add Profile to context
        context['profile'] = Profile.objects.filter(user=self.request.user).first()
        context['book'] = Book.objects.get(pk=self.kwargs['pk']) # Get pk from url
        return context

    def get_success_url(self) -> str:
        '''Return URL to redirect to on success.'''
        book = Book.objects.get(pk=self.kwargs['pk'])
        return reverse('show_book', kwargs={'pk': book.pk})

    def form_valid(self, form):
        '''This method is called after the form is validated, before saving data to the database.'''
        # attach the current book to the review instance
        book = Book.objects.get(pk=self.kwargs['pk'])
        form.instance.book = book  # set the correct book for the review

        # attach the Profile identified by the current user to the review instance
        form.instance.profile = Profile.objects.filter(user=self.request.user).first()

        # save the review to database
        r = form.save()

        # delegate work to superclass version of this method
        return super().form_valid(form)

class CreateProfileView(CreateView):
    '''A view to create a new Profile and save it to the database.'''

    model = Profile
    form_class = CreateProfileForm
    template_name = "bookshelf/create_profile_form.html"

    def get_success_url(self):
        return reverse('book_show_profile', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs: any):
        '''Both UserCreationForm and CreateProfileForm in template'''
        context = super().get_context_data(**kwargs)
        create_form = UserCreationForm()
        context['create_form'] = create_form

        return context

    def form_valid(self, form):
        '''This method is called after the form is validated,
        before saving data to the database.'''

        # UserCreationForm with POST data
        create_form = UserCreationForm(self.request.POST)

        if form.is_valid() and create_form.is_valid():
            # save UserCreationForm to database
            user = create_form.save()
            # FK 
            form.instance.user = user
            # form.save()

            # log the user in
            login(self.request, user)

            # delegate valid form to superclass
            return super().form_valid(form)

        # if the form is invalid, return to it (superclass method)
        return super().form_invalid(form)

class CreateBookView(CreateView):
    '''A view to create a new Book, checking if it already exists.'''
    form_class = CreateBookForm
    template_name = 'bookshelf/create_book_form.html'

    def form_valid(self, form):
        # Check if the book already exists
        title = form.cleaned_data['title']
        author = form.cleaned_data['author']
        book = Book.objects.filter(title=title, author=author).first()
        if book:
            self.object = book
            return super().form_valid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_book', kwargs={'pk': self.object.pk})

class CreateBookshelfView(LoginRequiredMixin, CreateView):
    '''A view to create a new Bookshelf.'''
    form_class = CreateBookshelfForm
    template_name = 'bookshelf/create_bookshelf_form.html'

    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        # return reverse('show_profile', kwargs={'pk': profile.pk})
        return reverse('show_bookshelf', kwargs={'pk': self.object.pk})

class CreateFriendView(LoginRequiredMixin, CreateView):
    '''A view to create a Friend relationship.'''
    form_class = CreateFriendForm
    template_name = 'bookshelf/create_friend_form.html'

    def form_valid(self, form):
        form.instance.profile1 = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book_show_profile', kwargs={'pk': self.request.user.profile.pk})

class UpdateBioView(LoginRequiredMixin, UpdateView):
    '''A view to update the bio of a Profile.'''
    model = Profile
    form_class = UpdateBioForm
    template_name = 'bookshelf/update_bio_form.html'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    # def get_success_url(self):
    #     return reverse('show_profile', kwargs={'pk': self.object.pk})

    def get_success_url(self):
        '''Return the URL to redirect to after successfully updating the profile.'''

        # After updating, redirect to the profile's detail page
        profile = Profile.objects.filter(user = self.request.user).first()
        return reverse('book_show_profile', kwargs={'pk': profile.pk})


class UpdateBookView(LoginRequiredMixin, UpdateView):
    '''A view to update Book details.'''
    model = Book
    form_class = UpdateBookForm
    template_name = 'bookshelf/update_book_form.html'

    def get_success_url(self):
        return reverse('show_book', kwargs={'pk': self.object.pk})

class UpdateReviewView(LoginRequiredMixin, UpdateView):
    '''A view to update a Review.'''
    model = Review
    form_class = UpdateReviewForm
    template_name = 'bookshelf/update_review_form.html'

    def get_success_url(self):
        return reverse('show_book', kwargs={'pk': self.object.book.pk})

class DeleteReviewView(LoginRequiredMixin, DeleteView):
    '''A view to delete a Review.'''
    model = Review
    template_name = 'bookshelf/delete_review_form.html'

    def get_object(self):
        review = super().get_object()
        if review.profile.user != self.request.user:
            raise PermissionDenied("You can only delete your own reviews.")
        return review

    def get_success_url(self):
        return reverse('show_book', kwargs={'pk': self.object.book.pk})

class DeleteCommentView(LoginRequiredMixin, DeleteView):
    '''A view to delete a comment from a Bookshelf.'''
    model = Comment
    template_name = 'bookshelf/delete_comment_form.html'

    def get_object(self):
        comment = super().get_object()
        if comment.profile.user != self.request.user and comment.bookshelf.profile.user != self.request.user:
            raise PermissionDenied("You can only delete your own comments or comments on your bookshelf.")
        return comment

    def get_success_url(self):
        return reverse('show_bookshelf', kwargs={'pk': self.object.bookshelf.pk})

class DeleteBookshelfView(LoginRequiredMixin, DeleteView):
    '''A view to delete a bookshelf.'''
    model = Bookshelf
    template_name = 'bookshelf/delete_bookshelf_form.html'

    def get_queryset(self):
        # Ensure that only the logged-in user can delete their own bookshelf
        return self.model.objects.filter(profile__user=self.request.user)

    def get_success_url(self):
        # if self.request.user.is_authenticated and hasattr(self.request.user, 'profile'):
        #     return reverse('book_show_profile', kwargs={'pk': profile.pk})
        # else:
        #     return reverse('login')  # Adjust to the appropriate URL if needed
        return reverse('book_show_all_profiles')

class AddBookToShelfView(LoginRequiredMixin, CreateView):
    '''A view to add a Book to a Bookshelf.'''
    form_class = AddBookForm
    template_name = "bookshelf/add_book_form.html"

    def get_login_url(self) -> str:
        '''Return the URL of the login page.'''
        return reverse('login')

    def get_context_data(self, **kwargs) -> dict[str, any]:
        # context from superclass
        context = super().get_context_data(**kwargs)
        context['bookshelf'] = Bookshelf.objects.get(pk=self.kwargs['pk']) # Get pk from URL
        return context
        
    def get_success_url(self) -> str:
        '''Return URL to redirect to on success.'''
        return reverse('show_bookshelf', kwargs={'pk': self.kwargs['pk']}) # Redirect to the current bookshelf

    def form_valid(self, form):
        '''This method is called after the form is validated, 
        before saving data to the database.'''

        # Link the new book to the current bookshelf
        form.instance.bookshelf = Bookshelf.objects.get(pk=self.kwargs['pk'])

        # Save the new book instance
        form.save()

        # Delegate work to superclass version of this method
        return super().form_valid(form)
