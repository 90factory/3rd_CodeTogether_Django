from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from subjects.models import *
from subjects.forms import SubjectForm
from subjects.subjects_validation import subject_validate
from accounts.user_authentication import *
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import json
import math


class SubjectListView(View):
    @verify_user_class
    def get(self, request):
        print(request.user)
        if request.user is not None:
            subject_list = Subject.objects.all().order_by('-created_at')
            paginator = Paginator(subject_list, 9)
            page = request.GET.get('page')
            subjects = paginator.get_page(page)
            page_range = paginator.page_range
            context = {
                'subjects': subjects,
                'name': 'name',
                'page_range': page_range
            }
            return render(request, 'subjects/subjectSearch.html', context=context)
        else:
            subject_list = Subject.objects.all().order_by('-created_at')
            paginator = Paginator(subject_list, 9)
            page = request.GET.get('page')
            subjects = paginator.get_page(page)
            page_range = paginator.page_range
            context = {
                'subjects': subjects,
                'page_range': page_range
            }
            return render(request, 'subjects/subjectSearch.html', context=context)

    def post(self, request):
        return redirect('/')

# class SubjectsList(View):
#     @v


def search(request):
    if request.method == 'GET':
        q = request.GET.get('q', None)
        print(q)
        if q is not None:
            queryset = Subject.objects.all().order_by('-created_at')
            if Subject.objects.filter(name__icontains=q).exists():
                subject_list = queryset.filter(name__icontains=q)
                search_list = [{
                    'id': subject.id,
                    'name': subject.name,
                    'difficulty': subject.difficulty,
                    'price': subject.price,
                    'description': subject.description,
                    'sub_image': subject.sub_image.url,
                    'language': subject.language,
                    'created_at': subject.created_at,
                    'teacher': subject.teacher.name
                } for subject in subject_list]
                return JsonResponse({'search_list': search_list}, status=200)
            elif Member.objects.filter(name=q, type=True).exists():
                a = Member.objects.get(name=q, type=True)
                teacher_lectures = Subject.objects.filter(teacher_id=a.id)
                search_teacher = [{
                    'id': subject.id,
                    'name': subject.name,
                    'difficulty': subject.difficulty,
                    'price': subject.price,
                    'description': subject.description,
                    'sub_image': subject.sub_image.url,
                    'language': subject.language,
                    'created_at': subject.created_at,
                    'teacher': subject.teacher.name
                } for subject in teacher_lectures]
                return JsonResponse({'search_list': search_teacher}, status=200)
            # else:
            #     return redirect('subjects:subjects_list')
            else:
                return JsonResponse({'error': '-1'}, status=200)
    else:
        return JsonResponse({'error': 'get?'})


class SubjectUpdateView(View):
    @verify_user_class
    def get(self, request, pk):
        if request.user is not None:
            subject = get_object_or_404(Subject, id=pk)
            video_dict = subject.video_urls.values()
            sub_video_dict = {}
            for i in video_dict:
                sub_video_name = i.get('sub_video_name')
                sub_video = i.get('sub_video')
                sub_video_dict[sub_video_name] = sub_video
            update_list = {
                'update': '수정하기',
                'name': subject.name,
                'sub_image': subject.sub_image.url,
                'price': subject.price,
                'language': subject.language,
                'difficulty': subject.difficulty,
                'description': subject.description,
                'sub_video_list': sub_video_dict
            }
            print(sub_video_dict)
            return render(request, 'subjects/subjectForm.html', context=update_list)
        else:
            return redirect('/')

    @verify_user_class
    def post(self, request, pk):
        if request.user is not None and Member.objects.filter(id=request.user, type=True).exists():
            print('hihihihih')
            name = request.POST['lecture-title']
            sub_image = request.FILES['lecture-photo']
            price = request.POST['lecture-price']
            language = request.POST['lecture-lang']
            difficulty = request.POST['lecture-level']
            description = request.POST['lecture-desc']
            sub_video_list = json.loads(request.POST['curriculumLists'])
            subject_val_list = [name, sub_image, price, language, difficulty, description, sub_video_list]
            if subject_validate(subject_val_list):
                update_subject = Subject.objects.get(id=pk)
                update_subject(name=name, sub_image=sub_image, price=price, language=language, difficulty=difficulty,
                        description=description,
                        )
                # update_subject.save()
                print('수정성공')
                SubVideoUrl.objects.filter(sub_id_id=pk).delete()
                for key, val in sub_video_list.items():
                    update_sub_video = SubVideoUrl(sub_id_id=pk, sub_video=val, sub_video_name=key)
                    # update_sub_video.save()
                print('url 수정성공')

                return redirect('subjects:subject_detail')
        else:
            return redirect('/')



