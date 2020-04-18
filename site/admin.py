from django.contrib import admin
from .models import * #импортируем из текущей папки файл models, всё

#admin.site.register(Subscriber) #регистрируем модель Подписчики
#новый способ этого же:
class SubscriberAdmin(admin.ModelAdmin):

    #это для списка записей:
    #list_display = ['name', 'email'] #какие поля выводить!
    # удобно, при этом форматирование строк в models.py не будет накладываться на список, но при открытие элекманта название будет по формату модели
    list_display = [field.name for field in Subscriber._meta.fields] #чтобы не перечислять названия всех полей делается цикл. "Subscriber._meta.fields" достаёт все поля из модели Subscriber
    list_filter = ['name'] #добавление в правой части окна столбца фильтр с указанием значений всех полей
    search_fields = ['name', 'email'] #добавляется поле поиска для возможности фильтрации по имени или email

    ##это для самой записи:
    #если нужно скрыть некоторые поля когда открывается запись:
    #exclude = ['email']

    #или наоборот, показывать только email:
    fields = ['email']


    class Meta:
        model= Subscriber

admin.site.register(Subscriber, SubscriberAdmin)