from profileApp.models import UserModel
from django.contrib.messages.constants import ERROR
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AnswersModel, FollowModel, QuestionsModel, Followers
from django.contrib import messages
from django.urls import reverse
import time
from django.db.models import Q

# Create your views here.
def homeView(request):
    if request.method == 'POST' and request.POST.get('que_post_btn')=='que_post':
        current_user = request.user
        user_id = current_user.id
        question_model = User.objects.get(id=user_id)
        que = f"{request.POST.get('question').lower()}?"
        que_category = request.POST.get('que_category')
        que_details = request.POST.get('que_details')
        QuestionsModel.objects.create(user=question_model, question=que, que_category=que_category, que_details=que_details)
        # for points
        got_user = UserModel.objects.get(user_id=user_id)
        got_user.points += 2
        got_user.save()
        # =============
        messages.add_message(request, messages.SUCCESS, "Your question has been posted.")
        return redirect("/")
    
    questions = QuestionsModel.objects.order_by('que_date_time').reverse()
    anss = AnswersModel.objects.filter(question=questions[1])
    ans_length = len(anss)
    if request.method == 'POST' and request.POST.get('search_btn')=='que_search':
        search_que = request.POST.get('search_input').lower()
        questions = QuestionsModel.objects.filter(question__contains=search_que)
        if len(questions) == 0:
            messages.add_message(request, messages.ERROR, "Sorry we did't found related questions. Please post your question below.")
        
    if request.method == 'POST' and request.POST.get('category_input') == 'category_form':
        category = request.POST.get('category')
        questions = QuestionsModel.objects.filter(que_category__iexact=category)
        
    context = {'home':'index_link_active','nav_home':'activeTopNav', 'questions':questions, 'ans_length':ans_length
    }
    return render(request, 'home/home.html', context=context)


def peoplesView(request, **kwargs):
    all_users = User.objects.all()
    people_heading = 'Suggested Peoples'
    # to search peoples=====================
    if request.method == 'POST' and request.POST.get('find_people_btn') == 'find_people':
        people_name = request.POST.get('find_people_input').title().split(' ')
        all_users = User.objects.filter(first_name__contains=people_name[0])
        people_heading = 'Searched Peoples'
        if len(all_users) == 0:
            messages.add_message(request, messages.WARNING, "No peoples with that name.")
    # ======================================
    context = {'peoples':'index_link_active', 'nav_peoples':'activeTopNav', 'all_users':all_users, 'people_heading':people_heading}
    return render(request, 'home/peoples.html', context=context)

@login_required(login_url='/login')
def FollowView(request, p_id):
    follow_to = get_object_or_404(User, id=request.POST.get('follow_btn'))
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

    card_id = f"#card_{p_id}"
    return redirect(reverse('peoples_main')+card_id)


def writeAnsView(request, pk):
    clicked_que = QuestionsModel.objects.get(id=pk)
    # --------------------
    # views count
    clicked_que.que_views+=1
    clicked_que.save()
    # -----------------
    # for form data

    if (request.method == "POST"):
        ans_text = request.POST.get('ans_text')
        AnswersModel.objects.create(question_id=pk, answer=ans_text, ans_by=request.user)
        # for points
        got_user = UserModel.objects.get(user_id=request.user.id)
        got_user.points += 5
        got_user.save()
        # ==========
        messages.add_message(request, messages.SUCCESS, "Your answer has been added successfully.")
        return redirect(reverse('ans_page', args=(pk,)))
    
    ans_obj = AnswersModel.objects.filter(question_id=pk)
    # for showing number of answers
    ans_count = len(ans_obj)
    if ans_count == 0:
        ans_count = "No"
    else:
        ans_count = ans_count
    # ================

    # for points
    gotUser = UserModel.objects.get(user_id=clicked_que.user.id)
    if gotUser.ans_point == False:
        gotUser.points += 2
        gotUser.ans_point = True
        gotUser.save()
    # ====================
    
    context = {'answers':'index_link_active', 'clicked_que':clicked_que,'ans_obj':ans_obj, 'ans_count':ans_count
    }
    return render(request, 'home/write_ans.html', context=context)


@login_required(login_url='/login')
def LikeView(request, pk):
    ans = get_object_or_404(AnswersModel, id=request.POST.get('like_btn'))
    ans_que_id = AnswersModel.objects.get(id=pk)
    que_id = ans_que_id.question_id
    if ans.likes.filter(id=request.user.id).exists():
        ans.likes.remove(request.user)
        # for points
        got_user = UserModel.objects.get(user_id=ans.ans_by.id)
        got_user.points -= 2
        got_user.save()
        # =================
    else:
        ans.likes.add(request.user)
        # for points
        got_user = UserModel.objects.get(user_id=ans.ans_by.id)
        got_user.points += 2
        got_user.save()
        # =================
    ans_id = f"#ans_{request.POST.get('like_btn')}"
    return redirect(reverse('ans_page', args=(que_id,)) + ans_id)


# def PeopleInfo(request, pc_id):
#     people_info = User.objects.get(id=pc_id)
#     return HttpResponseRedirect(reverse('homeApp:peoplesView', kwargs={ 'people_info': people_info }))