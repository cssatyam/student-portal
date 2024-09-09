from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import PasswordResetRequestForm

# Create your views here.
def index(request):
    return render(request, 'student.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')


# def resetpassword(request):
#     if request.method == "POST":
#         form = PasswordResetRequestForm(request.POST)
#         if form.is_valid():
#             email_or_phone = form.cleaned_data['email_or_phone']
#             users = User.objects.filter(email=email_or_phone) | User.objects.filter(profile__phone_number=email_or_phone)

#             if users.exists():
#                 for user in users:
#                     token = default_token_generator.make_token(user)
#                     uid = urlsafe_base64_encode(force_bytes(user.pk))
#                     password_reset_url = request.build_absolute_uri(f'/reset/{uid}/{token}/')

#                     # Send Email with the reset link
#                     send_mail(
#                         subject="Password Reset Request",
#                         message=f"Click the link to reset your password: {password_reset_url}",
#                         from_email='noreply@yourdomain.com',
#                         recipient_list=[user.email],
#                     )

#                 messages.success(request, "Password reset link has been sent to your email.")
#                 return redirect('login')
#             else:
#                 messages.error(request, "No user found with this email or phone number.")
#     else:
#         form = PasswordResetRequestForm()
    
#     return render(request, "resetpassword.html", {"form": form})