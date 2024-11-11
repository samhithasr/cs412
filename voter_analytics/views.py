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
    paginate_by = 100 # show 50 results per page

    def get_queryset(self) -> QuerySet[Any]:
        '''Limit the voters to a small number of records'''

        # default query set is all of the records:
        qs = super().get_queryset()
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            qs = qs.filter(party=party)
        if 'min' in self.request.GET:
            dob_min = self.request.GET.get('min')
            qs = qs.filter(dob__year__gte=dob_min).order_by('dob')
        if 'max' in self.request.GET:
            dob_max = self.request.GET.get('max')
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


class ShowVoterDetailView(DetailView):
    '''A view to show the details of a specific voter.'''
    template_name = 'voter_analytics/show_voter.html'
    model = Voter
    context_object_name = 'voter'

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     voter = Voter.objects.get(pk=self.kwargs['pk'])

    #     return context


    # overrides default get_context_data so that Foreign Key can
    # be used by site get a specific Profile's status messages and friends
    # def get_context_data(self, **kwargs: any):

    #     context = super().get_context_data(**kwargs)
    #     profile = Profile.objects.get(pk=self.kwargs['pk'])

    #     context['statuses'] = profile.get_status_messages()
    #     context['friends'] = profile.get_friends()
    #     return context

# def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
#         # get the superclass version of context
#         context = super().get_context_data(**kwargs)
#         r = context['r'] # obtain the single Result instance

#         # get data: half-marathon splits
#         first_half_seconds = (r.time_half1.hour * 3600 + 
#                               r.time_half1.minute * 60 + 
#                               r.time_half1.second)
        
#         second_half_seconds = (r.time_half2.hour * 3600 + 
#                               r.time_half2.minute * 60 + 
#                               r.time_half2.second)
        
#         # build a pie chart
#         x = ['first half time', 'second half time']
#         y = [first_half_seconds, second_half_seconds]
#         # print(f'x={x}')
#         # print(f'y={y}')
#         fig = go.Pie(labels=x, values=y)
#         pie_div = plotly.offline.plot({'data':[fig]},
#                                       auto_open=False,
#                                       output_type='div')
        
#         # add the pie chart to the context
#         context['pie_div'] = pie_div

#         # create a bar chart with the number of runners passed and who passed by
#         x = [f'runners passed by {r.first_name}',
#              f'runner who passed {r.first_name}']
#         y = [r.get_runners_passed(),
#              r.get_runners_passed_by()]
#         # print(f'x={x}')
#         # print(f'y={y}')
#         fig = go.Bar(x=x, y=y)
#         bar_div = plotly.offline.plot({'data':[fig]},
#                                       auto_open=False,
#                                       output_type='div')
#         # add this to the context data for use in the template
#         context['bar_div'] = bar_div

#         return context