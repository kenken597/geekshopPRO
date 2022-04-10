from django.shortcuts import render
import os
import json

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)

def products(request):
    #file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop - Catalog',
    }
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)

# def products(request):
#     context = {
#         'title': 'Geekshop - catalog',
#         'products': [
#             {
#                 "name": "Худи чёрного цвета с монограммами adidas Originals",
#                 "price": "6 090,00",
#                 "description": "Мягкая ткань для свитшотов. Стиль и комфорт - это образ жизни.",
#                 "image": "vendor/img/products/Adidas-hoodie.png"
#             },
#
#             {
#                 "name": "Синяя куртка The North Face",
#                 "price": "23 725,00",
#                 "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и тёплый пуховый наполнитель.",
#                 "image": "vendor/img/products/Blue-jacket-The-North-Face.png"
#             },
#
#             {
#                 "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
#                 "price": "3 390,00",
#                 "description": "Материал с плющевой текстурой. Удобный и мягкий.",
#                 "image": "vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png"
#             },
#
#             {
#                 "name": "Чёрный рюкзак Nike Heritage",
#                 "price": "2 340,00",
#                 "description": "Плотная ткань. Легкий материал.",
#                 "image": "vendor/img/products/Black-Nike-Heritage-backpack.png"
#             },
#
#             {
#                 "name": "Чёрные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
#                 "price": "13 590,00",
#                 "description": "Гладкий кожаный верх. Натуральный материал.",
#                 "image": "vendor/img/products/Black-Dr-Martens-shoes.png"
#             },
#
#             {
#                 "name": "Тёмно-синие широкие строгие брюки ASOS DESIGN",
#                 "price": "2 890,00",
#                 "description": "Легкая и эластичная ткань сирсакер. Фактурная ткань.",
#                 "image": "vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png"
#             }
#
#         ]
#     }
#     return render(request, 'mainapp/products.html', context)
