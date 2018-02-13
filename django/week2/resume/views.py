from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
   '''
   Renders flashcard app home page
   '''
   return HttpResponse('Welcome to the Resume app!')
