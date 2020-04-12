from django.shortcuts import render
from accounts.models import Member
from subjects.models import Subject, SubVideoUrl
from django.views import View
import requests
import json
from django.http import HttpResponse


# Create your views here.


class MyPageView(View):
    def get(self, request):
        # 학생일때 교사일때 분기 필요
        if Member.objects.filter(id=3, type=True).exists():
            member = Member.objects.get(id=3)
            subject_list = member.subjects.all()
            lecture_list = member.my_lectures.all()
            context = {
                'member': member.name,
                'subject_list': subject_list
            }
            return render(request, 'accounts/mypage.html', {'context': context})
        else:
            member = Member.objects.get(id=3)
            subject_list = member.subjects.all()
            context = {
                'member': member.name,
                'subject_list': subject_list
            }
            return render(request, 'accounts/mypage.html', {'context': context})


def test(request):
    member_id = 1
    params = {'member_id': member_id}
    params = json.dumps(params)
    print(type(params))
    r = requests.post(url='http://localhost:9000/create/', data=params)
    print('hi')
    print(r.json())
    print(r.url)
    return HttpResponse('success')
