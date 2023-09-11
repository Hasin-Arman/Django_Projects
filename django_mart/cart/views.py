from django.shortcuts import render,redirect
from store.models import Product
from .models import Cart,cartItem
# Create your views here.
def get_or_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def user_cart(request):
    cart_item=None
    total=0
    tax=0
    grandtotal=0
    session=get_or_create_session(request)
    if request.user.is_authenticated:
        cart_item=cartItem.objects.filter(user=request.user)
        for item in cart_item:
            total+=item.product.price * item.quantity
        tax=(2*total)//100
        grandtotal=total+tax
    else:
        cart=Cart.objects.filter(cart_id=session).exists()
        if cart:
            get_cart=Cart.objects.get(cart_id=session)
            cart_item=cartItem.objects.filter(cart=get_cart)
            for item in cart_item:
                total+=item.product.price * item.quantity
            tax=(2*total)//100
            grandtotal=total+tax
    return render(request, 'cart.html',{'cart_item':cart_item,'tax':tax,'total':total,'grandtotal':grandtotal})


def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    session=get_or_create_session(request)
    if request.user.is_authenticated:
        cart_item=cartItem.objects.filter(user=request.user,product=product).exists()
        if cart_item:
            item=cartItem.objects.get(product=product)
            item.quantity+=1
            item.save()
        else:
            item=cartItem.objects.create(
                product=product,
                quantity=1,
                user=request.user
            )
            item.save()    
    else: 
        cart_id=Cart.objects.filter(cart_id=session).exists()
        if cart_id:
            cart_item=cartItem.objects.filter(product=product).exists()
            if cart_item:
                item=cartItem.objects.get(product=product)
                item.quantity+=1
                item.save()
            else:
                cart_id=Cart.objects.get(cart_id=session)
                item=cartItem.objects.create(
                    cart=cart_id,
                    product=product,
                    quantity=1
                )
                item.save()
        else:
            cart=Cart.objects.create(
                cart_id=session
            )
            cart.save()
            cart_id=Cart.objects.get(cart_id=session)
            item=cartItem.objects.create(
                cart=cart_id,
                product=product,
                quantity=1
            )
            item.save()
            
    return redirect('cart')  

def remove_cart_item(request, product_id):
    product=Product.objects.get(id=product_id)
    session=request.session.session_key
    cart=Cart.objects.get(cart_id=session)
    cart_item=cartItem.objects.get(cart=cart,product=product)
    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart(request, product_id):
    product=Product.objects.get(id=product_id)
    session=request.session.session_key
    cart=Cart.objects.get(cart_id=session)
    cart_item=cartItem.objects.get(cart=cart,product=product)
    cart_item.delete()
    return redirect('cart')