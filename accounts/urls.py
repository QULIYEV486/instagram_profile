from django.urls import path
from accounts.views import profile, register

app_name = 'accounts'


urlpatterns = [
    path('profile/<slug:slug>',profile,name ='profile'),
    path('register/',register,name ='register'),
]           



