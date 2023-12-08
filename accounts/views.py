from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import UserRegistrationForm


def register_view(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
            )
            user.set_password(raw_password=form.cleaned_data['password'])
            user.save()
            return redirect("...")
    

    context = {
        "form": form
    }
    return render(request=request, template_name="register.html", context=context)


def login_view(request):
    pass


def logout_view(request):
    pass