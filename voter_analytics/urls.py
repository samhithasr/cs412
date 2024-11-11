# File: voter_analytics/urls.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 11/09/2024
# Description: URL patterns for the voter_analytics app

from django.urls import path
from . import views 
from .views import VotersListView, ShowVoterDetailView, GraphListView
urlpatterns = [
    # map the URL (empty string) to the view
    path(r'', views.VotersListView.as_view(), name='home'),
    path(r'voters', views.VotersListView.as_view(), name='voters'),
    path(r'voter/<int:pk>', views.ShowVoterDetailView.as_view(),name='show_voter'),
    path(r'graphs', views.GraphListView.as_view(),name='graphs'),
    # path(r'results', views.ResultsListView.as_view(), name='results'),
    
]