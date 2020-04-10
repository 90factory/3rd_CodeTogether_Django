from django.shortcuts import render
from django.views.generic import ListView
from subjects.models import *
# Create your views here.

class SubjectList(ListView):
    model = Subject

