from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("INDEX")

def add(request):
  return render(request, "tareas/add.html")

def eva(request):
  return render(request, "tareas/eva.html")