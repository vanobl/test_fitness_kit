# Generated by Django 3.0.5 on 2020-05-11 09:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('starttime', models.DateTimeField(default=datetime.datetime(2020, 5, 11, 9, 46, 12, 341527, tzinfo=utc), verbose_name='начало занятия')),
                ('endtime', models.DateTimeField(default=datetime.datetime(2020, 5, 11, 9, 46, 12, 341546, tzinfo=utc), verbose_name='окончание занятия')),
                ('appointment_id', models.CharField(blank=True, max_length=100, verbose_name='идентификатор встречи')),
                ('service_id', models.CharField(blank=True, max_length=100, verbose_name='идентификатор сервиса')),
                ('pay', models.BooleanField(default=False, verbose_name='оплата')),
                ('appointment', models.BooleanField(default=False, verbose_name='appointment')),
                ('color', models.CharField(blank=True, max_length=7, verbose_name='цвет')),
                ('availability', models.PositiveIntegerField(default=1, verbose_name='полезность')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lesson', to='courseapp.Course', verbose_name='курс')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lesson', to='courseapp.Place')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
            },
        ),
    ]
