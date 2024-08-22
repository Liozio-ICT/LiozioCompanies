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
    # tabservices = tabs
    # tabservices_title = list(tabs.keys())
    # context = {
    #     "titles": tabservices_title,
    #     "tabs": tabservices,
    #     "title": "Home",
    #     "link": "index"
    # }
    return render(request, 'LiozioMainApp/index.html')

