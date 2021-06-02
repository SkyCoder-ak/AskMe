from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from .models import UserModel
from homeApp.models import AnswersModel, QuestionsModel
from django.contrib import messages


# Create your views here.
@login_required(login_url='/login')
def profileView(request):
    user_ques = QuestionsModel.objects.filter(user=request.user)
    user_ques_len = len(user_ques)
    user_ans = AnswersModel.objects.filter(ans_by=request.user)
    user_ans_len = len(user_ans)

    return render(request, "profile/profile.html", {'dashboard':'profile_link_active', 'user_ques_len':user_ques_len, 'user_ans_len':user_ans_len})

@login_required(login_url='/login')
def editProfileView(request):
    if request.method == 'POST':
        current_user = User.objects.get(id=request.user.id)
        old_pass = request.POST.get('old_password')
        new_pass1 = request.POST.get('new_pass1')
        new_pass2 = request.POST.get('new_pass2')
        check_old_pass = current_user.check_password(old_pass)
        if (old_pass is not None):
            if (check_old_pass == True) and (new_pass1 == new_pass2):
                current_user.set_password(new_pass1)
                current_user.save()
                messages.add_message(request, messages.SUCCESS, "Your password has been changed successfully.")
                redirect('/profile/dashboard')
            else:
                messages.add_message(request, messages.ERROR, "Password not matched.")
                redirect('/profile/edit-profile')
        else:
        # getting all input values from template
            fullname = request.POST.get('fullname')
            fullname = fullname.split(" ")
            first_name = fullname[0]
            last_name = fullname[-1]
            username = request.POST.get('display_name')
            designation = request.POST.get('designation')
            city = request.POST.get('city')
            state = request.POST.get('state')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            bio = request.POST.get('bio')
            profile_img = request.FILES.get('avtar_img')
            # first saving the auth_user model
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.username = username
            current_user.email = email
            current_user.save()
            # saving the changes of UserModel
            user_model = UserModel.objects.get(user=request.user)
            user_model.designation = designation
            user_model.city = city
            user_model.state = state
            user_model.age = age
            user_model.gender = gender
            user_model.bio = bio
            user_model.profile_photo = profile_img
            user_model.save()
            
            messages.add_message(request, messages.SUCCESS, "Your profile has been updated successfully.")
            return redirect("/profile/dashboard")
    return render(request, "profile/edit_profile.html", {'edit_profile':'profile_link_active'})


def followersView(request):
    return render(request, "profile/followers.html", {'followers':'profile_link_active'})

def followingsView(request):
    return render(request, "profile/followings.html", {'followings':'profile_link_active'})

@login_required(login_url='/login')
def userQueView(request):
    que_data = QuestionsModel.objects.all().filter(user_id=request.user.id)
    return render(request, "profile/user_questions.html",{'questions':'profile_link_active','que_data':que_data})

@login_required(login_url='/login')
def userAnsView(request):
    given_anss = AnswersModel.objects.filter(ans_by=request.user)
    
    return render(request, "profile/user_answers.html", {'answers':'profile_link_active', 'given_anss':given_anss})

def logoutView(request):
    auth.logout(request)
    return redirect('/')