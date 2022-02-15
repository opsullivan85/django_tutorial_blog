from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'opsullivan85',
        'title': 'Blog Post 1',
        'content': 'Hello World!',
        'date_posted': '2022/02/15'
    },
    {
        'author': 'Anonomous',
        'title': 'Blog Post 2',
        'content': 'Hi Earth!',
        'date_posted': '2022/02/16'
    }
]

def home(request):
    '''
    home page
    '''
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    '''
    about page
    '''
    return render(request, 'blog/about.html', {'title': 'about'})
