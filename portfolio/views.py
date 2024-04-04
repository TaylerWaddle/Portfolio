from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, DetailView, ListView

from .models import Project, Blog, About

# Create your views here.
class Index(TemplateView):
    template_name = 'portfolio/index.html'

# Project Views
class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

# Blog Views
class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class AboutTemplateView(TemplateView):
    template_name = 'portfolio/about.html'


