from django.contrib import admin
from django.urls import path
from check import views

urlpatterns = [
    path('check_subject/', views.check_subject),
    path('course_description/<int:id>/', views.course_descript),
    path('check_qrcode/', views.qrcode)
]
