from django.urls import path
from registration.views import Login, Logout

app_name = 'registration'


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]