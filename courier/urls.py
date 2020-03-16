from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name="home"),
    path('student/<str:pk_test>/',views.student,name="student"),
    path('company/',views.company,name="company"),
    path('create_courier/<str:pk>/',views.createCourier,name='create_courier'),
    path('update_courier/<str:pk>/',views.updateCourier,name='update_courier'),
]
