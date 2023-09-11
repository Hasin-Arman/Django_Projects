from django.shortcuts import render,redirect
from first_app.forms import registrationForm,change_user_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash


# Create your views here.
def Signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=registrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account has been craeted successfully')
                form.save()
        else:
            form=registrationForm()
        return render(request, 'signup.html',{'form':form})
    else:
        return redirect('profile_page')

def home(request):
    return render(request, 'home.html')

def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile_page')
        else:
            form=AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile_page')
                
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=change_user_data(request.POST)
            if form.is_valid():
                messages.success(request, 'Account has been updated successfully')
                form.save()
        else:
            form=change_user_data(instance=request.user)
        return render(request, 'profile.html',{'form':form})
    else:
        return redirect('sign')

def Logout(request):
    logout(request)
    return redirect('login_page')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()	
                update_session_auth_hash(request,form.user)
                return redirect('profile_page')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login_page')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()	
                update_session_auth_hash(request,form.user)
                return redirect('profile_page')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login_page')
            