from django.shortcuts import render

# Create your views here.
def signupView(request):

    return render(request, "signup/signup.html")