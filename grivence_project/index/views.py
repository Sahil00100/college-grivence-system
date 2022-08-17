from django.shortcuts import render,redirect
from.forms import UserForm,User
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from django.contrib import messages
import datetime
from.models import Grivence,Message,Student
from django.contrib.auth.decorators import login_required   
# Create your views here.
@login_required(login_url='login')
def index_view(request):
    if request.method=="POST":
        subject=request.POST.get('subject')
        describe=request.POST.get('describe')
        name=User.objects.get(username=request.user)
        date=datetime.datetime.today()
        action='submitted'
        complaint=Grivence(
            subject=subject,
            describe=describe,
            name=name,
            date=date,
            action=action,
        )
        complaint.save()
        return redirect('index')
    user=request.user
    
    return render(request, 'index.html',{'user':user})

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('principal')
            else:
                login(request,user)
                return redirect('index')
        else:
            
            messages.add_message(request, messages.ERROR, 'Username or Password is invalid')
            print('invalid username or password')
            return redirect('login')
    

  
    return render(request,'login.html',{})
    

def signup_view(request):
    print(1)
    if request.method=='POST':
        print(2)
        form=UserForm(request.POST)
        if form.is_valid():
            print(3)
            user=form.create_user()
            student=form.create_student()
            user.save()
            student.save()
            return redirect('login')
        else:
            print(form.errors)
            print('failed')
    else:
        form=UserForm()
    return render(request, 'signup.html',{'form':form})


@login_required(login_url='login')
def dashboard_view(request):
    obj=Grivence.objects.filter(name=request.user).order_by('-id')
    return render(request, 'dashboard.html',{'obj':obj})
@login_required(login_url='login')
def message_view(request):
    msg=Message.objects.filter(name=request.user).order_by('-id')
    return render(request, 'message.html',{'msg':msg})
@login_required(login_url='login')
def principal_view(request):
    user=User.objects.get(username=request.user)
    if user.is_staff:

        obj=Grivence.objects.all().order_by('-id')
        finished=Grivence.objects.filter(action='finished')
        processing=Grivence.objects.filter(action='processing')
        pending=Grivence.objects.filter(action='submitted')

        total=len(obj)
        finished_1=len(finished)
        processing_1=len(processing)
        pending_1=len(pending)
        
        return render(request, 'principle.html',{'t':total,'f':finished_1,'process':processing_1,'pending':pending_1,'obj':obj})
    else:
        return redirect('index')
#log out
def logout_view(request):
    logout(request)
    print('logout success!')
    return redirect('login')