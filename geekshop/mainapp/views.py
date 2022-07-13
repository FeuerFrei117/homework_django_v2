from django.shortcuts import render
import json
import os

from django.views.generic import DetailView

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


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'
    # context_object_name = 'product'


    def get_context_data(self,**kwargs):
        """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context




















