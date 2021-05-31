from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import QuestionsModel
from django.contrib import messages

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

    return render(request, 'home/home.html', {'home':'index_link_active','questions':questions
    })


def peoplesView(request):
    return render(request, 'home/peoples.html', {'peoples':'index_link_active'})

def writeAnsView(request):
    return render(request, 'home/write_ans.html', {'answers':'index_link_active'})
