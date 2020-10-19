from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
#from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 rouse=cd['rouse'],
                 color=cd['color'],
                 color_type1=cd['color_type1'],
                 color_type2=cd['color_type2'],
                 color_type3=cd['color_type3'],
                 rp=cd['rp'],
                 quantity=cd['quantity'],
                 )
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    #messages.success(request, 'Удалено')
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})