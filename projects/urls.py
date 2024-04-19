from django.urls import path
from .views import render_projects, storytelling_ai

# Name of the app
app_name = 'projects'

urlpatterns = [
    # Name of the url is 'projects'
    path('', render_projects, name='projects'),
    path('storytelling-ai/', storytelling_ai, name='storytelling_ai'),
]