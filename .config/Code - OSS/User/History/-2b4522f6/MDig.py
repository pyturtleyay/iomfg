from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def store(request):
    return HttpResponse("Hello")

def user_login(request):
    if request.method=='POST':
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        print(userEmail, userPassword)
        user = authenticate(request, username = userEmail, password = userPassword)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled Account')    
    return render(request, '/home/pyturtle_/Documents/ESHOPPING/ecommerce/store/templates/registration/login.html')

@login_required
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)
