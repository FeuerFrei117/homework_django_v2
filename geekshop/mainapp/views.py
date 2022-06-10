from django.shortcuts import render
import json
import os
from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open(os.getcwd() + '\\mainapp\\fixtures\\products.json', 'r', encoding='utf-8') as f:
        templates = json.load(f)

    context = {
        'title': 'GeekShop | Каталог',
        'list_groups': ProductCategory.objects.all(),
        'clothes': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
