# Описание полей в таблице БД
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save

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
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #цена для всех товаров в заказе
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

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)



class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None) #ключ для соединения с заказом
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)  # ключ для соединения с заказом
    nmb = models.IntegerField(default=1) #nmb - numbers, количество товаров
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0) #цена за единицу товара. Если цена меняется, то в заказе можно будет увидеть цену продажи
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb
    is_active = models.BooleanField(default=True)  # для того чтобы скрывать товар в заказе, если его отменили
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Товар: {0}'.format(self.product.name)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs): #функция для переопределения сохранения
        price_per_item = self.product.price #цена в поле Модели Продукта присваивается цене в строке заказа
        self.price_per_item =  price_per_item # цене в строке заказа
        self.total_price = self.nmb * price_per_item #считаем итоговую сумму

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
       order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)  # обязательный атрибут для текстового поля это максимальная длина)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None) #ключ для соединения с заказом
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)  # ключ для соединения с заказом
    nmb = models.IntegerField(default=1) #nmb - numbers, количество товаров
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0) #цена за единицу товара. Если цена меняется, то в заказе можно будет увидеть цену продажи
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb
    is_active = models.BooleanField(default=True)  # для того чтобы скрывать товар в заказе, если его отменили
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Товар: {0}'.format(self.product.name)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):  # функция для переопределения сохранения
        price_per_item = self.product.price  # цена в поле Модели Продукта присваивается цене в строке заказа
        self.price_per_item = price_per_item  # цене в строке заказа
        self.total_price = int(self.nmb) * price_per_item  # считаем итоговую сумму

        super(ProductInBasket, self).save(*args, **kwargs)