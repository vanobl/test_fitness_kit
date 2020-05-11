from django.db import models
from django.contrib.auth.models import User


from groupstudentsapp.models import GroupOfStudents


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    position = models.CharField(
        verbose_name='позиция',
        max_length=150,
        blank=True
    )
    
    is_teacher = models.BooleanField(
        verbose_name='статус преподавателя'
    )

    foto = models.ImageField(
        verbose_name='фото',
        upload_to='user_avatar',
        blank=True
    )
    
    group = models.ManyToManyField(
        GroupOfStudents,
        verbose_name='группа',
        related_name='users',
        blank=True
    )
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )