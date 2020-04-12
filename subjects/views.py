from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from subjects.models import *
from subjects.forms import SubjectForm

# Create your views here.

class SubjectList(ListView):
    # model = Subject
    # context_object_name = 'subject_list'
    # template_name = 'subjects/subject_list.html'
    def get_queryset(self):
        queryset = Subject.objects.all().order_by('-created_at')
        query = self.request.GET.get('value', None)
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
            return queryset
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SubjectList, self).get_context_data()
        return context




class SubjectDetail(DetailView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'subjects/subject_detail.html'


class SubjectCreate(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, 'subjects/lecture_form.html', {'form': form})

    def post(self, request):
        name = request.POST['name']
        difficulty = request.POST['difficulty']
        rating = request.POST['rating']
        price = request.POST['price']
        description = request.POST['description']
        language = request.POST['language']
        sub_image = request.POST['sub_image']
        sub_video = request.POST['sub_video']





