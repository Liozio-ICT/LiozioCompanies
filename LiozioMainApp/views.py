from django.shortcuts import HttpResponse, HttpResponseRedirect, render # type: ignore
from django.urls import reverse # type: ignore
from django.views.defaults import page_not_found # type: ignore

# from .services import _services, sp_services
from .data import projects_data
from random import randrange
from .careers import openings

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
        "projects" : projects_data,
        'active_page': 'projects',
    }
    
    return render(request, 'LiozioMainApp/projects.html', context)

def project(request, slug):
    all_projects = projects_data
    projects_length = len(all_projects)
    single_project = next(
        _project for _project in projects_data if _project['slug'] == slug)
    
    other_projects = [
        _project for _project in projects_data if _project['slug'] != slug
    ]
    
    projects_length = len(other_projects)

    def generate_proj():
        start = randrange(0, projects_length)
        end = start + 2  # Ensuring exactly two items are selected
        if end <= projects_length:
            return start, end
        else:
            return generate_proj()
        
    range_val = generate_proj()

    # Select two items from the other projects
    two_items = [other_projects[item] for item in range(range_val[0], range_val[-1])]
    context = {
        "project": single_project,
        "project_content": single_project["description"].split("\n"),
        "thumbnail": single_project['image_url'],
        "title" : single_project['name'],
        "projects"  : two_items
    }
    return render(request, 'LiozioMainApp/project_details.html', context)

def contact(request):
    context = {
        'active_page': 'contact',
    }
    
    return render(request, 'LiozioMainApp/contact.html', context)

def careers(request):
    context = {
        "careers" : projects_data,
        "openings" : openings,
        'active_page': 'careers',
    }
    
    return render(request, 'LiozioMainApp/careers.html', context)


def career(request, slug):
    single_career = next(c for c in openings if c["slug"] == slug)
    more_careers = [c for c in openings if c["slug"] != slug]
    def generate_two(extras):
        extra_careers = []
        for x in range(2):
            extra_careers.append(extras[x])
        return extra_careers

    def break_description(desc_str):
        desc_list = desc_str.split("\n")
        return desc_list
    
    descriptions = break_description(single_career["description"])
    extra_two = generate_two(more_careers)
    print(extra_two)
    
    context = {
        "careers" : projects_data,
        "openings" : openings,
        "career" : single_career,
        'active_page': 'careers',
        "extra_careers" : extra_two,
        "descriptions" : descriptions
    }
    
    return render(request, 'LiozioMainApp/career.html', context)

