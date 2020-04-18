from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse

from Site.forms import * #импорт моделей

'''
#Из видео, не взлетело
def index(request):
#    return HttpResponse('Hello World') #для отображения текста и html тегов на странице, но лучше создать отдельный html
    current_day = datetime.today().date().strftime('%d.%m.%Y')
    current_time = datetime.today().time().strftime('%H:%M')
    form = SubscribersForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        newform = form.save()
    return render(request, 'index.html')
'''

#Рабочий код, по типу как в вебинаре: 
def index(request):
#    return HttpResponse('Hello World') #для отображения текста и html тегов на странице, но лучше создать отдельный html
    if request.method == 'GET':
        return render(request, 'index.html', {
            'current_day' : datetime.today().date().strftime('%d.%m.%Y'),
            'current_time' : datetime.today().time().strftime('%H:%M'),
            'form': SubscribersForm(request.POST or None)
            })
    else:
        email = request.POST['email']
        name = request.POST['name']

        Subscriber(
            email=email,
            name=name,
            ).save()
        return redirect('/')