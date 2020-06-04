from ..models import DeathReport
from django import forms


class SubjectDeathForm(forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = '__all__'
