from django.shortcuts import render,redirect
from .models import Feedbacks
from django.views.generic import ListView
from .forms import FeedbackForms
# Create your views here.

class FeedbackListView(ListView):
    model=Feedbacks
    template_name='feedbacks/feedbacklist.html'
    context_object_name='feedbacks'

def add_feedback(request):
    if request.method=='POST':
        form=FeedbackForms(request.POST)
        if(form.is_valid):
            form.save()
        return redirect('feedback-list')
    return render(
        request,
        'feedbacks/feedbackadd.html',
        context={
            'form':FeedbackForms
        }

    )