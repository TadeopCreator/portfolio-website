from django.shortcuts import render
import sys

#sys.path.append("/Users/tadeodeluca/Documents/django-portfolio/portfolio")
#from portfolio.models import Project

# Create your views here.
def render_projects(request):
    return render(request, 'archive.html')
