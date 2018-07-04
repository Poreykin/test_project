from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django_fsm import can_proceed, has_transition_perm
from .models import Course, Task, TaskStatus
from .forms import MoveCourseForm, CreateTaskForm, SendTaskBackForm

@login_required
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

@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            task_status = TaskStatus.objects.create(student=request.user, task=task)
            return redirect('task_view', task_status_id=task_status.pk)
    else:
        form = CreateTaskForm()
        return render(request, 'create_task.html', {'form': form, 'new': True})

@login_required
def task_view(request, task_status_id=None):
    task_status = get_object_or_404(TaskStatus, pk=task_status_id)
    if request.method == 'POST':
        form = SendTaskBackForm(request.POST)
        if form.is_valid():
            task_status.comment = form.cleaned_data['comment']
            task_status.response = form.cleaned_data['response']
            task_status.save()
            return redirect('send_task_back', task_status_id=task_status_id)
    task = task_status.task
    can_be_sent = (can_proceed(task_status.send) and has_transition_perm(task_status.send, request.user))
    review_mode = (task_status.state == 'RVW' and request.user.is_superuser)
    context = {'task': task, 'task_status': task_status, 'can_be_sent': can_be_sent, 'review_mode': review_mode, 'user': request.user}
    if review_mode:
        form = SendTaskBackForm()
        context['form'] = form
    return render(request, "task.html", context)

@login_required
def send_task(request, task_status_id=None):
    task_status = get_object_or_404(TaskStatus, pk=task_status_id)
    task_status.send()
    task_status.save()
    return redirect('task_view', task_status_id=task_status_id)

@login_required
def send_task_back(request, task_status_id=None):
    task_status = get_object_or_404(TaskStatus, pk=task_status_id)
    task_status.send_back()
    task_status.save()
    return redirect('task_view', task_status_id=task_status_id)

@login_required
def accept_task(request, task_status_id=None):
    task_status = get_object_or_404(TaskStatus, pk=task_status_id)
    task_status.accept()
    task_status.save()
    return redirect('task_view', task_status_id=task_status_id)
