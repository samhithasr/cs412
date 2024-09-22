##hw/views.py
##description: write view functions to handle URL requests for the hw app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# Create your views here.
# def home(request):
#     '''Handle the main URL for the hw app.''' #docstring

#     response_text = f'''
#     Hello, world! <br>
#     This page was generated at {time.ctime()}.
#     '''

#     #create and return response to client
#     return HttpResponse(response_text)

def home(request):
    '''
    Function to handle the URL request for /hw (home page).
    Delegate rendering to the template hw/home.html.
    '''
    #use this template to render the response
    template_name = 'hw/home.html'

    #create a dictionary of context variables for the template:
    context = {
        "current_time" : time.ctime(), 
        "letter1" : chr(random.randint(65,90)), #a letter from A...Z
        "letter2" : chr(random.randint(65,90)), 
        "number" : random.randint(1,10), # number from 1-10
    }

def about(request):
    '''
    Function to handle the URL request for /hw (home page).
    Delegate rendering to the template hw/home.html.
    '''
    #use this template to render the response
    template_name = 'hw/about.html'

    #create a dictionary of context variables for the template:
    context = {
        "current_time" : time.ctime(), 
        "letter1" : chr(random.randint(65,90)), #a letter from A...Z
        "letter2" : chr(random.randint(65,90)), 
        "number" : random.randint(1,10), # number from 1-10
    }

    #delegate rendering work to the template
    return render(request, template_name, context)