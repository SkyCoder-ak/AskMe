from profileApp.models import UserModel
from django.shortcuts import redirect, render
from .forms import UserRegForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db import IntegrityError
from django.core.mail import send_mail
from AskMe import settings
import random


# Create your views here.
def signupView(request):
    if request.method == 'POST':
        try:
            form = UserRegForm(request.POST)
            if form.is_valid():
                full_name = request.POST['full_name']
                fName = full_name.split(' ')
                first_name = fName[0]
                last_name = fName[-1]
                dis_name = request.POST['dis_name']
                email = request.POST['email']
                password = request.POST["password"]
                user_email = User.objects.filter(email=email)
                if len(user_email) == 0:
                    usr = User.objects.create_user(username=dis_name, email=email, first_name=first_name, last_name=last_name, password=password, is_active=False)
                    usr.save()
                    request.session['user_id'] = usr.id
                    usr.usermodel.full_name = full_name.lower()
                    usr.usermodel.save()

                    # for sending otp
                    otp_num = random.randint(11111,99999)
                    usr.usermodel.otp = otp_num
                    usr.usermodel.save()
                    mail_message = f'Your are almost there {usr.first_name},\n here is your OTP: {otp_num} '
                    sender = 'beyondhorrizon7@gmail.com'
                    recipients = [str(usr.email)]
                    sent = send_mail('Verify Your Email', mail_message, sender, recipients, fail_silently=False,auth_user=settings.EMAIL_HOST_USER,auth_password=settings.EMAIL_HOST_PASSWORD)
                    if sent == 1:
                        messages.add_message(request, messages.WARNING, "We sended an OTP to your email. Please verify your email with OTP.", extra_tags='otp_sent')
                    else:
                        messages.add_message(request, messages.ERROR, "Please enter correct email address.", extra_tags='email_fail')
                    # =====================

                    # to increate point
                    new_user = User.objects.get(username=usr)
                    new_user.usermodel.points += 20
                    new_user.usermodel.save()
                    # =====================
                    
                    return redirect("/signup")
                else:
                    messages.add_message(request, messages.WARNING, "Email is already taken.", extra_tags='email_exists')
                    return redirect("/signup")

        except IntegrityError:
            messages.add_message(request, messages.WARNING, "Username is already taken.", extra_tags='username_exists')
    else:
        form = UserRegForm()
    return render(request, "signup/signup.html", {'form': form})

def OtpView(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        otp = request.POST['otp']
        if int(otp) == user.usermodel.otp:
            user.is_active = True
            user.save()
            user.usermodel.otp = None
            user.usermodel.save()
            request.session['user_id'] = {}
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Wrong OTP', extra_tags='wrong_otp')

    return render(request, 'signup/otp.html')