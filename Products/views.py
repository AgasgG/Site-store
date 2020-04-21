from django.shortcuts import render, redirect
from django.http import HttpResponse

from Site.forms import * #импорт моделей
from Products.models import *

def product(requets, product_id):
    product = Product.objects.get(id=product_id)
    return render(requets, 'Products/product.html', locals())
        #return redirect('Products/product')