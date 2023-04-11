from django import forms
from .models import TeacherLectureAssessment
class TeacherLectureAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherLectureAssessment
        fields = ['student', 'teacher', 'informative', 'actuality']

    informative = forms.IntegerField(widget=forms.RadioSelect(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))))
    actuality = forms.IntegerField(widget=forms.RadioSelect(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))))