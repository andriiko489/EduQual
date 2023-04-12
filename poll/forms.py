from django import forms
from .models import TeacherAssessment, AssessmentField, Teacher
from django.shortcuts import HttpResponse

class TeacherAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherAssessment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if type(args[0])==type(1):
            try:
                teacher = Teacher.objects.filter(id=args[0])[0]
                assessment = TeacherAssessment.objects.filter(teacher=teacher)[0]
                assessment_fields = AssessmentField.objects.filter(teacherassessment=assessment)
            except:
                return HttpResponse(status=404)
            for field in assessment_fields:
                self.fields[f'field_{field.id}'] = forms.IntegerField(widget=forms.RadioSelect(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))), label=field.question, initial=field.num)
        else:
            for field in args[0]:
                print(field)