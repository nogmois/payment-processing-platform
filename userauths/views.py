
from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #form.save()
            new_user = form.save() #new_user.email
            username = form.cleaned_data.get('username')
            #username = request.POST.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")
            new_user = authenticate (username=form.cleaned_data['email'], password=form.cleaned_data['password1'])         

            login(request, new_user)
            return redirect('account')
        
    elif request.user.is_authenticated:
        messages.warning(request, f"You are alredy logged in")
        return redirect('account')
    
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'userauths/sign-up.html', context)


def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
        
            if user is not None: # if there is a user
                login(request, user)
                messages.success(request, 'You ar Logged')
                return redirect('account')
            else:
                messages.warning(request, 'Username or Password does not exist')
                return redirect('sign-in')
        except:
            messages.warning(request, 'User does not exist')
    
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged In')
        return redirect('account')
    
    return render(request, 'userauths/sign-in.html')


def logoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('sign-in')