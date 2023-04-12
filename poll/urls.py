from django.contrib import admin
from django.urls import path, include
from .views import home, assessment, studentsRating, teachersRating, subjects

urlpatterns = [
    path('', home,name='home'),
    path('studentsrating/', studentsRating, name='studentsRating'),
    path('teachersrating/', teachersRating, name='teachersRating'),
    path('assessment/<int:teacher_id>/<int:student_id>/', assessment, name='assessment'),
    path('subjects/', subjects)
]