# Generated by Django 3.0.5 on 2020-05-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acountapp', '0002_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='статус преподавателя'),
            preserve_default=False,
        ),
    ]