from django.contrib import admin
from .models import * #импортируем из текущей папки файл models, всё

admin.site.register(Subscribers) #регистрируем модель Подписчики