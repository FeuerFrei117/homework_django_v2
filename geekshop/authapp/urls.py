from django.urls import path

from authapp.views import login, register, logaut, profile

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logaut/', logaut, name='logaut'),
    path('profile/', profile, name='profile'),
]
