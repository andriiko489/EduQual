from django.contrib import admin
from django.urls import path, include
from .views import home, assessment, studentsRating, teachersRating

urlpatterns = [
    path('', home),
    path('studentsrating/', studentsRating),
    path('teachersrating/', teachersRating),
    path('assessment/<int:teacher_id>/<int:student_id>/', assessment),
]