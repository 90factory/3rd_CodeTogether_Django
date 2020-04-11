from django.urls import path
from subjects.views import *

urlpatterns = [
    path('', SubjectList.as_view(), name='subject_list')
]