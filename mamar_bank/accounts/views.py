from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import  userRegistrationForm,userUpdateForm
from django.views.generic import FormView
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
# Create your views here.

class userRegistrationView(FormView):
    template_name='user_regestration.html'
    form_class=userRegistrationForm
    success_url=reverse_lazy('home')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user=form.save()
        print(user)
        login(self.request, user)
        return super().form_valid(form)
class userLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class userLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class userUpdateView(View):
    template_name='profile.html'
    def get(self,request):
        form=userUpdateForm(instance=request.user)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=userUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,self.template_name,{'form':form})
        
    