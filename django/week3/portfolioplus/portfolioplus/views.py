from django.shortcuts import render

def home(request):
    """
    Renders home page
    """

    greeting = "Portfolio Plus - Ryan Warrick"
    # a dictionary with key word 'our_greeting' mapping to the varibale greeting defined above.

    context = {'our_greeting':greeting} # and empty dictionary

    return render(request, 'home.html', context)

def home(request):
    """
    Renders home page
    """

    greeting = "Portfolio Plus - Ryan Warrick"
    # a dictionary with key word 'our_greeting' mapping to the varibale greeting defined above.

    context = {'our_greeting':greeting} # and empty dictionary

    return render(request, 'home.html', context)
