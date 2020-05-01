from django.shortcuts import render, redirect
from accounts.models import Member
from subjects.models import Subject, SubVideoUrl
from django.views import View
import requests
import json
from accounts.user_authentication import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.to_spring import *


class SignUP(View):
    def get(self, request):
        return render(request, 'accounts/signUpForm.html')

    def post(self, request):
        print(request.POST['name'])
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['pw']
        re_password = request.POST['pwCheck']

        info = {
            'name': name,
            'phone': phone,
            'email': email,
            'password': password,
            're_password': re_password
        }
        r = requests.post('http://192.168.21.129:8080/user/create', json=info)
        result = r.json()
        # result = to_spring('user/create', info)
        print(result)
        if result['result'] == '0':
            return JsonResponse({'result': -1}, status=200)
        else:
            return JsonResponse({'result': 1}, status=200)

class Update(View):
    @verify_user_class
    def get(self, request):
        if request.user is not None and Member.objects.filter(id=request.user).exists():
            member_info = Member.objects.get(id=request.user)
            member_info_list = {
                'name': member_info.name,
                'email': member_info.email,
                'phone': member_info.phone,
                'update': '수정하기'
            }
            return render(request, 'accounts/signUpForm.html', context=member_info_list)
        else:
            return redirect('/')

    @verify_user_class
    def post(self, request):
        name = request.POST['']



def email_check(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        data = {
            'email': email
        }
        r = requests.post('http://192.168.21.129:8080/user/checkId', json=data)
        result = r.json()
        # result = to_spring('user/checkId', data)
        print(result)
        if result['result'] == '1':
            return JsonResponse({'result': 1})
        else:
            return JsonResponse({'result': -1})
    else:
        return redirect('/')


class SignIn(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        # 스프링에 요청
        # data = {
        #     'email': email,
        #     'password': password
        # }
        # print(data)data
        # r = requests.post('http://192.168.21.129:8080/login', json=data)
        # result = to_spring('login', data)

        # 내 테스트용
        data = {
            'member_id': 1,
        }
        # r = requests.post('http://127.0.0.1:9000/create/', json=data)
        # result = r.json()
        result = to_spring_test('create', data)

        print(result)
        if result['result'] == '1':

            member_id = result['member_id']
            token = result['token']

            response = redirect('/')
            response.set_cookie('JSON_WEB_TOKEN', token, max_age=1800)
            response.user = member_id
            return response
        else:
            return redirect('/')


@logout
def LogOut(request):
    if request.headers['Cookie']:
        response = redirect('/')
        response.delete_cookie('JSON_WEB_TOKEN')
        return response
    else:
        return redirect('/')


class DeleteUser(View):
    @verify_user_class
    def get(self, request):
        return render(request, 'accounts/deleteMember.html', {})

    @verify_user_class
    def post(self, request):
        print('delete')
        print(request.user)
        email = request.POST['email']
        password = request.POST['pw']
        data = {
            'email': email,
            'password': password,
            'member_id': request.user
        }
        r = requests.delete('http://192.168.21.129:8080/user/delete', json=data)
        result = r.json()
        # result = to_spring('user/delete', data)
        if result['result'] == '1':
            response = redirect('/')
            response.delete_cookie('JSON_WEB_TOKEN')
            return response
        else:
            return redirect('./')

class RePw(View):
    @verify_user_class
    def get(self, request):
        return render(request, 'accounts/rePw.html', {})

    @verify_user_class
    def post(self, request):
        email = request.POST.get('email')
        print(email)
        data = {
            'email': email
        }
        r = requests.post('http://192.168.21.129:8080/findPassword', json=data)
        result = r.json()
        # result = to_spring('user/findPassword', data)
        if result == '1':
            return redirect('/')
        else:
            return redirect('./')