from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomeView(request):
    return render(request,'home.html')

def SignUpView(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        #print(name,email,password1,password2 )
        if password1 != password2:
            return HttpResponse('password must be same')
        else:
            user = User.objects.create_user(name,email,password1)
            user.save()
            #return HttpResponse('user created')
            return redirect('login')
    return render(request,'signup.html')

def LoginView(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password1')
        #print(name,password)
        user = authenticate(request,username = name,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect!!!')
    return render(request,'login.html')

def LogOutView(request):
    logout(request)
    return redirect('login')