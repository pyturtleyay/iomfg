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
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], 
            password = cd['password'])
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled Account')
        else : 
            return HttpResponse('Invalid Login')
       
    else:
        form = LoginForm()
    return render(request, 'store/templates/registration/login.html', {'form' : form})

@login_required
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)
