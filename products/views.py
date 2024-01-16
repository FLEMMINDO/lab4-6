import random
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import Product_Category, Product, Basket, Order

def contact(request):
    return render(request, 'products/contact.html')

def index(request):
    return render(request, 'products/index.html')

def about(request):
    return render(request, 'products/about.html')

def shop(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 6
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'products': products_paginator,
        'categories': Product_Category.objects.all()
    }
    return render(request, 'products/shop.html', context)

def shop_single(request):
    return render(request, 'products/shop-single.html')

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)

    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.filter(id = basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def make_order(request):
    random_num = random.randint(2345678909800, 9923456789000)
    Order.objects.create(user = request.user, number = random_num)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

