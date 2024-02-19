from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginView(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Niepoprawne dane logowania', extra_tags='bad_credentials')
            
    context = {}
    return render (request, 'logins/login.html',context)

def logoutView(request):
    logout(request)
    return redirect('login')