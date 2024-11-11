# File: voter_analytics/views.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 11/11/2024
# Description: The views file for the voter_analytics application.

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Voter

import plotly
import plotly.graph_objects as go

# Create your views here.
class VotersListView(ListView):
    '''View to show a list of voters.'''

    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100 # show 50 results per page

    def get_queryset(self) -> QuerySet[Any]:
        '''Limit the voters to a small number of voters'''

        # default query set is all of the voters, but get_qs here
        # can filter for party, birth year, voter score, and if 
        # a voter has voted in a specific election.
        qs = super().get_queryset()
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            qs = qs.filter(party=party)
        if 'min' in self.request.GET:
            dob_min = self.request.GET.get('min')
            # Chronological order
            qs = qs.filter(dob__year__gte=dob_min).order_by('dob')
        if 'max' in self.request.GET:
            dob_max = self.request.GET.get('max')
            # Reverse chronological order
            qs = qs.filter(dob__year__lte=dob_max).order_by('-dob')
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            qs = qs.filter(voter_score=voter_score)
        if 'v20state' in self.request.GET:
            qs = qs.filter(v20state=True)
        if 'v21town' in self.request.GET:
            qs = qs.filter(v21town=True)
        if 'v21primary' in self.request.GET:
            qs = qs.filter(v21primary=True)
        if 'v22general' in self.request.GET:
            qs = qs.filter(v22general=True)
        if 'v23town' in self.request.GET:
            qs = qs.filter(v23town=True)
        return qs

class GraphListView(ListView):
    '''View to show graphs for voter data.'''
    template_name = 'voter_analytics/graphs.html'
    model = Voter

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Override the default get_context_data so that
        graphs can be generated (using Plotly).'''
        context = super().get_context_data(**kwargs)

        # These if statements check the URL for queries
        voters = Voter.objects.all()
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            voters = voters.filter(party=party)
        if 'min' in self.request.GET:
            dob_min = self.request.GET.get('min')
            # Given year is the minimum birth year
            voters = voters.filter(dob__year__gte=dob_min)
        if 'max' in self.request.GET:
            dob_max = self.request.GET.get('max')
            # Given year is the maximum birth year
            voters = voters.filter(dob__year__lte=dob_max)
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            voters = voters.filter(voter_score=voter_score)
        if 'v20state' in self.request.GET:
            voters = voters.filter(v20state=True)
        if 'v21town' in self.request.GET:
            voters = voters.filter(v21town=True)
        if 'v21primary' in self.request.GET:
            voters = voters.filter(v21primary=True)
        if 'v22general' in self.request.GET:
            voters = voters.filter(v22general=True)
        if 'v23town' in self.request.GET:
            voters = voters.filter(v23town=True)
        context['voters'] = voters

        # Get the list of dates of birth, and then the years
        dobs = voters.values_list('dob', flat=True)
        dob_years = [dob.year for dob in dobs]

        # Generate histogram for birth years
        fig = go.Figure(data=[go.Histogram(x=dob_years)])
        fig.update_layout(
            title='Voter Birth Years', 
            xaxis_title='Birth Year',            
            yaxis_title='Count',
        )
        bar_div = plotly.offline.plot(fig,auto_open=False,output_type='div')

        # Pass it to context
        context['bar_div'] = bar_div

        # Create counts for the pie chart
        parties = voters.values_list('party', flat=True)
        party_counts = {}
        for party in parties:
            if party in party_counts:
                party_counts[party] += 1
            else:
                party_counts[party] = 1
        # Create labels for the pie chart
        x = list(parties.distinct())
        
        # Build pie chart
        fig2 = go.Figure(data=go.Pie(labels=x, values=list(party_counts.values())))
        fig2.update_layout(
            title='Party Affiliations Pie Chart',
        )
        pie_div = plotly.offline.plot(fig2, auto_open=False, output_type='div')

        # Pass to context
        context['pie_div'] = pie_div

        # Values for voter score histogram
        scores = voters.values_list('voter_score', flat=True)

        # Build histogram for voter scores
        fig3 = go.Figure(data=[go.Histogram(x=list(scores))])
        fig3.update_layout(
            title='Voter Scores', 
            xaxis_title='Score',            
            yaxis_title='Count',
        )
        bar2_div = plotly.offline.plot(fig3,auto_open=False,output_type='div')

        # Pass to context
        context['bar2_div'] = bar2_div

        return context

class ShowVoterDetailView(DetailView):
    '''A view to show the details of a specific voter.'''
    template_name = 'voter_analytics/show_voter.html'
    model = Voter
    context_object_name = 'voter'