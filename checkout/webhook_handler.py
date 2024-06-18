from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown or unexpected
            webbhook event """
        return HttpResponse(
            conten=f'Unhandled Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle they payment_intent.succeeded webhook from stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            conten=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle they payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            conten=f'Webhook recieved: {event["type"]}',
            status=200)