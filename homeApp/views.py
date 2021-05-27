from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return render(request, 'home/home.html', {'home':'index_link_active'})


def peoplesView(request):
    return render(request, 'home/peoples.html', {'peoples':'index_link_active'})

def writeAnsView(request):
    return render(request, 'home/write_ans.html', {'answers':'index_link_active'})