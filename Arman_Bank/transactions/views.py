from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import TransactionModel
from .models import Deposit,Withdraw,Loan,Loan_paid
from .forms import depositForm,withdrawForm,loanForm
from django.contrib import messages
from django.views.generic import ListView
from datetime import datetime
from django.db.models import Sum
from django.views import View

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name='transaction_form.html'
    model=TransactionModel
    title=''
    success_url=reverse_lazy('report')
    
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({
            'account':self.request.user.account
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        })
        return context

class deposit_view(TransactionCreateMixin):
    form_class = depositForm
    title='deposit'
    
    def get_initial(self):
        initial={'transaction_type':Deposit}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        self.request.user.account.balance+=form.cleaned_data['amount']
        self.request.user.account.save(update_fields=['balance'])
        messages.success(self.request,f'{amount} deposited successfully')
        return super().form_valid(form)
    

class withdraw_view(TransactionCreateMixin):
    form_class = withdrawForm
    title='withdraw'
    
    def get_initial(self):
        initial={'transaction_type':Withdraw}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        self.request.user.account.balance-=form.cleaned_data['amount']
        self.request.user.account.save(update_fields=['balance'])
        messages.success(self.request,f'{amount} withdrawn successfully')
        return super().form_valid(form)
    
class loan_request_view(TransactionCreateMixin):
    form_class=loanForm
    title='Request For Loan'
    
    def get_initial(self):
        initial={'transaction_type':Loan}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        
        messages.success(self.request,f'Loan request for amount {amount} submitted successfully')
        return super().form_valid(form)
    

class TransactionReportView(LoginRequiredMixin,ListView):
    template_name='transaction_report.html'
    model=TransactionModel
    
    def get_queryset(self):
        queryset=super().get_queryset().filter(account = self.request.user.account)
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str,"%Y-%m-%d").date()
            end_date=datetime.strptime(end_date_str,"%Y-%m-%d").date()
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })
        return context
    
class payLoanView(LoginRequiredMixin,View):
    def get(self, request, loan_id):
        loan=TransactionModel.objects.get(id=loan_id)
        if loan.loan_approved:
            user_account=loan.account
            if(loan.amount < user_account.balance):
                user_account.balance-=loan.amount
                user_account.save()
                loan.balance_after_transaction=user_account.balance
                loan.transaction_type=Loan_paid
                loan.save()
                return redirect('show_loans')
            else:
                messages.error(request, f'you dont have enough balance to pay the loan')
        return redirect('show_loans')

class LoanListView(LoginRequiredMixin,ListView):
    model = TransactionModel
    template_name='loan_request.html'
    context_object_name='loans'
    def get_queryset(self):
        user_account = self.request.user.account
        queryset=TransactionModel.objects.filter(account=user_account,transaction_type=3)
        return queryset
    
            
            
        
    
    
    
    
    