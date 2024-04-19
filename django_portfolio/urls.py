from django.contrib import admin
from django.urls import path, include
from portfolio import views
from helpers.views import handle_not_found

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('projects/', include('projects.urls')),
]

handler404 = handle_not_found