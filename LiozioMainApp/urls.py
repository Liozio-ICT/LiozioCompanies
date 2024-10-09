
from django.urls import path # type: ignore

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    # path('about/<str:about_var>', views.about_more, name='about-more'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    # path('special/<slug:slug>', views.sp_service, name='services-special'),
    path('careers', views.careers, name='careers'),
    path('careers/<slug:slug>', views.career, name='career-detail'),
    path('projects', views.projects, name='projects'),
    path('projects/<slug:slug>', views.project, name='project-detail'),
]