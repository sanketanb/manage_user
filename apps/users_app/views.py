from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib.messages import error


# the index function is called when root is visited
# below methods render
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request,"users_app/index.html", context)

def new(request):
    return render(request,"users_app/new.html")

def show(request, id):
    context = {
       "user" : User.objects.get(id=id)
    }
    return render(request,"users_app/show.html", context)

def edit(request, id):
    context = {
       "user" : User.objects.get(id=id)
    }
    return render(request,"users_app/edit.html", context)

def destroy(request, id):
    d = User.objects.get(id=id)
    d.delete()
    return redirect(reverse('users:my_index'))

# form methods

def update(request, id):
    if request.method == "POST":
        result = User.objects.validate_update(request.POST, user_id=id)
        if type(result) == User:
            return redirect(reverse('users:my_show', kwargs={'id':id}))
        for err in result:
            error(request, err, 'red')        
    return redirect(reverse('users:my_edit', kwargs={'id':id}))
    

def create(request):
    result = User.objects.validate_create(request.POST)
    if type(result) == User:
        return redirect(reverse('users:my_index'))
    else:
        for err in result:
            error(request, err, 'red')
            return redirect(reverse('users:my_new'))
    




