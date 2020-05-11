from django.urls import path
import courseapp.views as courseapp

app_name = 'courseapp'

urlpatterns = [
    path('', courseapp.LessonList.as_view(), name='index'),
    path('getjson/', courseapp.ExportJson.as_view(), name='getjson'),
]
