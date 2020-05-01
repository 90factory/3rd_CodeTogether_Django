from django.urls import path
from subjects.views import *

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subjects_list'),
    path('<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('add/', SubjectCreate.as_view(), name='subject_register'),
    path('<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('<int:pk>/lecture/', Lecture.as_view(), name='lecture'),
    path('<int:pk>/pay/', Pay.as_view(), name='pay'),
    path('search/', search, name='search')
]
