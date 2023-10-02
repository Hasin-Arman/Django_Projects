from django.urls import path
from . import views
urlpatterns = [
    path('deposit/',views.deposit_view.as_view(),name='deposit'),
    path('withdraw/',views.withdraw_view.as_view(),name='withdraw'),
    path('loan/',views.loan_request_view.as_view(),name='loan'),
    path('transaction_report/',views.TransactionReportView.as_view(),name='report'),
    path('loan_pay/<int:loan_id>/',views.payLoanView.as_view(),name='pay_loan'),
    path('show_loans/',views.LoanListView.as_view(),name='show_loans'),
]
