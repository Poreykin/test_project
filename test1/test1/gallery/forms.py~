from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photo

attrs_dict = {'class': 'required'}

class UploadForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('image_file',)
