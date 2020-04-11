from django.shortcuts import render
from django.views.generic import ListView
from subjects.models import *
# Create your views here.

class SubjectList(ListView):
    model = Subject
    context_object_name = 'subjects_list'
    queryset = Subject.objects.all().order_by('-created_at')
    template_name = 'subjects/lecture_list.html'

