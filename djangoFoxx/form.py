from django import forms
from djangoFoxx.model import Students

class Empform(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"


