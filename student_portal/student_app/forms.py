from django import forms

class PasswordResetRequestForm(forms.Form):
    email_or_phone = forms.CharField(label="Enter your Email or Phone number", max_length=254)
