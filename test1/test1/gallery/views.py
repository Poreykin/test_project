import os
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Photo
from .forms import UploadForm
from test1.settings import MEDIA_ROOT

@login_required
def gallery_view(request):
    photos = [{'uploader': photo.uploader, 'id': photo.pk, 'image': photo.image_file} for photo in Photo.objects.all()]
    full_list = True

    context = {
        'photos': photos,
        'user': request.user,
        'full_list': full_list,
    }

    return render(request, 'gallery_view.html', context)

@login_required
def upload_photo(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.image_thumbnail = form.cleaned_data['image_file']
            photo.image_thumbnail2 = form.cleaned_data['image_file']
            photo.image_thumbnail3 = form.cleaned_data['image_file']
            photo.uploader = request.user
            photo.save()
            return redirect('gallery_view')
    else:
        form = UploadForm()
        return render(request, 'upload_photo.html', {'form': form, 'new': True})

@login_required
def delete_photo(request, photo_id = None):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user.username == photo.uploader.username:
        photo.delete()

    return redirect('gallery_view')
