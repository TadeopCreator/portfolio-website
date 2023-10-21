from django.shortcuts import render
import sys

sys.path.append("/Users/tadeodeluca/Documents/django-portfolio/portfolio")
from portfolio.models import Project

# Create your views here.
def render_projects(request):
    # Get all project order by year descending
    projects = Project.objects.all().order_by('-year')
    
    return render(request, 'archive.html', {'projects': projects})
