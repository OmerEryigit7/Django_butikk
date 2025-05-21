from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import ProductForm
from .models import ProductInfo

def store(request):
    products = ProductInfo.objects.all()
    return render(request, 'store.html', {'products': products})

def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = ProductForm()
    return render(request, 'register_product.html', {'form': form})

def get_product_info(request, pk):
    product = get_object_or_404(ProductInfo, pk=pk)
    return render(request, 'product_page.html', {'product': product})


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
    
def add_to_cart(request, pk): 
    if request.method == 'POST':
        
        product = get_object_or_404(ProductInfo, pk=pk)

        cart = request.session.get('cart', {})
        print(cart)

        if str(pk) in cart:
            cart[str(pk)] += 1
        else:
            cart[str(pk)] = 1
        
        request.session['cart'] = cart

        
        return render(request, 'product_page.html', {'product': product})

def get_cart(request):
    cart = request.session.get('cart', {})
    print(cart)

    if not cart or cart =={}:
        messages.error(request, 'Handlekurven er tom')
        return render(request, 'cart.html')
   
    else:
        products = []

        for product_pk, quantity in cart.items():
            product = get_object_or_404(ProductInfo, pk=product_pk)
            price_of_quantity = product.price * quantity

            products.append({
                'product_info': product,
                'quantity': quantity,
                'price_of_quantity': price_of_quantity
            })

            print(products)
        return render(request, 'cart.html', {'products': products})