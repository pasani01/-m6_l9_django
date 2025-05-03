from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import StudentForm
from .models import Students

# Create your views here.
class StudentsListView(ListView):
    model=Students
    template_name='students/studentlist.html'
    context_object_name='students'


def add_students(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student-list')  
    return render(
        request,
        'students/studentadd.html',
        context={
            'form':StudentForm()
        }
    )