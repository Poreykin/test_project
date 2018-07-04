from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services import CreatePayment, ExecutePayment

@login_required
def pay(request):
    created, payment = CreatePayment.execute({'return_url': 'http://localhost:8000/pay/success', 'cancel_url': 'http://localhost:8000/pay/cancel', 'total_amount': '1.00', 'currency': 'RUB'})

    if created:
        # Extract redirect url
        for link in payment.links:
            if link.method == "REDIRECT":
                # Capture redirect url
                return redirect(str(link.href))
    else:
        return render(request, 'payment_error.html', context={'error': payment.error})

@login_required
def pay_success(request):
    executed, payment = ExecutePayment.execute(request.GET)
    if executed:
        return render(request, 'payment_success.html', context={'id': payment.id})
    else:
        return render(request, 'payment_error.html', context={'error': payment.error})

@login_required
def pay_cancel(request):
    return render(request, 'payment_error.html', context={'error': 'Payment cancelled.'})
