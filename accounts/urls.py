from django.urls import path
from accounts.views import ProfileView ,RegisterView,LoginUserView
# ,UpdateUSerView

app_name = 'accounts'


urlpatterns = [
    path('profile/<slug:slug>',ProfileView.as_view(),name ='profile_account'),
    path('register/',RegisterView.as_view(),name ='register'),
    path('login/',LoginUserView.as_view(),name ='login'),
    # path('update/',UpdateUSerView,name ='update'),

]

