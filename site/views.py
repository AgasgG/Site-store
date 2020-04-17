from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse



def index(request):
#    return HttpResponse('Hello World')

    return render(request, 'index.html', {
        'current_day' : datetime.today().date().strftime('%d.%m.%Y'),
        'current_time' : datetime.today().time().strftime('%H:%M'),
    })