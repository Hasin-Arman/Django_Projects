from django.shortcuts import render,redirect
from cart.models import Cart,cartItem
from .forms import orderForm
from django.contrib.auth.models import User
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from store.models import Product
from .models import Order,Payment,OrderedProduct
# Create your views here.

def order_complete(request):
    return render(request,'order_complete.html')

def checkout(request):
    cart_item=None
    total=0
    tax=0
    grandtotal=0
    cart_item=cartItem.objects.filter(user=request.user)
    if cart_item.count() < 1:
        return redirect('store')
    for item in cart_item:
        total+=item.product.price * item.quantity
    tax=(2*total)//100
    grandtotal=total+tax
    if request.method == 'POST':
        form=orderForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.instance.order_total=grandtotal
            form.instance.tax=tax
            form.instance.ip=request.META.get('REMOTE_ADDR')
            saved_instance=form.save()
            form.instance.order_number=saved_instance.id
            form.save()
            return redirect(sslcommerz_payment_gateway(request,saved_instance.id,request.user.id,grandtotal))
    return render(request, 'place-order.html',{'cart_item':cart_item,'tax':tax,'total':total,'grandtotal':grandtotal})

@method_decorator(csrf_exempt,name='dispatch')
def success_view(request):
    data=request.POST
    user_id=data['value_b']
    user=User.objects.get(pk=user_id)
    payment=Payment.objects.create(
        user=user,
        payment_id=data['tran_id'],
        payment_method=data['card_issuer'],
        amount=data['store_amount'],
        status=data['status']
    )
    payment.save()
    
    order=Order.objects.get(order_number=data['value_a'],user=user,is_ordered=False)
    order.is_ordered=True
    order.save()
    
    cart_items=cartItem.objects.filter(user=user)
    for item in cart_items:
        product=Product.objects.get(id=item.product.id)
        orderedProdcut=OrderedProduct(
            user=user,
            product=product,
            order=order,
            payment=payment,
            quantity=item.quantity,
            ordered=True
        )
        orderedProdcut.save()
        product.stock-=item.quantity
        product.save()
    
    cart_items.delete()
    return redirect('complete')
