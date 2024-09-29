from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def show_form(request):
    '''Show the contact form.'''

    template_name = "formdata/form.html"
    return render(request, template_name)

def submit(request):
    '''
    Handle the submission.
    Read the form data from the request, 
    and send it back to a template.
    '''

    template_name = 'formdata/confirmation.html'
    print(request)

    # check that we have a POST request
    if request.POST:
        
        #print(request.POST)
        # read form data into python variables
        name = request.POST['name']
        color = request.POST['color']

        #package form data up as context variables for the template
        context = {
            'name': name,
            'color': color,
        }

        return render(request, template_name, context)

    ## handle GET request on this URL

    #redirect to correct URL
    return redirect("show_form")


    #return HttpResponse("Nope.")
    # template_name = "formdata/form.html"
    # return render(request, template_name)

    
