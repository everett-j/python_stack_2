from django.shortcuts import render, redirect
from .models import Shows
    
def index(request):
  
    return redirect(request, "/")


def shows_new(request): #DONE
    print ("I am before the if")
    if request.method=="POST":
        Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], description=request.POST['description'])
    return render(request, "shows/index.html")


def shows_all(request):
    context = {
    	"shows_all": Shows.objects.all(),
    }
    return render(request, "shows/shows.html", context)


def shows_edit(request, shows_id):
    context = {
    	"shows_edit": Shows.objects.all(),
    }
    return render(request, "shows/edit.html", context)


def shows_view(request, shows_id): #WIP
    context = {
        'shows' : Shows.objects.get(id = shows_id),
        'all_shows' : Shows.objects.all(),
    }
    return render(request, "shows/show_detail.html", context)
