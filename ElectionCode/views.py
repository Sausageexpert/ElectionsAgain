from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'ElectionCode/homepage.html', {'pageName':'Voting Page'})

def live(request):
    return render(request, 'ElectionCode/live.html', {'pageName':'Live Poll'})
    