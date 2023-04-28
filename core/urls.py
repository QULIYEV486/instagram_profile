from django.urls import path
from core.views import mainpage, explore, profile

app_name = 'core'


urlpatterns = [
    path('',mainpage,name ='main'),
    path('exp/',explore,name ='explore'),
    path('profile/',profile,name ='profile'),
]