from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import userAccountForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
class userRegistrationView(FormView):
    template_name='user_registration.html'
    form_class=userAccountForm
    success_url=reverse_lazy('register')
    
    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)

class userLoginView(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')

class userLogoutView(LogoutView):
    def get_success_url(self):
        logout(self.request)
        return reverse_lazy('homepage')

class userUpdateView(View):
    template_name = 'profile.html'
    def get(self,request):
        form=UserUpdateForm(instance=request.user)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(request,self.template_name,{'form':form})