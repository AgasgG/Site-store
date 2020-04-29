from django import forms
from .models import *

class CheckoutContentForm(forms.Form): #создание формы на основе Модели
    name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)