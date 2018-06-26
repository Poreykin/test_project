import os
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Photo
from .forms import UploadForm
from test1.settings import MEDIA_ROOT

@login_required
def gallery_view(request, photo_id = None):
    if photo_id:
        photo = get_object_or_404(Photo, pk=photo_id)
        photos = [{'uploader': photo.uploader, 'id': photo.pk, 'url': os.path.join(MEDIA_ROOT, photo.image_file.url)}]
        full_list = False
    else:
        photos = [{'uploader': photo.uploader, 'id': photo.pk, 'url': MEDIA_ROOT + '/' + photo.image_file.url} for photo in Photo.objects.all()]
        full_list = True

    context = {
        'photos': photos,
        'user': request.user,
        'full_list': full_list,
    }

    return render(request, 'gallery_view.html', context)

@login_required
def upload_photo(request, photo_id = None):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('upload_photo')
        else:
            return redirect('login')
    else:
        form = UploadForm()
        return render(request, 'upload_photo.html', {'form': form, 'new': True})
