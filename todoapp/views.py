from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages


# Create your views here.
def create(request):
    cre = Todo_list.objects.all()
    if request.method == "POST":
     tasks=Todo_list()
     tasks.task=request.POST.get('tas')
     tasks.save()
     return redirect('home')
    context={'cre' :cre}
    return render(request,'index.html',context)

def finished(request, pk):
    todo =get_object_or_404(Todo_list, id=pk)
    todo.finished = True
    
    todo.save()  
    return redirect('home')
   
def delete(request,pk):
    dele =Todo_list.objects.get(id=pk)
    dele.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':  
        uname = request.POST.get('username')  
        email = request.POST.get('email')  
        pass1 = request.POST.get('password') 
        pass2 = request.POST.get('password1')
        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                reg1 = User.objects.create_user(
                username=uname,
                email=email,
                password=pass1
                
        )
            reg1.save()
            return redirect('login')
        else:
          messages.info(request,'password mismatch')
        
      
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        us=authenticate(request,username=uname,password=passw)
        if us is not None:
            login(request, us)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login.html')
    else:
        return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('login')
