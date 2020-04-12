from django import forms
from subjects.models import *
from accounts.models import *
from django.forms import inlineformset_factory


class SubjectForm(forms.ModelForm):
    sub_video1 = forms.URLField(max_length=255)
    class Meta:
        model = Subject
        exclude = ('student', 'teacher')
        labels = {
            'sub_video': 'sub_video1'
        }


SubjectInlineFormset = inlineformset_factory(Subject, SubVideoUrl,
                                             fields='__all__'
                                             )

