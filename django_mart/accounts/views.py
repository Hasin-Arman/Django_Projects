from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib.auth import login,logout,authenticate
from cart.models import Cart,cartItem
# Create your views here.

def get_or_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def user_register(request):
    form=registerForm(request.POST)
    if form.is_valid():
        user=form.save()
        login(request, user)
        return redirect('profile')
    return render(request,'register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        cart_id=Cart.objects.filter(cart_id=get_or_create_session(request)).exists()
        # cart=Cart.objects.get(cart_id=get_or_create_session(request))
        if cart_id:
            cart_item=cartItem.objects.filter(cart=cart)
            for item in cart_item:
                item.user=user
                item.save()
        login(request, user)
        return redirect('profile')
    return render(request,'signin.html')

def user_profile(request):
    return render(request,'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')