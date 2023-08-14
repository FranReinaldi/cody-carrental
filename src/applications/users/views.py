from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return redirect('login')
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        return redirect('register')
    return render(request, 'profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})


def check_email(request):
    email = request.GET.get('email', None)
    if email:
        email_taken = CustomUser.objects.filter(email=email).exists()
        print(email_taken)
        return JsonResponse({'email_taken': email_taken})
    return JsonResponse({'error': 'Email no proporcionado'}, status=400)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
