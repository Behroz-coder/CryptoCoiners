from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(index):
    return HttpResponse('this is dashoard')