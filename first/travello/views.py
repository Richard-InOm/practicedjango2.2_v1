from django.shortcuts import render
from .models import Destination
from django.contrib.auth.models import User, auth

# Create your views here.
dests = Destination.objects.all()
def index(request):  
    return render(request, 'index.html', {'dests': dests})
def destination(request):
    if request.method == 'POST':
        name = request.POST['dest']
        return render(request, 'destination.html', {'name': name})
    else:
        return render(request, 'destination.html')