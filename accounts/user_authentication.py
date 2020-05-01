from django.shortcuts import redirect, render
from accounts.models import *
from subjects.models import *
from django.http import HttpResponse
from config.settings import SECRET_KEY
from accounts.models import Member
import jwt
import requests
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from http import cookies
from django.core.paginator import Paginator
from accounts.to_spring import *



# 메인화면
# def authentication_get(func):
#     @csrf_exempt
#     def wrapper(request, *args, **kwargs):
#         print('유저인증 시작')
#         try:
#             a = request.META['HTTP_COOKIE']
#             c = cookies.SimpleCookie()
#             c.load(a)
#             if c['JSON_WEB_TOKEN']:
#                 token = c['JSON_WEB_TOKEN'].value
#                 print(token)
#                 token = {
#                     'token': token
#                 }
#                 # 스프링
#                 # r = requests.post('http://192.168.1.53:8080/getId.do', json=token)
#                 # result = r.json()
#                 # result = to_spring('getId', token)
#
#                 # 테스트용
#                 # r = requests.post('http://127.0.0.1:9000/verify/', json=token)
#                 # result = r.json()
#                 result = to_spring_test('verify', token)
#                 print(result)
#                 request.user = result['member_id']
#                 return func(request, *args, **kwargs)
#         except KeyError as e:
#             request.user = None
#             return func(request, *args, **kwargs)
#         except TypeError as e:
#             print(e)
#     return wrapper


def logout(func):
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        try:
            print('유저인증 시작')
            a = request.META['HTTP_COOKIE']
            c = cookies.SimpleCookie()
            c.load(a)
            if c['JSON_WEB_TOKEN']:
                token = c['JSON_WEB_TOKEN'].value
                print(token)
                token = {
                    'token': token
                }
                # r = requests.post('http://192.168.21.129:8080/auth/getId', json=token)
                # result = r.json()
                # result = to_spring('getId', token)

                # 테스트용
                # r = requests.post('http://127.0.0.1:9000/verify/', json=token)
                # result = r.json()
                result = to_spring_test('verify', token)
                print(result)
                request.user = result['member_id']
                return func(request, *args, **kwargs)
        except KeyError as e:
            print(e)
            return redirect('/')
        except TypeError as e:
            print(e)
            return redirect('/')
    return wrapper

# class 는 3번 함수는 main2번
def verify_user_class(func):
    @csrf_exempt
    def wrapper(self, request, *args, **kwargs):
        try:
            print('유저인증 시작')
            print(request.headers)
            a = request.META['HTTP_COOKIE']
            c = cookies.SimpleCookie()
            c.load(a)
            if c['JSON_WEB_TOKEN']:
                token = c['JSON_WEB_TOKEN'].value
                print(token)
                token = {
                    'token': token
                }
                # r = requests.post('http://192.168.21.129:8080/auth/getId', json=token)
                # result = r.json()
                # result = to_spring('getId', token)

                # 테스트용
                # r = requests.post('http://127.0.0.1:9000/verify/', json=token)
                # result = r.json()
                result = to_spring_test('verify', token)
                print(result)
                request.user = result['member_id']
                return func(self, request, *args, **kwargs)
        except KeyError as e:
            request.user = None
            return func(self, request, *args, **kwargs)
        except TypeError as e:
            print(e)
            return func(self, request, *args, **kwargs)
    return wrapper





# def lecture_list(func):
#     @csrf_exempt
#     def wrapper(self, request, *args, **kwargs):
#         try:
#             print('유저인증 시작')
#             print(request.headers)
#             a = request.META['HTTP_COOKIE']
#             c = cookies.SimpleCookie()
#             c.load(a)
#             if c['JSON_WEB_TOKEN']:
#                 token = c['JSON_WEB_TOKEN'].value
#                 print(token)
#                 token = {
#                     'token': token
#                 }
#                 # r = requests.post('http://192.168.1.53:8080/getId.do', json=token)
#                 # result = r.json()
#                 # result = to_spring('getId', token)
#
#                 # 테스트
#                 result = to_spring_test('verify', token)
#                 print(result)
#                 request.user = result['member_id']
#                 return func(self, request, *args, **kwargs)
#         except KeyError as e:
#             request.user = None
#             # subject_list = Subject.objects.all().order_by('-created_at')
#             # paginator = Paginator(subject_list, 6)
#             # page = request.GET.get('page')
#             # subjects = paginator.get_page(page)
#             # context = {
#             #     'subjects': subjects,
#             # }
#             # return render(request, 'subjects/subjectSearch.html', context=context)
#             return func(self, request, *args, **kwargs)
#         except TypeError as e:
#             print(e)
#             return redirect('/')
#     return wrapper


