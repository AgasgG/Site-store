from django.contrib import admin
from .models import * #импортируем из текущей папки файл models, всё

#класс для отображения фото под карточкой товара
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0 #по умолчанию при загрузке 2х картинок для продукта ещё 3 пустые сввтятся, чтобы их не было укахывается этот параметр

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields] #чтобы не перечислять названия всех полей делается цикл. "Subscriber._meta.fields" достаёт все поля из модели Subscriber
    inlines = [ProductImageInline]
    class Meta:
        model= Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields] #чтобы не перечислять названия всех полей делается цикл. "Subscriber._meta.fields" достаёт все поля из модели Subscriber

    class Meta:
        model= ProductImage

admin.site.register(ProductImage, ProductImageAdmin)