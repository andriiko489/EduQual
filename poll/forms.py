from django import forms
from .models import TeacherAssessment, AssessmentField


class TeacherAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherAssessment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(args)
        assessment_fields = AssessmentField.objects.filter(teacherassessment=TeacherAssessment.objects.get(id=1))
        for field in assessment_fields:
            self.fields[f'field_{field.id}'] = forms.IntegerField(widget=forms.RadioSelect(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))), label=field.question, initial=field.num)