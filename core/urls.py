from django.urls import path
from core.views import MainView , ExploreView
# login


app_name = 'core'


urlpatterns = [
    path('',MainView.as_view(),name ='main'),
    path('exp/',ExploreView.as_view() ,name ='explore'),
    # path('login/',login,name ='login'),
    

]