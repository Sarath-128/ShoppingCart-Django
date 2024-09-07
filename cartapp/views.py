from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from myapp.models import appl
from .models import Cart, CartItems
import stripe

def Add_cart(request,book_id):

    book=appl.objects.get(id=book_id)
    if book.quantity > 0 :
        cart, created =Cart.objects.get_or_create(user=request.user)
        cart_item, item_created =CartItems.objects.get_or_create(cart=cart,book=book)

        if not item_created:
            cart_item.quantity +=1
            cart_item.save()    
    return redirect('viewcart')

    

def view_card(request):
    
    cart,created =Cart.objects.get_or_create(user=request.user)
    cart_items=cart.cartitems_set.all()
    cart_item=CartItems.objects.all()
    total_price=sum(item.book.price * item.quantity for item in cart_items)
    total_items=cart_items.count()
    

    context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}

    return render(request,'cart.html',context)

def increase_quantity(request,item_id):
    cart_item=CartItems.objects.get(id=item_id)

    if cart_item.quantity < cart_item.book.quantity :
        cart_item.quantity +=1
        cart_item.save() 

    return redirect('viewcart')

def decrease_quantity(request,item_id):
    cart_item=CartItems.objects.get(id=item_id)

    if cart_item.quantity > 1 :
        cart_item.quantity -=1
        cart_item.save() 

    return redirect('viewcart')

def remove_cart(request,item_id):
    try:
        cart_item=CartItems.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass

    return redirect('viewcart')


def create_checkout_session(request):
    cart_items = CartItems.objects.all()  # Consider filtering by user/session if necessary
    
    if cart_items:
        stripe.api_key = settings.STRIPE_SECRET_KEY

        if request.method == 'POST':
            line_items = []
            for cart_item in cart_items:
                if cart_item.book:
                    line_item = {
                        'price_data': {
                            'currency': 'INR',
                            'unit_amount': int(cart_item.book.price * 100),  # Multiply by 100 to convert to cents
                            'product_data': {
                                'name': cart_item.book.item
                            },
                        },
                        'quantity': 1,
                    }
                    line_items.append(line_item)  # Removed the comma

            if line_items:
                try:
                    checkout_session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=line_items,
                        mode='payment',
                        success_url=request.build_absolute_uri(reverse('success')),
                        cancel_url=request.build_absolute_uri(reverse('cancel')),
                    )
                    return redirect(checkout_session.url, code=303)
                except stripe.error.StripeError as e:
                    # Add some error logging here to handle Stripe API errors
                    print(f"Stripe Error: {e}")
                    return HttpResponse("Error in creating checkout session", status=500)
    else:
        return HttpResponse("Your cart is empty", status=400)

def success(request):
    cart_items=CartItems.objects.all()

    for cart_item in cart_items:
        product=cart_item.book
        if product.quantity >= cart_item.quantity :
            product.quantity -=cart_item.quantity
            product.save()

    cart_items.delete()

    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')