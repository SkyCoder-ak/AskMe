from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AnswersModel, FollowModel, QuestionsModel, Followers
from django.contrib import messages
from django.urls import reverse
import time

# Create your views here.
def homeView(request):
    if request.method == 'POST':
        current_user = request.user
        user_id = current_user.id
        question_model = User.objects.get(id=user_id)
        que = request.POST.get('question')
        que_category = request.POST.get('que_category')
        que_details = request.POST.get('que_details')
        QuestionsModel.objects.create(user=question_model, question=que, que_category=que_category,que_details=que_details)
        
        messages.add_message(request, messages.SUCCESS, "Your question has been posted.")
        
        return redirect("/")
    
    questions = QuestionsModel.objects.order_by('que_date_time').reverse()
    anss = AnswersModel.objects.filter(question=questions[1])
    ans_length = len(anss)
    

    return render(request, 'home/home.html', {'home':'index_link_active','questions':questions, 'ans_length':ans_length
    })


def peoplesView(request):
    all_users = User.objects.all()
    return render(request, 'home/peoples.html', {'peoples':'index_link_active','all_users':all_users})

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
        

    else:
        obj,create = FollowModel.objects.get_or_create(u=request.user)
        obj.followed_to.add(follow_to)
        us,cret = Followers.objects.get_or_create(card_user=follow_to)
        us.followed_by.add(request.user)

    card_id = f"#card_{p_id}"
    return redirect(reverse('peoples_main')+card_id)


def writeAnsView(request, pk):
    # getting the question which click by ans button
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
        messages.add_message(request, messages.SUCCESS, "Your answer has been added successfully.")
        return redirect(reverse('ans_page', args=(pk,)))
    
    ans_obj = AnswersModel.objects.filter(question_id=pk)
    # for showing number of answers
    ans_count = len(ans_obj)
    if ans_count == 0:
        ans_count = "No"
    else:
        ans_count = ans_count

    context = {'answers':'index_link_active', 'clicked_que':clicked_que,'ans_obj':ans_obj, 'ans_count':ans_count
    }
    return render(request, 'home/write_ans.html', context=context)

@login_required(login_url='/login')
def LikeView(request, pk):
    ans = get_object_or_404(AnswersModel, id=request.POST.get('like_btn'))
    ans_que_id = AnswersModel.objects.get(id=pk)
    que_id = ans_que_id.question_id
    is_liked = False
    if ans.likes.filter(id=request.user.id).exists():
        ans.likes.remove(request.user)
        is_liked = False
    else:
        ans.likes.add(request.user)
        is_liked = True
    ans_id = f"#ans_{request.POST.get('like_btn')}"
    return redirect(reverse('ans_page', args=(que_id,)) + ans_id)
    