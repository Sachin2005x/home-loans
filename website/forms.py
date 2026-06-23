from django import forms
from .models import Inquiry, CallbackRequest


def validate_phone(phone):

    phone = phone.strip()

    # Remove spaces and hyphens
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    # Remove +91
    if phone.startswith("+91"):
        phone = phone[3:]

    # Remove 91
    elif phone.startswith("91") and len(phone) == 12:
        phone = phone[2:]

    if not phone.isdigit():
        raise forms.ValidationError(
            "Enter a valid mobile number."
        )

    if len(phone) != 10:
        raise forms.ValidationError(
            "Mobile number must be 10 digits."
        )

    return phone


class InquiryForm(forms.ModelForm):

    def clean_phone(self):
        return validate_phone(
            self.cleaned_data.get('phone', '')
        )

    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'district',
            'loan_amount'
        ]


class CallbackForm(forms.ModelForm):

    def clean_phone(self):
        return validate_phone(
            self.cleaned_data.get('phone', '')
        )

    class Meta:
        model = CallbackRequest
        fields = [
            'name',
            'phone',
            'preferred_time'
        ]