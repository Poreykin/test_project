from django import forms
from .models import Photo

attrs_dict = {'class': 'required'}

class UploadForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('image_file',)
