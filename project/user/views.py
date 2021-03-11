""" All views for the user application """
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from product.models import Product
from .models import User
from .forms import RegisterForm, LoginForm


class RegisterAccount(View):
    """ Class View to display the the form register """

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

        return render(request, self.template_name, {'form': form})


class LoginAccount(LoginView):
    """ Class View to display the the form login """

    template_name = 'user/login.html'
    authentication_form = LoginForm


class MyAccount(View):
    """ Class View to display the my account page """

    template_name = 'user/my_account.html'

    def get(self, request):
        return render(request, self.template_name)


class MySubstitutes(View):
    """ Class View to display the my substitutes page """

    template_name = 'user/my_substitutes.html'

    def get(self, request):
        if request.user.is_authenticated:
            products = User.objects.get(id=request.user.id).product_set.all()
            len_products = len(products)
            context = {'products': products, 'len': len_products}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated:
            query = request.POST.get('product_id')
            product = Product.objects.get(id=query)
            user = User.objects.get(id=request.user.id)
            product.delete_substitute(user)

            res = {'good_message': 'delete'}
        else:
            res = {'error_message': 'impossible'}

        return JsonResponse(res)


class LogoutAccount(LogoutView):
    """ Class View to deconnect user """

    def get(self, request):
        logout(request)

        return redirect('home:home')
