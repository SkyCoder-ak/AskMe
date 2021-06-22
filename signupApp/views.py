from django.shortcuts import redirect, render
from .forms import UserRegForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db import IntegrityError

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
                    usr = User.objects.create_user(username=dis_name, email=email, first_name=first_name, last_name=last_name, password=password )
                    usr.save()

                    usr.usermodel.full_name = full_name.lower()
                    usr.usermodel.save()
                    # to increate point
                    new_user = User.objects.get(username=usr)
                    new_user.usermodel.points += 20
                    new_user.usermodel.save()
                    # =====================
                    messages.add_message(request, messages.SUCCESS, "Your account has been created successfully.")
                    return redirect("/signup")
                else:
                    messages.add_message(request, messages.WARNING, "Email is already taken.", extra_tags='email_exists')
                    return redirect("/signup")

        except IntegrityError:
            messages.add_message(request, messages.WARNING, "Username is already taken.", extra_tags='username_exists')
    else:
        form = UserRegForm()
    return render(request, "signup/signup.html", {'form': form})