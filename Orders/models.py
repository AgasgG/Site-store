# Описание полей в таблице БД
from django.db import models
from Products.models import Product

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Статус: {0}'.format(self.name)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0) #цена для всех товаров в заказе
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)  # обязательный атрибут для текстового поля это максимальная длина
    customer_email = models.EmailField(blank=True, null=True, default=None) #тип поля имэйл
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None) #Blank - поле может быть пустым
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None) #Blank - поле может быть пустым
    comments = models.TextField(blank=True, null=True, default=None)#несколько строк
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Заказ: {0}, Статус: {1}'.format(self.id, self.status.name)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None) #ключ для соединения с заказом
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)  # ключ для соединения с заказом
    nmb = models.IntegerField(default=1) #nmb - numbers, количество товаров
    price_per_item = models.DecimalField(max_digits=7, decimal_places=2, default=0) #цена за единицу товара. Если цена меняется, то в заказе можно будет увидеть цену продажи
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0) #price*nmb
    is_active = models.BooleanField(default=True)  # для того чтобы скрывать товар в заказе, если его отменили
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Товар: {0}'.format(self.product.name)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары в заказах'