class SubjectDetailView(View):
    @verify_user_class
    def get(self, request, pk):
        print(request.user)
        if request.user is not None:
            if ClassRoom.objects.filter(sub_id=pk, mem_id=request.user).exists():
                subject = get_object_or_404(Subject, id=pk)
                video_list = subject.video_urls.all()
                name = Member.objects.get(id=request.user).name
                context = {
                    'subject': subject,
                    'video': video_list,
                    'name': name,
                    'mysubject': '강의보기'
                }
                return render(request, 'subjects/subjectDetail.html', context=context)
            else:
                subject = get_object_or_404(Subject, id=pk)
                video_list = subject.video_urls.all()
                name = Member.objects.get(id=request.user).name
                context = {
                    'subject': subject,
                    'video': video_list,
                    'name': name,
                            }
                return render(request, 'subjects/subjectDetail.html', context=context)
        else:
            subject = get_object_or_404(Subject, id=pk)
            video_list = subject.video_urls.all()
            context = {
                'subject': subject,
                'video': video_list,
            }
            return render(request, 'subjects/subjectDetail.html', context=context)

    def post(self, request, pk):
        return redirect('/')


class SubjectCreate(View):
    @verify_user_class
    def get(self, request):
        if Member.objects.filter(id=request.user, type=True).exists():
            return render(request, 'subjects/subjectForm.html', {})
        else:
            return redirect('/')

    @verify_user_class
    def post(self, request):
        print('hibye')
        if request.user is not None and Member.objects.filter(id=request.user, type=True).exists():
            try:
                print('hibyes')
                name = request.POST['lecture-title']
                sub_image = request.FILES['lecture-photo']
                price = request.POST['lecture-price']
                language = request.POST['lecture-lang']
                difficulty = request.POST['lecture-level']
                description = request.POST['lecture-desc']
                price = int(price)
                sub_video_list = json.loads(request.POST['curriculumLists'])
            except Exception as e:
                print(e)
                return JsonResponse({'msg0': '값을 모두 입력해 주세요'}, status=200)

            subject_val_list = [name, sub_image, price, language, difficulty, description, sub_video_list]
            print(subject_val_list)
            if subject_validate(subject_val_list) is not True:
                return JsonResponse(subject_validate(subject_val_list), safe=False, status=200)

            if Member.objects.filter(id=request.user).exists():
                new_subject = Subject(
                    name=name,
                    sub_image=sub_image,
                    price=int(price),
                    rating=3,
                    language=language,
                    difficulty=difficulty,
                    description=description,
                    teacher=Member.objects.get(id=request.user)
                )
                # new_subject.save()
                print('저장성공')
                for key, val in sub_video_list.items():
                    print(key, val)
                    new_sub_video = SubVideoUrl(
                        sub_id_id=new_subject.id,
                        sub_video_name=key,
                        sub_video=val
                                                )
                    print(new_sub_video)
                    # new_sub_video.save()
                print('sub저장성공')
                teacher_name = Member.objects.get(id=request.user).name
                message = {
                    'name': teacher_name,
                    'subject_name': new_subject.name
                }
                return JsonResponse(message, status=200)
            else:
                print('여기2')
                return redirect('/')
        else:
            print('여기')
            return redirect('/')


class SubjectDeleteView(View):
    @verify_user_class
    def get(self, request, pk):
        if Subject.objects.filter(id=pk, teacher=request.user):
            subject = get_object_or_404(Subject, id=pk)
            context = {
                'name': subject.name,
                'teacher': subject.teacher.name,
            }
            return render(request, 'subjects/deleteConfirm.html', context=context)
        else:
            return redirect('/')

    @verify_user_class
    def post(self, request, pk):
        if Subject.objects.filter(id=pk, teacher=request.user):
            subject = get_object_or_404(Subject, id=pk)
            subject.delete()
            return redirect('accounts:mypage')
        else:
            return redirect('/')


class Lecture(View):
    @verify_user_class
    def get(self, request, pk):
        if ClassRoom.objects.filter(sub_id=pk, mem_id=request.user).exists():
            lecture = Subject.objects.get(id=pk)
            lecture_info = {}
            for i in lecture.video_urls.values():
                sub_video = i.get('sub_video')
                sub_video_name = i.get('sub_video_name')
                lecture_info[sub_video_name] = sub_video
            context = {
                'lecture': lecture.name,
                'video': lecture.video_urls.values_list('sub_video', flat=True)[0],
                'lecture_info': lecture_info
            }
            print(lecture_info)
            print(type(lecture_info))
            return render(request, 'subjects/subjectLearning.html', context=context)
        else:
            return redirect('/')


class Pay(View):
    def get(self, request, pk):
        return redirect('/')

    @pay
    def post(self, request, pk):
        if request.user is not None and request.method == 'POST':
            price = request.POST['price']
            price = int(price)
            subject_price = Subject.objects.get(id=pk).price
            if price >= subject_price:
                message = {
                    'result': 1
                }
                new_class = ClassRoom(sub_id=pk, mem_id=request.user)
                new_class.save()
                return JsonResponse(message, status=200)
            else:
                message = {
                    'result': -1
                }
                return JsonResponse(message, status=200)
        # return redirect('/accounts/')
        message = {
            'result': -2
        }
        return JsonResponse(message, status=200)