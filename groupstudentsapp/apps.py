from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class GroupstudentsappConfig(AppConfig):
    name = 'groupstudentsapp'
    verbose_name = gettext_lazy('Группы студентов')
