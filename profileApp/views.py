from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from .models import UserModel
from homeApp.models import AnswersModel, Followers, QuestionsModel, FollowModel
from django.contrib import messages
from django.urls import reverse


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
            all_fields = [user_model.designation, user_model.city, user_model.state, user_model.age, user_model.gender, user_model.bio, user_model.profile_photo]
            if all(all_fields) == True and user_model.points_update == 'not_updated':
                user_model.points += 10
                user_model.points_update = 'updated'
                user_model.save()
            return redirect("/profile/dashboard")
    return render(request, "profile/edit_profile.html", {'edit_profile':'profile_link_active'})

@login_required(login_url='/login')
def followersView(request):
    return render(request, "profile/followers.html", {'follower_link':'profile_link_active'})

@login_required(login_url='/login')
def ProfileFollowView(request, f_id):
    follow_to = get_object_or_404(User, id=request.POST.get('follow_btn_prof2'))
    
    following = FollowModel.objects.filter(u=request.user, followed_to=follow_to)
    is_following = True if following else False
    if is_following:
        obj,create = FollowModel.objects.get_or_create(u=request.user)
        obj.followed_to.remove(follow_to)
        us,cret = Followers.objects.get_or_create(card_user=follow_to)
        us.followed_by.remove(request.user)
        got_user = UserModel.objects.get(user_id=follow_to.id)
        got_user.points -= 7
        got_user.save()
        

    else:
        obj,create = FollowModel.objects.get_or_create(u=request.user)
        obj.followed_to.add(follow_to)
        us,cret = Followers.objects.get_or_create(card_user=follow_to)
        us.followed_by.add(request.user)
        got_user = UserModel.objects.get(user_id=follow_to.id)
        got_user.points += 7
        got_user.save()

    follower_card = f"#follower_card_{f_id}"
    return redirect(reverse('followers_main')+follower_card)


@login_required(login_url='/login')
def followingsView(request):
    return render(request, "profile/followings.html", {'followings':'profile_link_active'})

@login_required(login_url='/login')
def ProfileFollowingsView(request, f_ing_id):
    follow_to = get_object_or_404(User, id=request.POST.get('following_btn_prof'))
    
    following = FollowModel.objects.filter(u=request.user, followed_to=follow_to)
    is_following = True if following else False
    if is_following:
        obj,create = FollowModel.objects.get_or_create(u=request.user)
        obj.followed_to.remove(follow_to)
        us,cret = Followers.objects.get_or_create(card_user=follow_to)
        us.followed_by.remove(request.user)
        got_user = UserModel.objects.get(user_id=follow_to.id)
        got_user.points -= 7
        got_user.save()
        
    return redirect(reverse('followings_main'))



@login_required(login_url='/login')
def userQueView(request):
    que_data = QuestionsModel.objects.all().filter(user_id=request.user.id)
    return render(request, "profile/user_questions.html",{'questions':'profile_link_active','que_data':que_data})

@login_required(login_url='/login')
def userAnsView(request):
    given_anss = AnswersModel.objects.filter(ans_by=request.user)
    
    return render(request, "profile/user_answers.html", {'answers':'profile_link_active', 'given_anss':given_anss})


def DeleteQue(request, que_id):
    que = QuestionsModel.objects.get(id=que_id)
    que.delete()
    messages.add_message(request, messages.SUCCESS, 'Your question has been deleted.')
    return redirect(reverse('userquestions'))

def DeleteAns(request, ans_id):
    ans = AnswersModel.objects.get(id=ans_id)
    ans.delete()
    messages.add_message(request, messages.SUCCESS, 'Your answer has been deleted.')
    return redirect(reverse('useranswers'))

def logoutView(request):
    auth.logout(request)
    return redirect('/')