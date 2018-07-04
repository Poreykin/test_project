from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from paypalrestsdk import configure, Payment

@login_required
def pay(request):
    configure({
      "mode": "sandbox", # sandbox or live
      "client_id": "AYC0aWHLKVnQkuFMdnPZfIz5J2VR4lTmM9ghU_szP9QT95xkWo0NQZNZ6Rme11MSw9P9SCejMfhSlakU",
      "client_secret": "EAu4fR7ccEdPU8Np-5ljZOaEyReXM-nC5Aetwdz_uiGef6ZeUc11plBjAso3BeNAj_Tc_0WnfCn8m2e9" })

    payment = Payment({
        "intent": "sale",

        # Set payment method
        "payer": {
            "payment_method": "paypal"
        },

        # Set redirect urls
        "redirect_urls": {
            "return_url": "http://localhost:8000/pay/success",
            "cancel_url": "http://localhost:8000/pay/cancel"
        },

        # Set transaction object
        "transactions": [{
            "amount": {
                "total": "1.00",
                "currency": "RUB"
            },
            "description": "payment description"
        }]
    })

    if payment.create():
        # Extract redirect url
        for link in payment.links:
            if link.method == "REDIRECT":
                # Capture redirect url
                redirect_url = str(link.href)
                return redirect(redirect_url)
    else:
        return render(request, 'payment_error.html', context={'error': payment.error})

def pay_success(request):
    configure({
      "mode": "sandbox", # sandbox or live
      "client_id": "AYC0aWHLKVnQkuFMdnPZfIz5J2VR4lTmM9ghU_szP9QT95xkWo0NQZNZ6Rme11MSw9P9SCejMfhSlakU",
      "client_secret": "EAu4fR7ccEdPU8Np-5ljZOaEyReXM-nC5Aetwdz_uiGef6ZeUc11plBjAso3BeNAj_Tc_0WnfCn8m2e9" })
    # Payment id obtained when creating the payment (following redirect)
    payment = Payment.find(request.GET['paymentId'])

    # Execute payment using payer_id obtained when creating the payment (following redirect)
    if payment.execute({"payer_id": request.GET['PayerID']}):
        return render(request, 'payment_success.html', context={'id': payment.id})
    else:
        return render(request, 'payment_error.html', context={'error': payment.error})

def pay_cancel(request):
    return render(request, 'payment_error.html', context={'error': 'Payment cancelled.'})
