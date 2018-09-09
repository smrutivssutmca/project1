from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, checkin_form, edit_form
from .models import checkin
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Logged In !!!')
            return redirect('home')

        else:
            return redirect('login_user')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Registered !!!')
            return redirect('home')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Edited Your Profile !!!')
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'editprofile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Changed Your Password!!!')
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'change_password.html', context)


def create_checkin(request):
    return render(request, 'create_checkin.html')


def save_checkin(request):
    if request.method == 'POST':
        form = checkin_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            address = form.cleaned_data['address']
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            place_name = form.cleaned_data['place_name']
            review = form.cleaned_data['review']
            p = checkin(address=address, longitude=longitude, latitude=latitude, place_name=place_name, review=review, user=post.user)
            p.save()
            messages.success(request, 'You have saved your review')
            return redirect('home')


def get_checkin(request):
    form = checkin_form()
    post = checkin.objects.filter(user=request.user)
    args = {'form': form, 'post': post}

    return render(request, 'get_checkin.html', args)

def delete_checkin(request, pk):
    query = checkin.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'You have deleted your checkin')
    return redirect('home')


