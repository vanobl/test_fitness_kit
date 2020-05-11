from django.contrib import admin

from .models import Course, Place, Lesson

admin.site.register(Course)
admin.site.register(Place)
admin.site.register(Lesson)
