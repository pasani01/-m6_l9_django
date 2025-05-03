from  django.urls import path
from .views import StudentsListView,add_students

urlpatterns = [
    path('students/',StudentsListView.as_view(),name='student-list'),
    path('students/add-students',add_students,name='student-add'),
    
]
