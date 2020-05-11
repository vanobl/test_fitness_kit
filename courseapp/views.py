import json
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from .models import Lesson


class LessonList(LoginRequiredMixin, ListView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список занятий'
        if not self.request.user.is_superuser:
            groups = self.request.user.profile.group.all()
            context['object_list'] = Lesson.objects.filter(group__in=groups)
        else:
            context['object_list'] = Lesson.objects.all()
        return context


class ExportJson(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            groups = self.request.user.profile.group.all()
            lessons = Lesson.objects.filter(group__in=groups)
        else:
            lessons = Lesson.objects.all()
        
        response = {}

        for i, item in enumerate(lessons):
            data = {
                'name': str(item.course.name),
                'description': item.description,
                'place': str(item.place),
                'teacher': item.group.users.filter(is_teacher=True)[0].user.get_full_name(),
                'startTime': str(item.starttime),
                'endTime': str(item.endtime),
                'weekDay': int(item.starttime.isoweekday()),
                'appointment_id': str(item.appointment_id),
                'service_id': str(item.service_id),
                'pay': bool(item.pay),
                'appointment': bool(item.appointment),
                'teacher_v2': {
                    'short_name': item.group.users.filter(is_teacher=True)[0].user.get_short_name(),
                    'name': item.group.users.filter(is_teacher=True)[0].user.get_full_name(),
                    'position': str(item.group.users.filter(is_teacher=True)[0].position),
                    'imageUrl': str(item.group.users.filter(is_teacher=True)[0].foto)
                },
                'color': str(item.color),
                'availability': str(item.availability)
            }

            response[i] = data

        return JsonResponse(response)
