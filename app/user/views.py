from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from user.forms import LoginForm


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            password = form.cleaned_data.get("password")
            user = authenticate(phone=phone, password=password)
            login(request, user)
            messages.success(request, '로그인 하였습니다.')
            return redirect('home')
    context = {'form': form}
    return render(request, "user/login.html", context)
