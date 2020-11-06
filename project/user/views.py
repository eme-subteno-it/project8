from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .models import User
from .forms import RegisterForm


class RegisterAccount(View):
    template_name = 'user/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        new_template = 'user/my_account.html'
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            subscribed = form.cleaned_data['subscribed']

            user = User.objects.filter(email=email)
            if not user.exists():
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    subscribed=subscribed)
            else:
                user = user.first()
            login(request, user)
            return redirect('my_account')

        else:
            context = {'form': form, 'error': form.errors.items()}
            return render(request, self.template_name, context)


class LoginAccount(View):
    template_name = 'user/login.html'

    def get(self, request):
        return render(request, self.template_name)


class MyAccount(View):
    template_name = 'user/my_account.html'

    def get(self, request):
        return render(request, self.template_name)
