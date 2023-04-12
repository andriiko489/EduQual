from django.contrib import admin
from django.urls import path, include
from .views import home, assessment, studentsRating, teachersRating, subjects, weeks, week, teachers
from .views import home, assessment, studentsRating, teachersRating, subjects, teacher, march

urlpatterns = [
    path('', home,name='home'),
    path('studentsrating/', studentsRating, name='studentsRating'),
    path('teachersrating/', teachersRating, name='teachersRating'),
    path('teachers/<int:teacher_id>/<int:student_id>/', assessment, name='assessment'),
    path('subjects/', subjects),
    path('schedule/', weeks, name='weeks'),
    path('schedule/<int:week_id>', week),
    path('teachers/', teachers, name='teachers'),
    path('assessment/<int:teacher_id>/<int:student_id>/', assessment, name='assessment'),
    path('subjects/', subjects),
    path('account/teacher/', teacher),
    path('march/', march,  name='march')

]