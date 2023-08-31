from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
from .forms import LoginForm


def store(request):
    return HttpResponse("Hello")

def user_login(request):
    if request.method=='POST':
        pass
    return render(request, '/home/pyturtle_/Documents/ESHOPPING/ecommerce/store/templates/registration/login.html', {'form' : form})

@login_required
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)