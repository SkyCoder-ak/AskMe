from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            print("login success")
            return redirect("/profile/dashboard")
        else:
            messages.add_message(request, messages.ERROR, "Incorrect Username or Password.!!!")
            return redirect('/login')
    else:
        form = LoginForm()
        return render(request, "login/login.html", {'form':form})