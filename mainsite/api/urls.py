from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.showall,name='apiview'),
    path('choice/<int:id>/',views.choice,name='choice'),
    path('create',views.create,name='create'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'), 
]