from django import forms
from ..models import SubjectOffstudy


class SubjectOffStudyForm(forms.ModelForm):

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'
