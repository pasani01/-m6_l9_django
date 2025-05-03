from django.urls import path
from .views import FeedbackListView,add_feedback

urlpatterns = [
    
    path('feedbacks',FeedbackListView.as_view(),name='feedback-list'),
    path('feedback/feedback-add',add_feedback,name='feedback-add')

]
