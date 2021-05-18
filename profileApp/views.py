from django.shortcuts import render

# Create your views here.
def profileView(request):
    return render(request, "profile/profile.html")

def editProfileView(request):
    return render(request, "profile/edit_profile.html")

def followersView(request):
    return render(request, "profile/followers.html")

def followingsView(request):
    return render(request, "profile/followings.html")

def userQueView(request):
    return render(request, "profile/user_questions.html")

def userAnsView(request):
    return render(request, "profile/user_answers.html")