# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is my Home")

def about(request):
    return render(request,'about.html')

def category(request):
    return render(request,'category.html')

def work(request):
    return render(request,'work.html')

