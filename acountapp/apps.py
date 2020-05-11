from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class AcountappConfig(AppConfig):
    name = 'acountapp'
    verbose_name = gettext_lazy('Пользователи')
