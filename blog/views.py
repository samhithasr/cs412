# blog/views.py
# define the views for the blog app
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import * ## import the models (e.g., Article)s
from .forms import * ## import forms (like: CreateCommentForm)

# class-based view
class ShowAllView(ListView):
    '''the view to show all Articles'''
    model = Article # the model to display
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' # context variable to use in the template

class RandomArticleView(DetailView):
    '''Show the details for one article.'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'
    # pick one article at random:

    def get_object(self):
        '''Return one Article object chosen at random.'''

        # retrieve all articles
        all_articles = Article.objects.all()

        # return one at random
        return random.choice(all_articles)

class ArticleView(DetailView):
    '''Display one Article selected by primary key.'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'
    # pick one article at random:

    # def get_object(self):
    #     '''Return one Article object chosen at random.'''

    #     # retrieve all articles
    #     all_articles = Article.objects.all()

    #     # return one at random
    #     return random.choice(all_articles)

# class CreateCommentView(CreateView):
#     '''A view to create a Comment on an Article.
#     on GET: send back form to display
#     on POST: read/process form, save new Comment to database'''

#     form_class = CreateCommentForm
#     template_name = "blog/create_comment_form.html"

#     def get_success_url(self) -> str:
#         '''Return the URL to redirect to on success.'''
#         # return 'show_all' #a valid URL pattern
#         return reverse('show_all') # look up the URL called show_all