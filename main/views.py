from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def project(request):
    return render(request, 'main/project.html')

def calc(request):
    return render(request, 'main/projects/calc.html')

def weather(request):
    return render(request, 'main/projects/weather.html')

def tictactoe(request):
    return render(request, 'main/projects/tictactoe.html')