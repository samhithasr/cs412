## blog/urls.py
## description: URL patterns for the hw app

from django.urls import path #django.urls is a library for url management, path implements
from django.conf import settings #.conf configuration package; importing settings so file knows about project level settings
from . import views #from . = current directory, . import views imports [views.py] from current directory
from .views import ShowAllView # our view class definition 

#all of the URLs that are part of this app
urlpatterns = [
    # path(r'', views.home, name="home"), #letter r means can support regular expressions
    # path(r'about', views.about, name="about"),
    path(r'', views.RandomArticleView.as_view(), name="random"),
    path(r'show_all', views.ShowAllView.as_view(), name="show_all"),
    path(r'article/<int:pk>', views.ArticleView.as_view(), name="article"), 
    # path(r'create_comment', views.CreateCommentView.as_view(), "create_comment"), ## 10/10
    path(r'article/<int:pk>/create_comment', views.ArticleView.as_view(), name="article"), 

]