from django.db import models
from accounts.models import Member
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from uuid import uuid4
import os


def sub_image_path(instance, filename):
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.path.join('subjects', uuid_name + extension)


class Subject(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=45)
    rating = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    sub_image = models.ImageField(upload_to=sub_image_path)
    sub_thumbnail = ImageSpecField(
        source='sub_image',
        processors=[Thumbnail(250, 250)],
        format='jpeg',
        options={'quality': 60})
    language = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='my_lectures')
    student = models.ManyToManyField(Member, through='ClassRoom', related_name='subjects')

    class Meta:
        db_table = 'subjects'
        # ordering = ['-created_at']

    def __str__(self):
        return self.name


class SubVideoUrl(models.Model):
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='video_urls')
    sub_video = models.URLField()

    class Meta:
        db_table = 'subvideos'

    def __str__(self):
        return str(self.sub_video)


class ClassRoom(models.Model):
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='mapping')
    mem = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        db_table = 'member_subject'

    def __str__(self):
        return str(self.mem)