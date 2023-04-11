from django.shortcuts import render
from django.views.generic import CreateView
from .models import TeacherLectureAssessment
from django.urls import reverse_lazy
from .forms import TeacherLectureAssessmentForm
def home(request):
    return render(request, 'home/index.html')

def assessment(request):
    return render(request, 'assessment/index.html', context={'form':TeacherLectureAssessmentForm})