from django.contrib import admin
from django.urls import path, include
from .views import home, assessment

urlpatterns = [
    path('', home),
    path('assessment/<int:teacher_id>/<int:student_id>/', assessment),
]