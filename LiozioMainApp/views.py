from django.shortcuts import HttpResponse, HttpResponseRedirect, render # type: ignore
from django.urls import reverse # type: ignore
from django.views.defaults import page_not_found # type: ignore

# from .services import _services, sp_services
# from .services import tabs
from random import randrange

# Create your views here.

# Create 404 view

def error_404_view(request, exception):
   
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

# Create Home View

def index(request):

    context = {
            'active_page': 'home',
        }
    
    return render(request, 'LiozioMainApp/index.html',context)


def about(request):
    context = {
        'active_page': 'about',
    }
    
    return render(request, 'LiozioMainApp/about.html', context)

def services(request):
    context = {
        'active_page': 'services',
    }
    
    return render(request, 'LiozioMainApp/services.html', context)

def projects(request):
    context = {
        'active_page': 'projects',
    }
    
    return render(request, 'LiozioMainApp/projects.html', context)

def contact(request):
    context = {
        'active_page': 'contact',
    }
    
    return render(request, 'LiozioMainApp/contact.html', context)

