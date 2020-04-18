# Описание полей в таблице БД
from django.db import models


class Subscribers(models.Model):
    email = models.EmailField() #тип поля имэйл
    name = models.CharField(max_length=128) #обязательный атрибут для текстового поля это максимальная длина
