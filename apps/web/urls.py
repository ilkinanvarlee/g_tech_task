from django.urls import path
from . views import index_view, contact_view

app_name = 'web'

urlpatterns = [
    path('', index_view, name="index_view"),
    path('contact', contact_view, name="contact_view"),

]
