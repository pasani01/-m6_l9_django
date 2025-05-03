from django.forms import ModelForm

from .models import Teacher

class TeacherForms(ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'
        exclude =[]