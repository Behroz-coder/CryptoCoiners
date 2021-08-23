from django.shortcuts import render, HttpResponse

# Create your views here.
def user(index):
    return HttpResponse('this is user')