from django.urls import path
from subjects.views import *

app_name = 'subjects'

urlpatterns = [
    path('', SubjectList.as_view(), name='subject_list'),
    path('<int:pk>/', SubjectDetail.as_view(), name='subject_detail'),
    path('register/', SubjectCreate.as_view(), name='subject_register'),
]
