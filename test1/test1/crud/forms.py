from django import forms
from .models import Article

attrs_dict = {'class': 'required'}

class CreateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('name', 'text',)

class UpdateForm(forms.Form):
     name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label="Name")
     text = forms.CharField(widget=forms.Textarea, label="Text")

     def put_name(self, name):
         name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=name)
         form.save()

     def put_text(self, text):
         text = forms.CharField(widget=forms.Textarea, label=text)
         form.save()

     def clean_name(self):
         return self.cleaned_data['name']

     def clean_text(self):
         return self.cleaned_data['text']
