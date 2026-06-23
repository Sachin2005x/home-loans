import json
import urllib.error
import urllib.request

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import CallbackForm, InquiryForm


def home(request):
    inquiry_form = InquiryForm()
    callback_form = CallbackForm()

    if request.method == 'POST':
        if 'callback_submit' in request.POST:
            callback_form = CallbackForm(request.POST)
            if callback_form.is_valid():
                callback = callback_form.save()
                print(f'Callback saved: {callback.name} / {callback.phone}')
                print(f'Notifying via email to: {getattr(settings, "NOTIFICATION_EMAIL", None)}')
                notify_callback_request(callback)
                return redirect('callback_success')
        else:
            inquiry_form = InquiryForm(request.POST)
            if inquiry_form.is_valid():
                inquiry = inquiry_form.save()
                notify_inquiry(inquiry)
                return redirect('success')

    return render(request, 'home.html', {
        'form': inquiry_form,
        'callback_form': callback_form,
    })


def home_purchase(request):
    return render(request, 'services/home_purchase.html')


def construction(request):
    return render(request, 'services/construction.html')


def renovation(request):
    return render(request, 'services/renovation.html')


def services(request):
    return render(request, 'services/services.html')


def extension(request):
    return render(request, 'services/extension.html')


def plot_construction(request):
    return render(request, 'services/plot_construction.html')


def balance_transfer(request):
    return render(request, 'services/balance_transfer.html')


def topup(request):
    return render(request, 'services/topup.html')


def loan_against_property(request):
    return render(request, 'services/lap.html')


def emi_calculator(request):
    return render(request, 'emi.html')


def success(request):
    return render(request, 'success.html')


def callback_success(request):
    return render(request, 'callback_success.html')



def about(request):
    return render(request, 'about.html')


def notify_inquiry(inquiry):
    subject = 'New Home Loan Inquiry'
    message = (
        f'New inquiry received:\n'
        f'Name: {inquiry.name}\n'
        f'Phone: {inquiry.phone}\n'
        f'District: {inquiry.district}\n'
        f'Loan Amount: {inquiry.loan_amount}\n'
        f'Received: {inquiry.created_at}\n'
    )
    send_notifications(subject, message)


def notify_callback_request(callback):
    subject = 'New Callback Request'
    message = (
        f'New callback request received:\n'
        f'Name: {callback.name}\n'
        f'Phone: {callback.phone}\n'
        f'Preferred Time: {callback.preferred_time}\n'
        f'Received: {callback.created_at}\n'
    )
    send_notifications(subject, message)


def send_notifications(subject, message):
    recipient = getattr(settings, 'NOTIFICATION_EMAIL', None)
    if not recipient and getattr(settings, 'ADMINS', None):
        recipient = settings.ADMINS[0][1]
    if not recipient:
        recipient = 'admin@example.com'

    try:
        result = send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
        print(f'✓ Email sent successfully to {recipient}')
    except Exception as exc:
        # Print the actual error so user can debug
        print(f'✗ Email notification failed: {exc}')
        import traceback
        traceback.print_exc()

    if getattr(settings, 'WHATSAPP_API_TOKEN', '') and getattr(settings, 'WHATSAPP_PHONE_ID', '') and getattr(settings, 'WHATSAPP_RECIPIENT_NUMBER', ''):
        payload = json.dumps({
            'messaging_product': 'whatsapp',
            'to': settings.WHATSAPP_RECIPIENT_NUMBER,
            'type': 'text',
            'text': {'body': message},
        }).encode('utf-8')

        request = urllib.request.Request(
            f'https://graph.facebook.com/v16.0/{settings.WHATSAPP_PHONE_ID}/messages',
            data=payload,
            headers={
                'Authorization': f'Bearer {settings.WHATSAPP_API_TOKEN}',
                'Content-Type': 'application/json',
            },
            method='POST',
        )
        try:
            urllib.request.urlopen(request, timeout=15)
        except urllib.error.URLError:
            pass
