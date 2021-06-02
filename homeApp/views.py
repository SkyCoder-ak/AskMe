from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AnswersModel, QuestionsModel
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
    return render(request, 'home/peoples.html', {'peoples':'index_link_active'})

def writeAnsView(request, que_id):
    # getting the question which click by ans button
    clicked_que = QuestionsModel.objects.get(id=que_id)
    # --------------------
    # views count
    clicked_que.que_views+=1
    clicked_que.save()
    # -----------------
    # for form data
    if request.method == "POST":
        ans_text = request.POST.get('ans_text')
        AnswersModel.objects.create(question_id=que_id, answer=ans_text, ans_by=request.user)
        messages.add_message(request, messages.SUCCESS, "Your answer has been added successfully.")
        return redirect(reverse('ans_page', args=(que_id,)))
    
    ans_obj = AnswersModel.objects.filter(question_id=que_id)
    # for showing number of answers
    ans_count = len(ans_obj)
    if ans_count == 0:
        ans_count = "No"
    else:
        ans_count = ans_count


    return render(request, 'home/write_ans.html', {'answers':'index_link_active', 'clicked_que':clicked_que, 'ans_obj':ans_obj, 'ans_count':ans_count
    })
