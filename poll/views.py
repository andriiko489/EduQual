from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView
from .models import TeacherLectureAssessment
from django.urls import reverse_lazy
from .forms import TeacherLectureAssessmentForm
from .models import Teacher, Student
def home(request):
    return render(request, 'home/index.html')

def assessment(request, teacher_id, student_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "POST":
        form = TeacherLectureAssessmentForm(request.POST)
        if form.is_valid():
            # Create a new Assessment object with the cleaned form data
            assessment = form.save(commit=False)
            assessment.student = student
            assessment.teacher = teacher
            assessment.save()
            return HttpResponseRedirect("/thanks/")
    else:
        form = TeacherLectureAssessmentForm()
    return render(request, "assessment/index.html", {"form": form})