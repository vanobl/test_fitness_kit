# Generated by Django 3.0.5 on 2020-05-11 08:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('students', models.ManyToManyField(related_name='group', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Группа студентов',
                'verbose_name_plural': 'Группы студентов',
            },
        ),
    ]
