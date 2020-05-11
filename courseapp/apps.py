from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class CourseappConfig(AppConfig):
    name = 'courseapp'
    verbose_name = gettext_lazy('Курсы')
