from django.shortcuts import render
from django.http import HttpResponse

from Site.forms import * #импорт моделей
from Products.models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)

        #return redirect('Products/product')

    session_key = request.session.session_key #ключ сессии для авторизованных пользователей
    if not session_key:
        request.session.cycle_key() #создание ключа сессии для неавторизованных пользователей
    print(request.session.session_key)

    return render(request, 'Products/new_product2.html', locals())