from django import forms
from .models import *

class SubscribersForm(forms.ModelForm): #создание формы на основе Модели

    class Meta:
        model = Subscriber #название модели на основе которой нужно сделать
        # fields = [''] #перечисляются все поля которые есть, их может быть много, поэтому легче взять все и исключить не нужные exclude
        exclude = [''] #исключить поля