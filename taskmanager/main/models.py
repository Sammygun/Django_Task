from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    '''TextField там где много текста надо'''

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = 'Задачи'
    "Класс meta внутри класса переименовал task задача, в самом главном меню задачи"

    


