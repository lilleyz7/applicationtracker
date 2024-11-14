from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                user.save()
                login(request, user)
                return redirect('login/')
            except Exception as e:
                return render(request, 'register.html', {'register_form': form, 'error_message': 'Unable to create user'})
        return render(request, 'authentication/register.html', {'register_form': form, 'error_message': 'Enter form correctly'})
    else:
        form = RegisterForm()
        return render(request,'authentication/register.html', {'register_form': form})

def login_user(request):
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/recipes/home')
            else:
                return render(request, 'authentication/login.html', {'login_form': form, 'error_message': 'Incorrect password'})
    else:
        form = LoginForm()
        return render(request, 'authentication/login.html', {'login_form': form})
@login_required(login_url="/auth/login/")
def logout_user(request):
    logout(request)
    return redirect('/authentication/login')