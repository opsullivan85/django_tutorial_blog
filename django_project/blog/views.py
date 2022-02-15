from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    '''
    home page
    '''
    return render(request, 'blog/home.html', {})


def about(request):
    '''
    about page
    '''
    return render(request, 'blog/home.html', {})
