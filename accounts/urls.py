from django.urls import path
from accounts.views import *

app_name='accounts'

urlpatterns = [
    path('', MyPageView.as_view(), name='mypage'),
    path('test/', test, name='test')
]