from django.urls import path
from .views import TeachersListView,add_teacher

urlpatterns = [
    path('teachers/',TeachersListView.as_view(),name='teacher-list'),
    path('teachers/teacher-add',add_teacher,name='teacher-add')
]
