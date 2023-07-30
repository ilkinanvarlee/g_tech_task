from django.urls import path
from . views import profile_view

app_name = 'user'

urlpatterns = [
    path('profile', profile_view, name='profile_view'),

]

