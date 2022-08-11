from django.urls import path

from . import views

urlpatterns = [
    path('', views.sending_mail, name='sending_mail'),
    path('thanks/', views.thanks, name='thanks'),
]