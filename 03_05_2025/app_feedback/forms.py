from django.forms import ModelForm
from .models import Feedbacks

class FeedbackForms(ModelForm):
    class Meta:
        model=Feedbacks
        fields='__all__'
        exclude =[]