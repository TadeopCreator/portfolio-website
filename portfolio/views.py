from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail

# Create your views here.
def home(request):
    projects = Project.objects.all()    

    # Send an email
    print('send an email')
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        send_mail(
            'Portfolio Contact from {} | {}'.format(name, subject),
            message,
            email,
            ['tadeo.deluca2002@gmail.com']
        )
        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'home.html', {'projects': projects})