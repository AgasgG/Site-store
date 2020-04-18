from django.contrib import admin
from .models import * #импортируем из текущей папки файл models, всё

#admin.site.register(Subscriber) #регистрируем модель Подписчики
#новый способ этого же:
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0 #по умолчанию при загрузке 2х картинок для продукта ещё 3 пустые сввтятся, чтобы их не было укахывается этот параметр



class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields] #чтобы не перечислять названия всех полей делается цикл. "Subscriber._meta.fields" достаёт все поля из модели Subscriber

    class Meta:
        model= Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] #чтобы не перечислять названия всех полей делается цикл. "Subscriber._meta.fields" достаёт все поля из модели Subscriber
    inlines = [ProductInOrderInline]

    class Meta:
        model= Order

admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields] #чтобы не перечислять названия всех полей делается цикл. "Subscriber._meta.fields" достаёт все поля из модели Subscriber

    class Meta:
        model= ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)