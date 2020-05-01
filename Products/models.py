# Описание полей в таблице БД
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):  # вернёт значение строки по заданному формату
        return 'Категория: {0}, ID: {1}'.format(self.name, self.id)

    class Meta:  # произносимое имя.
        # Задаётся имя в единственном и множественном числе:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)  # обязательный атрибут для текстового поля это максимальная длина
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None) #короткое описание
    description = models.TextField(blank=True, null=True, default=None)#несколько строк
    is_active = models.BooleanField(default=True)  # для того чтобы скрывать товар, допустим его нет
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Товар: {0}, ID: {1}'.format(self.name, self.id)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) #для того чтобы скрывать картинки
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #значение меняется при создании
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #значение меняется при любом обновлении в модели/записи

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Фото: {0}'.format(self.id)

    class Meta: #произносимое имя.
# Задаётся имя в единственном и множественном числе:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'