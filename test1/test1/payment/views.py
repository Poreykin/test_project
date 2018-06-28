from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cloudpayments import CloudPayments
from .forms import SubmitCreditCardForm



@login_required
def pay(request):
    #client = CloudPayments('public_id', 'api_secret')
    #message = client.test()
    message = ''

    form = SubmitCreditCardForm()
    return render(request, 'payment.html', context={'message': message, 'form': form})
