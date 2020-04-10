from django.db import models


from django.db import models
from uuid import uuid4
import datetime
import os


class Member(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    type = models.BooleanField(default=False)
    social = models.BooleanField(default=False)
    valid = models.BooleanField(default=False)
    naver_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return str(self.name)


def teacher_path(instance, filename):
    d = datetime.datetime.now()
    today = d.strftime('%Y-%m-%d')
    extension = os.path.splitext(filename)[-1].lower()
    uuid_name = uuid4().hex
    return os.path.join('teachers', today, uuid_name+extension)


class Teacher(models.Model):
    member_id = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to=teacher_path)

    def __str__(self):
        return str(self.member_id)







