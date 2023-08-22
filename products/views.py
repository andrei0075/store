from django.shortcuts import render

from products.models import ProductCategory, Product

# Create your views here.

def index(request):
    сontext = {'title': 'Test Title',
               'username': 'andrei',
               }

    return render(request, 'products/index.html', сontext)


def products(request):
    context = {
        'title':'Store - Каталог',
        'products': Product.objects.all(),
        'categories':ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
