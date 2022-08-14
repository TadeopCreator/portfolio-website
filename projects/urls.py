from django.urls import path
from .views import render_projects

# Name of the app
app_name = 'projects'

urlpatterns = [
    # Name of the url is 'projects'
    path('', render_projects, name='projects'),
]