from django.contrib import admin
from django.urls import path
from myCRM import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('loggout', views.logginout, name="loggout"),
    path('SignupPage', views.SignupPage, name='SignupPage'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record', views.add_record, name= 'add_record'),
    path('update_record/<int:pk>',views.update_record, name='update_record'),
    ]
