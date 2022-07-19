from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .auth import unauthenticated_user


# Create your views here.


@unauthenticated_user
def userregister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully')
            return redirect('news_user:login')

        else:
            messages.add_message(request, messages.ERROR, 'Error in registering user')

            return render(request, 'news_user/register.html', {'form': form})

    context = {
        'form': UserCreationForm

    }

    return render(request, 'news_user/register.html', context)


def userlogout(request):
    logout(request)
    return redirect('/')


def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            print(user)

            if user is not None:
                if not user.is_staff:
                    login(request,user)
                    return redirect('news:home')
                elif user.is_staff:
                    login(request,user)
                    return redirect('news_admin:dashboard')
                   
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Invalid Username or Password')


            else:
                messages.add_message(request, messages.ERROR, 'Invalid Username or Password')

                return render(request, 'news_user/login.html', {'form': form})

    context = {
        'form': LoginForm
    }
    return render(request, 'news_user/login.html', context)


# def user_account(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account Update Successful for' + str(request.user.profile))
#             return redirect('/profile')

#     context = {'form': form}
#     return render(request, 'accounts/profile.html', context)
