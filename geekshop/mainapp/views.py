from django.shortcuts import render
import json
import os


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open(os.getcwd() + '\\mainapp\\fixtures\\products.json', 'r', encoding='utf-8') as f:
        templates = json.load(f)
    context = {
        'title': 'GeekShop - Каталог',
        'list_groups': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'clothes': templates,
        # 'clothes': [{
        #     'name': 'Худи черного цвета с монограммами adidas Originals',
        #     'price': '6 090,00',
        #     'image': 'vendor/img/products/Adidas-hoodie.png',
        #     'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
        # }, {
        #     'name': 'Синяя куртка The North Face',
        #     'price': '23 725,00',
        #     'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
        #     'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
        # }, {
        #     'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        #     'price': '3 390,00',
        #     'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
        #     'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
        # }, {
        #     'name': 'Черный рюкзак Nike Heritage',
        #     'price': '2 340,00 руб.',
        #     'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
        #     'description': 'Плотная ткань. Легкий материал.'
        # }, {
        #     'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
        #     'price': '13 590,00',
        #     'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
        #     'description': 'Гладкий кожаный верх. Натуральный материал.'
        # }, {
        #     'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        #     'price': '2 890,00',
        #     'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
        #     'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
        # },
        # ]
    }
    return render(request, 'mainapp/products.html', context)
