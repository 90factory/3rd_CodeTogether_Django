from django.urls import path
from accounts.views import *
from accounts.member import *

app_name='accounts'

urlpatterns = [
    path('', MyPageView.as_view(), name='mypage'),
    path('signup/', SignUP.as_view(), name='signup'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('email_check/', email_check, name='email_check'),
    path('logout/', LogOut, name='logout'),
    path('delete/', DeleteUser.as_view(), name='delete_user'),
    path('repw/', RePw.as_view(), name='repw'),
    path('update/', Update.as_view(), name='update')
]