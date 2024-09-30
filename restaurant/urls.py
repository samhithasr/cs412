## restaurant/urls.py
## description: URL patterns for the qotd app

from django.urls import path #django.urls is a library for url management, path implements
from django.conf import settings #.conf configuration package; importing settings so file knows about project level settings
from . import views #from . = current directory, . import views imports [views.py] from current directory

#all of the URLs that are part of this app
urlpatterns = [
    path(r'', views.home, name="home"), #letter r means can support regular expressions
    path(r'confirmation', views.confirmation, name="confirmation"),
    path(r'order', views.order, name="order"),
]