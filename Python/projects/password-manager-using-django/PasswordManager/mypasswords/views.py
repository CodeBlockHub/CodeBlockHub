from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Password

def index(request):
    if request.method == 'POST':
        website = request.POST['website']
        username = request.POST['username']
        password = request.POST['password']
        new_entry = Password(website=website, username=username, password=password)
        new_entry.save()
        return redirect('index')
    else:
        passwords = Password.objects.all()
        return render(request, 'index.html', {'passwords': passwords})