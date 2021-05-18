from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return render(request, 'home/home.html')


def peoplesView(request):
    return render(request, 'home/peoples.html')

def writeAnsView(request):
    return render(request, 'home/write_ans.html')