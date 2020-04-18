# Описание полей в таблице БД
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField() #тип поля имэйл
    name = models.CharField(max_length=128) #обязательный атрибут для текстового поля это максимальная длина

    def __str__(self): #вернёт значение строки по заданному формату
        return 'Пользователь: {1} | E-mail: {0}'.format(self.email, self.name)  #можно записать это так: return '%s|%s' % (self.email, self.name)
        # '%s %s' - будут подставляться значения переменных по очередности после % ()
        #return self.email #записи в /admin в моделях и приложениях будут называться не название модели Object, а допустим email внутри

    class Meta: #произносимое имя.
# Задаётся имя вместо имени Subscribers(s добавляет Django) в единственном и множественном числе:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'