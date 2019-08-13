from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%A, %B %d, %Y", gmtime()),
        "time2": strftime("%H : %M", gmtime())
    }
    return render(request, "app_two/index.html", context)

def index_new(request):
    return HttpResponse("This is the /NEW page")
def create(request):
    return HttpResponse("This is the /CREATE page")
def show(request,my_val):
    return HttpResponse(f"Placeholder to display blog number {my_val} page")
def edit(request,my_val):
    return HttpResponse(f"Placeholder to EDIT blog number {my_val}")
def destroy(request,my_val):
    return HttpResponse(f"Placeholder to DELETE blog number {my_val}")