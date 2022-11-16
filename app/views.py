from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')


def question(request, question_id):
    return render(request,'question.html')


def ask(request):
    return render(request,'ask.html')


def login(request):
    return render(request,'login.html')


def settings(request):
    return render(request,'settings.html')


def signup(request):
    return render(request,'signup.html')


def tagged_question(request, question_tag):
    return render(request,'tagQuestion.html')
