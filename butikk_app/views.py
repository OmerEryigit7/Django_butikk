from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import ProductForm

def store(request):
     return render(request, 'store.html')

def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = ProductForm()
    return render(request, 'register_product.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.error(request, 'Feil brukernavn eller passord.')
    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            messages.error(request, 'Passordene samsvarer ikke.')
            return render(request, 'register_user.html')
    
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Denne e-posten er allerede registrert.')
            return render(request, 'register_user.html')

        user = User.objects.create_user(first_name = first_name, last_name = last_name, username=email, password=password)
        user.save()

        login(request, user)
        return redirect('store')
    else:
        return render(request, 'register_user.html')

