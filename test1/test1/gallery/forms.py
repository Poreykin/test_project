from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photo

attrs_dict = {'class': 'required'}

class UploadForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('image_file',)

"""class UpdateForm(forms.Form):
     name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label="")
     text = forms.CharField(widget=forms.Textarea, label="")
 
     def put_name(self, name):
         name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=name)
         form.save()
 
     def put_name(self, text):
         text = forms.CharField(widget=forms.Textarea, label=text)
 
     def clean_name(self):
         return self.cleaned_data['name']
 
     def clean_text(self):
         return self.cleaned_data['text']"""