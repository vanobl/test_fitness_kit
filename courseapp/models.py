from django.db import models
from django.utils import timezone


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    
    name = models.CharField(
        verbose_name='название',
        max_length=100,
        blank=False
    )

    def __str__(self):
        return self.name


class Place(models.Model):
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
    
    name = models.CharField(
        verbose_name='название',
        max_length=100,
        blank=False
    )

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
    
    description = models.CharField(
        verbose_name='описание',
        max_length=255,
        blank=False
    )

    starttime = models.DateTimeField(
        verbose_name='начало занятия',
        default=timezone.now()
    )

    endtime = models.DateTimeField(
        verbose_name='окончание занятия',
        default=timezone.now()
    )

    appointment_id = models.CharField(
        verbose_name='идентификатор встречи',
        max_length=100,
        blank=True
    )

    service_id = models.CharField(
        verbose_name='идентификатор сервиса',
        max_length=100,
        blank=True
    )

    pay = models.BooleanField(
        verbose_name='оплата',
        default=False
    )

    appointment = models.BooleanField(
        verbose_name='appointment',
        default=False
    )

    color = models.CharField(
        verbose_name='цвет',
        max_length=7,
        blank=True
    )

    availability = models.PositiveIntegerField(
        verbose_name='полезность',
        default=1
    )

    course = models.ForeignKey(
        Course,
        verbose_name='курс',
        on_delete=models.PROTECT,
        related_name='lesson'
    )

    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        related_name='lesson'
    )

    def __str__(self):
        return f'{self.description} ({self.starttime})'
