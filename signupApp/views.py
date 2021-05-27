from django.shortcuts import redirect, render
from .forms import UserRegForm
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def signupView(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            fName = full_name.split(' ')
            first_name = fName[0]
            last_name = fName[-1]
            dis_name = request.POST['dis_name']
            email = request.POST['email']
            password = request.POST["password"]
            
            usr = User.objects.create_user(username=dis_name, email=email, first_name=first_name, last_name=last_name, password=password )
            usr.save()
            messages.add_message(request, messages.SUCCESS, "Your account has been created successfully.")
            return redirect("/login")
    else:
        form = UserRegForm()
    return render(request, "signup/signup.html", {'form': form})