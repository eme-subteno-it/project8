""" All views for the product application """
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.http import JsonResponse
from user.models import User
from user.forms import LoginForm
from .models import Product


class SearchProduct(View):
    """ Class View to display the result of search products """

    template_name = 'product/result.html'

    def get(self, request):
        query = request.GET.get('search')
        if not query:
            message = _('This product does not exist.')
            context = {'error': message}
        else:
            products = Product.objects.filter(name__icontains=query)
            if not products.exists():
                message = _('This product does not exist sorry.')
                context = {'error': message}
            else:
                context = {'products': products}

        return render(request, self.template_name, context)


class Substitutes(View):
    """ Class View to display the substitutes of search products """

    template_name = 'product/substitutes.html'
    form_class = LoginForm

    def get(self, request, product_id):
        form = self.form_class
        product = get_object_or_404(Product, pk=product_id)
        substitutes = product.calculate_substitutes(50)
        context = {}

        query = request.GET.get('substitute_id')
        if query:
            if request.user.is_authenticated:
                substitute_for_save = Product.objects.get(id=query)
                user = User.objects.get(id=request.user.id)
                substitute_for_save.save_substitute(user)
                context['message'] = _('Your product has been saved.')
        context['product'] = product
        context['substitutes'] = substitutes
        context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request):
        """ Method to save a substitute in call Ajax """
        number_list = request.POST.get('number')
        if number_list:
            product = get_object_or_404(Product, pk=request.POST.get('product_search_id'))
            substitutes = product.calculate_substitutes(number_list)
            context = {}
            context['product'] = product
            context['substitutes'] = substitutes

            return render(request, 'product/substitutes_loop.html', context)

        if request.user.is_authenticated:
            query = request.POST.get('product_id')
            product = Product.objects.get(id=query)
            user = User.objects.get(id=request.user.id)
            product.save_substitute(user)

            res = {'status': 'success'}
        else:
            res = {'status': 'error'}

        return JsonResponse(res)


class ProductView(View):
    """ Class view to display the product page choose """

    template_name = 'product/product.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        context = {'product': product}
        return render(request, self.template_name, context)
