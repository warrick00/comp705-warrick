from django.http import HttpResponse

def home(request):
    return HttpResponse('Portfolio Homepage')
