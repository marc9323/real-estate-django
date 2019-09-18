from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# methods and urls linked to them

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
