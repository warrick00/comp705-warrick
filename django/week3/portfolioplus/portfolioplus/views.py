from django.shortcuts import render

def home(request):
    """
    Renders home page
    """

    context = {} # and empty dictionary

    return render(request, 'home.html', context)
