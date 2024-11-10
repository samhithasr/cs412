from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Voter

# Create your views here.
class VotersListView(ListView):
    '''View to show a list of voters.'''

    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 50 # show 50 results per page

    def get_queryset(self) -> QuerySet[Any]:
        '''Limit the voters to a small number of records'''

        # default query set is all of the records:
        qs = super().get_queryset()
        # return qs[:25] # limit to 25 records
        
        # handle search form/URL parameters:
        if 'first' in self.request.GET:

            first = self.request.GET['first']
            # filter the Results by this parameter
            qs = Voter.objects.filter(first__icontains=first)

        return qs