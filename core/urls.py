from django.urls import path
from core import views

urlpatterns=[
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('respForm', views.respForm, name='respForm'),
]