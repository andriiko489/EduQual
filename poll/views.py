from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView
from .models import TeacherAssessment, AssessmentField, Subject
from django.urls import reverse_lazy
from .forms import TeacherAssessmentForm
from .models import Teacher, Student
def home(request):
    return render(request, 'home/index.html')
def studentsRating(request):
    context = {}
    context['members'] = Student.objects.order_by('score').reverse().all()
    return render(request, 'rating/rating.html', context=context)
def teachersRating(request):
    context = {}
    context['members'] = Teacher.objects.order_by('score').reverse().all()
    return render(request, 'rating/rating.html', context=context)
def assessment(request, teacher_id, student_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    student = get_object_or_404(Student, pk=student_id)
    print(1)
    if request.method == "POST":
        print(2)
        form = TeacherAssessmentForm(request.POST)
        #print("asdasdasd {}".format(form.is_valid()))
        if form.is_valid():
            # Create a new Assessment object with the cleaned form data
            assessment = form.save(commit=False)
            assessment.student = student
            assessment.teacher = teacher
            assessment.save()
            return HttpResponseRedirect("/")
    else:
        form = TeacherAssessmentForm(teacher_id)
    teacher = Teacher.objects.filter(id=teacher_id)[0]
    assessment = TeacherAssessment.objects.filter(teacher=teacher)[0]
    assessment_fields = AssessmentField.objects.filter(teacherassessment=assessment)
    for i in assessment_fields:
        print(i)
    context = {"fields":assessment_fields, "form":form}
    return render(request, "assessment/poll.html", context=context)

def subjects(request):
    context = {'subjects':[]}
    for i in Subject.objects.all():
        context['subjects'].append(str(i))
    return render(request, "subject/subject.html", context=context)