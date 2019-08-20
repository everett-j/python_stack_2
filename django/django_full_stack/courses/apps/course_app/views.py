from django.shortcuts import render, redirect
from .models import Courses
from django.contrib import messages
    
def index(request):
    context={
        "course": Courses.objects.all()
    }
    
    return render(request, "course_app/index.html", context)