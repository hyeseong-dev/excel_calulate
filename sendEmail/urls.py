from django.urls import path,include
from . import views

urlpatterns = [
    path('send', views.send, name='email_send'),
]
