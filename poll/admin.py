from django.contrib import admin
from .models import University, Institute, Specialization, Teacher, Subject, Group, Student, Course, Question, AssessmentField, TeacherAssessment, DaySchedule, WeekSchedule, Lesson

admin.site.register(University)
admin.site.register(Institute)
admin.site.register(Specialization)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(TeacherAssessment)
admin.site.register(AssessmentField)
admin.site.register(DaySchedule)
admin.site.register(WeekSchedule)
admin.site.register(Lesson)