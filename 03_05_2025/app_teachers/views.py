from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import TeacherForms


from .models import Teacher
# Create your views here.

class TeachersListView(ListView):
    model=Teacher
    template_name='teachers/teacherlist.html'
    context_object_name='teachers'

def add_teacher(request):
    if request.method=='POST':
        form=TeacherForms(request.POST)
        if(form.is_valid):
            form.save()
        return redirect('teacher-list')
    return render(
        request,
        'teachers/teacheradd.html',
        context={
            'form':TeacherForms
        }
    )
