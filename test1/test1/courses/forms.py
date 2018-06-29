from django import forms
from .models import Course

attrs_dict = {'class': 'required'}

class MoveCourseForm(forms.Form):
    courses_ids = [(course.pk, course.name) for course in Course.objects.all()]
    courses_names = [(course.name, course.name) for course in Course.objects.all()]

    id = forms.ChoiceField(choices=courses_ids, label="id")
    left = forms.ChoiceField(choices=[('NONE', 'To the left')]+courses_names, label="left")
    right = forms.ChoiceField(choices=courses_names+[('NONE', 'To the right')], label="right")
