from django import forms

attrs_dict = {'class': 'required'}
months = [("%02d" % (i,), "%02d" % (i,)) for i in range(1, 13)]

class SubmitCreditCardForm(forms.Form):
    card_number = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), min_length=16, max_length=16, label="Card number")
    name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label="Name")
    expire_month = forms.ChoiceField(choices=months, label="Month")
    expire_year = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), min_length=2, max_length=2, label="Year")
    cvv = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), min_length=3, max_length=3, label="CVV")
