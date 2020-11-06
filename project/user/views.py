from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import RegisterForm, LoginForm


class RegisterAccount(View):
    template_name = 'user/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            subscribed = form.cleaned_data['subscribed']

            user = User.objects.filter(email=email)
            if not user.exists():
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password1,
                    subscribed=subscribed)
            else:
                user = user.first()
            login(request, user)
            return redirect('user:my_account')

        else:
            return render(request, self.template_name, {'form': form})


class LoginAccount(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request):
    #     form = self.form_class()

    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']

    #         user = authenticate(email=email, password=password)
    #         if user is not None:
    #             login(request, user)
    #         else:
    #             return render(request, self.template_name, {'form': form})

class MyAccount(View):
    template_name = 'user/my_account.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutAccount(LogoutView):

    def get(self, request):
        if request.user:
            logout(request.user)
            return redirect('home:home')
