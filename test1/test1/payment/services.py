from django import forms
from service_objects.services import Service
from paypalrestsdk import configure, Payment
from test1.settings import PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET

def configure_paypal():
    configure({
      "mode": "sandbox", # sandbox or live
      "client_id": PAYPAL_CLIENT_ID,
      "client_secret": PAYPAL_CLIENT_SECRET })

    return

class CreatePayment(Service):
    return_url = forms.URLField()
    cancel_url = forms.URLField()
    total_amount = forms.CharField()
    currency = forms.CharField()

    def process(self):
        configure_paypal()

        payment = Payment({
            "intent": "sale",

            # Set payment method
            "payer": {
                "payment_method": "paypal"
                },

            # Set redirect urls
            "redirect_urls": {
                "return_url": self.cleaned_data['return_url'],
                "cancel_url": self.cleaned_data['cancel_url'],
            },

            # Set transaction object
            "transactions": [{
                "amount": {
                    "total": self.cleaned_data['total_amount'],
                    "currency": self.cleaned_data['currency'],
                },
            }]
        })

        created = payment.create()
        return created, payment

class ExecutePayment(Service):
    paymentId = forms.CharField()
    PayerID = forms.CharField()

    def process(self):
        configure_paypal()

        # Payment id obtained when creating the payment (following redirect)
        payment = Payment.find(self.cleaned_data['paymentId'])

        # Execute payment using payer_id obtained when creating the payment (following redirect)
        executed = payment.execute({"payer_id": self.cleaned_data['PayerID']})
        return executed, payment
