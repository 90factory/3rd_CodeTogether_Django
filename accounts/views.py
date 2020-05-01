from django.shortcuts import render, redirect
from accounts.models import Member
from subjects.models import Subject, SubVideoUrl
from django.views import View
import requests
import json
from accounts.user_authentication import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @authentication_get
# def main(request):
#     print(request.user)
#     subject_order_list = Subject.objects.all().order_by('-created_at')[:3]
#     subject_order_next_list = Subject.objects.all().order_by('-created_at')[3:6]
#     subject_famous_list = Subject.objects.all().order_by('-created_at')[:3]
#     if request.user is not None:
#         if Member.objects.filter(id=request.user, type=True).exists():
#             name = Member.objects.get(id=request.user).name
#             context = {
#                 'subject_order_list': subject_order_list,
#                 'subject_order_next_list': subject_order_next_list,
#                 'subject_famous_list': subject_famous_list,
#                 'name': name,
#                 'teacher': '선생님'
#             }
#         else:
#             name = Member.objects.get(id=request.user).name
#             print(name)
#             context = {
#                 'subject_order_list': subject_order_list,
#                 'subject_order_next_list': subject_order_next_list,
#                 'subject_famous_list': subject_famous_list,
#                 'name': name
#             }
#         return render(request, 'accounts/home.html', context=context)
#     else:
#         context = {
#             'subject_order_list': subject_order_list,
#             'subject_order_next_list': subject_order_next_list,
#             'subject_famous_list': subject_famous_list,
#         }
#         return render(request, 'accounts/home.html', context=context)


class Main(View):
    @verify_user_class
    def get(self, request):
        print(request.user)
        subject_order_list = Subject.objects.all().order_by('-created_at')[:3]
        subject_order_next_list = Subject.objects.all().order_by('-created_at')[3:6]
        subject_famous_list = Subject.objects.all().order_by('-created_at')[:3]
        if request.user is not None:
            if Member.objects.filter(id=request.user, type=True).exists():
                name = Member.objects.get(id=request.user).name
                context = {
                    'subject_order_list': subject_order_list,
                    'subject_order_next_list': subject_order_next_list,
                    'subject_famous_list': subject_famous_list,
                    'name': name,
                    'teacher': '선생님'
                }
            else:
                name = Member.objects.get(id=request.user).name
                print(name)
                context = {
                    'subject_order_list': subject_order_list,
                    'subject_order_next_list': subject_order_next_list,
                    'subject_famous_list': subject_famous_list,
                    'name': name
                }
            return render(request, 'accounts/home.html', context=context)
        else:
            context = {
                'subject_order_list': subject_order_list,
                'subject_order_next_list': subject_order_next_list,
                'subject_famous_list': subject_famous_list,
            }
            return render(request, 'accounts/home.html', context=context)


class MyPageView(View):
    @verify_user_class
    def get(self, request):
        # 학생일때 교사일때 분기 필요
        # id를 받아야 한다.
        if Member.objects.filter(id=request.user, type=True).exists():
            member = Member.objects.get(id=request.user)
            subject_list = member.subjects.all()
            lecture_list = member.my_lectures.all()
            context = {
                'name': member.name,
                'subject_list': lecture_list,
                'subjects_list': subject_list,
                'teacher': '선생님!'
            }
            return render(request, 'accounts/myPage.html', context=context)
        elif Member.objects.filter(id=request.user).exists():
            member = Member.objects.get(id=request.user)
            subject_list = member.subjects.all()
            lecture_list = member.my_lectures.all()
            context = {
                'name': member.name,
                'subject_list': subject_list,
            }
            return render(request, 'accounts/myPage.html', context=context)
        else:
            return redirect('/')
