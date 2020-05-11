from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    position = models.CharField(
        verbose_name='позиция',
        max_length=150,
        blank=True)

    foto = models.ImageField(
        verbose_name='фото',
        upload_to='user_avatar',
        blank=True)