# def lecture(func):
#     @csrf_exempt
#     def wrapper(self, request, pk, **kwargs):
#         try:
#             print('유저인증 시작')
#             a = request.META['HTTP_COOKIE']
#             c = cookies.SimpleCookie()
#             c.load(a)
#             if c['JSON_WEB_TOKEN']:
#                 token = c['JSON_WEB_TOKEN'].value
#                 print(token)
#                 token = {
#                     'token': token
#                 }
#                 r = requests.post('http://192.168.1.53:8080/getId.do', json=token)
#                 result = r.json()
#                 print(result)
#                 request.user = result['member_id']
#                 return func(self, request, pk, **kwargs)
#         except KeyError as e:
#             # print('hi')
#             # if Subject.objects.filter(id=pk).exists():
#             #     subject = Subject.objects.get(id=pk)
#             #     video_list = subject.video_urls.all()
#             #     context = {
#             #         'subject': subject,
#             #         'video': video_list,
#             #     }
#             #     return render(request, 'subjects/subjectDetail.html', context=context)
#             request.user = None
#             return func(self, request, pk, **kwargs)
#         except TypeError as e:
#             print(e)
#             return redirect('/')
#     return wrapper


# def lecture_room(func):
#     @csrf_exempt
#     def wrapper(self, request, *args, **kwargs):
#         try:
#             print('유저인증 시작')
#             print(request.headers)
#             a = request.META['HTTP_COOKIE']
#             c = cookies.SimpleCookie()
#             c.load(a)
#             if c['JSON_WEB_TOKEN']:
#                 token = c['JSON_WEB_TOKEN'].value
#                 print(token)
#                 token = {
#                     'token': token
#                 }
#                 r = requests.post('http://192.168.1.53:8080/getId.do', json=token)
#                 result = r.json()
#                 print(result)
#                 request.user = result['member_id']
#                 return func(self, request, *args, **kwargs)
#         except KeyError as e:
#             return redirect('/')
#         except TypeError as e:
#             print(e)
#             return func(self, request, *args, **kwargs)
#     return wrapper


def pay(func):
    @csrf_exempt
    def wrapper(self, request, pk, **kwargs):
        try:
            print('유저인증 시작')
            print(request.headers)
            a = request.META['HTTP_COOKIE']
            c = cookies.SimpleCookie()
            c.load(a)
            if c['JSON_WEB_TOKEN']:
                token = c['JSON_WEB_TOKEN'].value
                print(token)
                token = {
                    'token': token
                }
                # r = requests.post('http://192.168.21.129:8080/auth/getId', json=token)
                # result = r.json()
                # result = to_spring('getId', token)

                result = to_spring_test('verify', token)
                print(result)
                request.user = result['member_id']
                return func(self, request, pk, **kwargs)
        except KeyError as e:
            request.user = None
            return func(self, request, pk, **kwargs)
        except TypeError as e:
            print(e)
            return redirect(f'/subjects/{pk}/')
    return wrapper



# def verify_teacher(func):
#     @csrf_exempt
#     def wrapper(self, request, **kwargs):
#         print('유저인증 시작')
#         print(request.headers)
#         try:
#             a = request.META['HTTP_COOKIE']
#             c = cookies.SimpleCookie()
#             c.load(a)
#             if c['JSON_WEB_TOKEN']:
#                 token = c['JSON_WEB_TOKEN'].value
#                 print(token)
#                 token = {
#                     'token': token
#                 }
#                 # r = requests.post('http://192.168.1.53:8080/getId.do', json=token)
#                 # result = r.json()
#                 # result = to_spring('getId', token)
#
#                 result = to_spring_test('verify', token)
#                 print(result)
#                 request.user = result['member_id']
#                 # if Member.objects.filter(id=request.user, type=True).exists():
#                 #     return func(self, request, **kwargs)
#                 # else:
#                 #     return redirect('/')
#                 return func(self, request, **kwargs)
#         except KeyError:
#             request.user = None
#             return func(self, request, **kwargs)
#         except TypeError:
#             return func(self, request, **kwargs)
#     return wrapper