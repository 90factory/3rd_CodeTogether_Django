from django.http import JsonResponse
import re

# def subject_validate(information):
#     print(information)
#     print('타고 들어오나요')
#     if len(information[0]) < 5:
#         print('name')
#         return JsonResponse({'msg1': '너무 짧은 제목'}, status=200)
#     elif information[1] is None:
#         print('sub_image')
#         return JsonResponse({'msg2': '이미지가 없습니다'}, status=200)
#     elif information[3] not in ['Java', 'Javascript', 'Python']:
#         print('language')
#         return JsonResponse({'msg3': '언어값이 틀립니다'}, status=200)
#     elif information[4] not in ['입문', '중급', '고급']:
#         print('difficulty')
#         return JsonResponse({'msg4': '강의값이 틀립니다'}, status=200)
#     elif len(information[5]) > 1000:
#         print('description')
#         return JsonResponse({'msg5': '너무 긴 소개 입니다.'}, status=200)
#     elif type(information[2]) != int:
#         print('price')
#         return JsonResponse({'msg6': '숫자형태가 아닙니다.'}, status=200)
#     else:
#         print('sub_video_list')
#         num = 0
#         for val in information[6].values():
#             p = re.compile('(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?')
#             m = p.match(val)
#             num += 1
#             if m is None:
#                 return JsonResponse({'msg7': f'{num}번째 url이 잘못되었습니다'}, status=200)
#     return True

def subject_validate(information):
    print(information)
    if None in information:
        print('none')
        msg = {'msg1': '값을 모두 넣어주세요'}
        return msg
    elif len(information[0]) < 5:
        print('name')
        msg = {'msg1': '너무 짧은 이름'}
        return msg
    elif information[1] is None:
        msg = {'msg2': '이미지가 없습니다.'}
        return msg
    elif type(information[2]) != int:
        msg = {'msg3': '숫자가 아닙니다.'}
        return msg
    elif information[3] not in ['Java', 'Javascript', 'Python']:
        msg = {'msg4': '언어가 선택되지 않았습니다.'}
        return msg
    elif information[4] not in ['입문', '중급', '고급']:
        msg = {'msg5': '난이도가 선택되지 않았습니다.'}
        return msg
    elif len(information[5]) > 500:
        msg = {'msg6': '너무 긴 길이 입니다.'}
        return msg
    else:
        if information[6] is None:
            print('difhidfhi')
            return JsonResponse({'msg8': '강의를 입력해 주세요'})
        else:
            print(information[6])
            num = 0
            for val in information[6].values():
                p = re.compile('(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?')
                m = p.match(val)
                num += 1
                if m is None:
                    msg = {'msg7': f'{num}째가 url이 아닙니다'}
                    return msg
    return True

# info = ['파이썬으로 배우는 프로그래밍', '/media/tmp/sdflifjl', 23423, 'Python', '입문',
#         'ㄴㅇㄹㅎㅁㄴㅇㅎㅁㄴㅇㅎㅁㄹㄴㅇㅁㄹㅁㄴㅇㄹㄴㅇㄹㄴㅁㅇㄹㅁㄴㄹㄴㅁㅇㄹㅁㄴㅇㄴㅇㅁㄹㅁㄴㅇ',
#         {'1강': 'https://youtube.com/embewd/weoFEfjwif',
#          }]

# print(subject_validate(info))