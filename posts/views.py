from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("All Time High!!")
# Create your views here.
