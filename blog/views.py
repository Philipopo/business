from django.shortcuts import render
from django.http import HttpResponse

def handle_not_found(request,exception):
    return render(request, 'not-found.html')

def home(request):
    return render(request, 'home.html', {})
