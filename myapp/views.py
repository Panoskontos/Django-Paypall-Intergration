from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.


def home(request):
    basket = UserBasket.objects.filter(user=request.user)

    total = 0
    for i in basket:
        total += i.product.price

    products = Product.objects.all()
    context = {
        'basket': basket,
        'products': products,
        'total': total,
    }

    return render(request, 'myapp/home.html', context)


def add_in_basket(request, product_id):

    product = Product.objects.get(id=product_id)

    new = UserBasket(product=product, user=request.user)

    new.save()

    return redirect('home')


def remove_from_basket(request, product_id):
    product = Product.objects.get(id=product_id)

    basket = UserBasket.objects.filter(
        product=product, user=request.user).first()

    if basket is not None:
        basket.delete()

    return redirect('home')


# all = objects.all()
# one = objects.get()
# many or none = objects.filter()


def checkout(request):
    basket = UserBasket.objects.filter(user=request.user)
    total = 0
    for i in basket:
        total += i.product.price

    context = {
        'total': total,
    }
    return render(request, 'myapp/checkout.html', context)
