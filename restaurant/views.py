## restaurant/views.py
## description: write view functions to handle URL requests for the restaurant app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random



# Create your views here.

def home(request): 
    '''
    note to self: CHANGE DOCSTRINGS!!!!!!!
    Function to handle the URL request for /restaurant (restaurant home page)
    Delegate rendering to the template restaurant/main.html
    '''

    template_name = 'restaurant/main.html'

    return render(request, template_name)

def order(request):
    '''
    Show the order form.
    '''
    specials = ["Salad:4", "Milkshake:6", "Nachos:5", "Corn Dog:3"]
    today_special = random.choice(specials)

    val = today_special.split(':')
    special_item = val[0]
    special_price = val[1]

    context = {
        'special': special_item,
        'special_price': special_price,
    }


    template_name = 'restaurant/order.html'
    return render(request, template_name, context)

def confirmation(request):
    '''
    Handle the order submission.
    Read the form data from the request, 
    and send it back to a template.
    Presented to the client as
    an order confirmation.
    '''
    template_name = 'restaurant/confirmation.html'
    print(request)

    if request.POST:
        name = request.POST['name']
        instructions = request.POST['instructions']
        phone = request.POST['phone']
        email = request.POST['email']
        ordered = request.POST.getlist('menu') # Should get a list of the items that have been checked from the menu
        burger = request.POST.getlist('burger')
        # current_time = time.ctime()
        # total = sum([int(price) for price in ordered]) # Final order total

        wait = random.randint(1800,3600) # 30-60 mins in seconds
        ready_time = time.ctime(time.time() + wait)
        # ready_time_str = time.ctime(ready_time) # makes ready_time readable...? Might get rid of this depending on what it looks like
        #ready_time_str = time.strftime("%H:%M:%S", ready_time)

        food = []
        prices = []
        toppings = []
        total = 0
        for item in ordered:
            val = item.split(':')
            prices.append(int(val[1]))
            # food.append(val[0])
            if(val[0] == "Burger"):
                for t in burger:
                    toppings.append(t)
                food.append(val[0] + " $5 (" + ", ".join(toppings) + ")")
            else:
                food.append(val[0] + " $" + val[1])
        total = sum(prices)


        context = {
            'name': name,
            'instructions': instructions,
            'phone': phone,
            'email': email,
            # 'current_time': current_time,
            'ordered': food,
            'total': total,
            'ready': ready_time, # This is the line you change if format is weird
        }

        return render(request, template_name, context)
