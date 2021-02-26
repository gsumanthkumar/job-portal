from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, response
from .models import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def search(request):
    if request.method == 'POST':
        skeyword = request.POST['Search']
        searchcontent = postjob.objects.filter(jobname__icontains=skeyword)
        context = {
        'search' : skeyword,
        'post':searchcontent
        }
    return render(request, 'main/search.html',context)

def logout(request):
    auth.logout(request)
    return redirect('login')
    
def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=u,password=p)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email is already taken by others')
                return redirect('register')
            elif User.objects.filter(username = uname):
                messages.warning(request, 'Username is taken by others')
                return redirect('register')
            else:
                user = User.objects.create_user(username = uname, email = email, password=password1)
                return redirect('login')
        else:
            messages.warning(request, 'passwords not matching')
            return redirect('register')
        
    else:
        return render(request, 'main/register.html')


@login_required(login_url= 'login')
def getjobv(request):
    form = postjob.objects.all().exclude(jobposter=request.user)
    context = {
        'form' : form
    }
    return render(request, 'main/getjob.html',context)

@login_required(login_url= 'login')
def postjobv(request):
    if request.method == 'POST':
        form = postjobform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.jobposter = request.user
            obj.save()
            messages.success(request,'Successfully Posted')
            return redirect('postjobv')
    else:
        form = postjobform()
        context = {
            'form' : form
        }
        return render(request, 'main/postjob.html', context)

@login_required(login_url= 'login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url= 'login')
def mypostedjobs(request):
    form = postjob.objects.filter(jobposter=request.user)
    context = {
        'form' : form
    }
    return render(request, 'main/mypostedjobs.html', context)

@login_required(login_url= 'login')
def update(request, pk):
    task = postjob.objects.get(id=pk)
    form = postjobform(instance=task)
    if request.method == 'POST':
        form = postjobform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        context = {'form': form}
        return render(request, 'main/update.html',context)

@login_required(login_url= 'login')
def delete(request,pk):
    item = postjob.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('profile')
    else:
        context = {'item': item}
        return render(request, 'main/delete.html',context)


@login_required(login_url= 'login')
def profile(request):
    form = postjob.objects.filter(jobposter=request.user)
    context = {
        'form' : form
    }
 
    return render(request, 'main/profile.html',context)
@login_required(login_url= 'login')
def about(request):
    return render(request, 'main/about.html')