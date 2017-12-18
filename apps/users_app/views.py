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
    errors = User.objects.validate(request.POST)
    print errors
    if errors:
        for err in errors:
            error(request, err, 'red')        
        return redirect(reverse('users:my_edit', kwargs={'id':id}))
    else:
        u = User.objects.get(id=id)
        u.firstname = request.POST['fname']
        u.lastname = request.POST['lname']
        u.email = request.POST['email']
        u.save()
        return redirect(reverse('users:my_show', kwargs={'id':id}))

def create(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err, 'red')
        return redirect(reverse('users:my_new'))
    else: 
        User.objects.create(
            firstname = request.POST['fname'],
            lastname = request.POST['lname'],
            email = request.POST['email']
        )         
    return redirect(reverse('users:my_index'))




