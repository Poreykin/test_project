from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from .models import Course
from .forms import MoveCourseForm

def courses_view(request):
    if request.method == "POST":
        form = MoveCourseForm(request.POST)
        if form.is_valid():
            course = Course.objects.get(pk=form.cleaned_data['id'])
            if form.cleaned_data['left'] != 'NONE':
                course_left = Course.objects.get(name=form.cleaned_data['left'])
                if course_left.is_leaf_node():
                    Course.objects.move_node(course, course_left, position='right')
                else:
                    Course.objects.move_node(course, course_left, position='first-child')
            elif form.cleaned_data['right'] != 'NONE':
                course_right = Course.objects.get(name=form.cleaned_data['right'])
                Course.objects.move_node(course, course_right, position='left')
            return redirect('courses')
    courses = Course.objects.all()
    form = MoveCourseForm()
    return render(request, "courses.html", {'courses': courses, 'form': form})
