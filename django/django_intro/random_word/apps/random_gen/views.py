from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "count" not in request.session:
        request.session["count"]=1
        request.session['random']=get_random_string(length=14)
    return render(request, "random_gen/index.html")

def generate(request):
    request.session["count"]=request.session["count"]+1
    request.session['random']=get_random_string(length=14)
    return redirect('/')
