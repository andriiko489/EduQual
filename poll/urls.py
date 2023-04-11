from django.contrib import admin
from django.urls import path, include
from .views import home, assessment

urlpatterns = [
    path('', home),
    path('1/', assessment),
]