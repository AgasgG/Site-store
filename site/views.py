from django.shortcuts import render, redirect
from django.http import HttpResponse

from Site.forms import * #импорт моделей
from Products.models import *

#Рабочий код, по типу как в вебинаре:
def index(request):
#    return HttpResponse('Hello World') #для отображения текста и html тегов на странице, но лучше создать отдельный html
    if request.method == 'GET':
        return render(request, 'Site/index.html', {
            'form': SubscribersForm(request.POST or None)
            })
    else:
        email = request.POST['email']
        name = request.POST['name']

        if len(email) == 0:
            if len(name) == 0:
                return render(request, 'Site/index.html', {
                    'form': SubscribersForm(request.POST or None),
                    'error1': 'укажите имя',
                    'error2': 'укажите адрес',})
            else:
                return render(request, 'Site/index.html', {
                    'form': SubscribersForm(request.POST or None),
                    'error2': 'укажите адрес'
            })

        if len(name) == 0:
            return render(request, 'Site/index.html', {
                'form': SubscribersForm(request.POST or None),
                'error1': 'укажите имя'
            })

        Subscriber(
            email=email,
            name=name,
            ).save()
        #return redirect('/index/')


        return render(request, 'Site/index.html', {
            'form': SubscribersForm(request.POST or None),
            'message': 'Вы успешно подписались!'
        })

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_notepads = products_images.filter(product__category__id=1)
    products_images_cards = products_images.filter(product__category__id=3)
    products_images_moms = products_images.filter(product__category__id=2)
    return render(request, 'Site/home.html', locals())