from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket, Order
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user_login = request.POST['username']
            user_password = request.POST['password']
            user = auth.authenticate(username = user_login, password = user_password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:index'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def bucket(request):
    username = auth.get_user(request)
    basket = Basket.objects.filter(user = request.user)
    countof_basket_elems = len(list(Basket.objects.filter(user=request.user)))

    context = {'user': username, 'basket': basket, 'basket_count': countof_basket_elems}
    return render(request, 'users/bucket.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    orders = Order.objects.filter(user=request.user)
    context = {'form': form, 'orders': orders}

    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))



