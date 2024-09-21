## quotes/views.py
## description: write view functions to handle URL requests for the qotd app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# lists?

imageList = ["https://cdn.britannica.com/07/254207-050-A30BAFA8/James-Baldwin-author-1975.jpg",
            "https://beenhere.org/wp-content/uploads/2017/08/baldwin-james-2017-photo-by-dmitri-kasterine.jpg", 
            "https://media.newyorker.com/photos/59095c1fc14b3c606c10543d/master/w_1920,c_limit/Cole-James-Baldwin-Stranger-In-The-Village.jpg",
            "https://media.gq.com/photos/5c34dd88189eae07d4aabc75/master/w_1600,c_limit/James%20Baldwin-Acyde%20on%20James%20Baldwin_s%20Righteous%20Style-GQ020119-GYOL-02.jpg",
            "https://www.economist.com/cdn-cgi/image/width=960,quality=80,format=auto/content-assets/images/20240803_CUP502.jpg",
            ]

quoteList = ["Neither love nor terror makes one blind: indifference makes one blind.", 
            "You read something which you thought only happened to you, and you discover that it happened 100 years ago to Dostoyevsky. This is a very great liberation for the suffering, struggling person, who always thinks that he is alone. This is why art is important.", 
            "There are so many ways of being despicable it quite makes one's head spin. But the way to be really despicable is to be contemptuous of other people's pain.",
            "Children have never been very good at listening to their elders, but they have never failed to imitate them.",
            "Trust life, and it will teach you, in joy and sorrow, all you need to know.",
            ]

# Create your views here.
# def home(request):
#     '''Handle the main URL for the hw app.''' #docstring

#     response_text = f'''
#     Hello, world! <br>
#     This page was generated at {time.ctime()}.
#     '''

#     #create and return response to client
#     return HttpResponse(response_text)

def home(request): #idk how to make this blank but i'll figure that out
    '''
    You'll need to make this a real docstring btw
    '''

    template_name = 'quotes/home.html'

    context = {
        "qotd" : random.choice(quoteList),
        "image": random.choice(imageList)
    }

    return render(request, template_name, context)

    # '''
    # Function to handle the URL request for /hw (home page).
    # Delegate rendering to the template hw/home.html.
    # '''
    # #use this template to render the response
    # template_name = 'hw/home.html'

    # #create a dictionary of context variables for the template:
    # context = {
    #     "current_time" : time.ctime(), 
    #     "letter1" : chr(random.randint(65,90)), #a letter from A...Z
    #     "letter2" : chr(random.randint(65,90)), 
    #     "number" : random.randint(1,10), # number from 1-10
    # }

def quote(request):
    '''
    You'll need to make this a real docstring btw
    '''
    template_name = 'quotes/quotes.html'

    context = {
        "qotd": random.choice(quoteList),
        "image": random.choice(imageList)
    }

    return render(request, template_name, context)



def show_all(request):
    '''
    You'll need to make this a real docstring btw
    '''
    template_name = 'quotes/show_all.html'

    context = {
        "quotes": quoteList,
        "images": imageList
    }

    return render(request, template_name, context)


def about(request):
    '''
    You'll need to make this a real docstring btw
    '''
    template_name = 'quotes/about.html'

    context = {
        "quotes": quoteList,
        "images": imageList
    }

    return render(request, template_name, context)



    # '''
    # Function to handle the URL request for /hw (home page).
    # Delegate rendering to the template hw/home.html.
    # '''
    # #use this template to render the response
    # template_name = 'hw/about.html'

    # #create a dictionary of context variables for the template:
    # context = {
    #     "current_time" : time.ctime(), 
    #     "letter1" : chr(random.randint(65,90)), #a letter from A...Z
    #     "letter2" : chr(random.randint(65,90)), 
    #     "number" : random.randint(1,10), # number from 1-10
    #}

    #delegate rendering work to the template
    #return render(request, template_name, context)
