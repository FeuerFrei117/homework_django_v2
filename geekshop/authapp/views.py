from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop | Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop | Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Изменения успешно сохранены')
            form.save()
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)

    """Одно из решений подсчета общей суммы и кол. товара"""
    # total_quantity = 0
    # total_sum = 0
    # baskets = Basket.objects.filter(user=request.user)
    # for basket in baskets:
    #     total_quantity += basket.quantity
    #     total_sum = basket.sum()
    """total_quantity и total_sum передаем в context и дальше в шаблон"""

    """Еще одно решение"""
    # baskets = Basket.objects.filter(user=request.user)
    # total_quantity = sum(basket.quantity for basket in baskets)
    # total_sum = sum(basket.sum() for basket in baskets)


    context = {
        'title': 'Geekshop | Профайл',
        'form': UserProfileForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user),

    }
    return render(request, 'authapp/profile.html', context)


def logaut(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
