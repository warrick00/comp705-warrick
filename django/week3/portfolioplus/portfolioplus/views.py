from django.shortcuts import render

def home(request):
    """
    Renders home page
    """

    greeting = "Portfolio Plus - Ryan Warrick"
    # a dictionary with key word 'our_greeting' mapping to the varibale greeting defined above.

    context = {'our_greeting':greeting} # and empty dictionary

    return render(request, 'home.html', context)

def resume(request):
    """
    Renders resume page
    """

    greeting = "Portfolio Plus - Ryan Warrick"
    # a dictionary with key word 'our_greeting' mapping to the varibale greeting defined above.

    context = {'our_greeting':greeting} # and empty dictionary

    return render(request, 'resume.html', context)

def portfolio(request):
    """
    Renders portfolio page
    """

    greeting = "Portfolio Plus - Ryan Warrick"
    # a dictionary with key word 'our_greeting' mapping to the varibale greeting defined above.

    context = {'our_greeting':greeting} # and empty dictionary

    return render(request, 'portfolio.html', context)

def contact(request):
    """
    Renders contact page
    """

    greeting = "Portfolio Plus - Ryan Warrick"
    # a dictionary with key word 'our_greeting' mapping to the varibale greeting defined above.

    context = {'our_greeting':greeting} # and empty dictionary

    return render(request, 'contact.html', context)
