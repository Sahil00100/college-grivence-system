
from django.urls import path
from.views import *
urlpatterns = [
   path('index/',index_view,name='index'),
   path('login/',login_view,name='login'),
   path('signup/',signup_view,name='signup'),
   path('dashboard/',dashboard_view,name='dashboard'),
   path('message/',message_view,name='message'),
   path('principal/',principal_view,name='principal'),
   path('logout/',logout_view,name='logout'),
]
