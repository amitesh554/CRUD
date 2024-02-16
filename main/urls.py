from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('fetch/',views.fetch),
    path('update',views.update),
    path('delete/',views.delete)
]