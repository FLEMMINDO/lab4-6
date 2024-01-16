from users.views import login, register, bucket, profile, logout
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', login, name = 'index'),
    path('register/', register, name = 'register'),
    path('bucket/', bucket, name = 'bucket'),
    path('profile/', profile, name = 'profile'),
    path('logout/', logout, name = 'logout')
]