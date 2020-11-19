from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from user.models import User
from django.http import JsonResponse


class SearchProduct(View):
    template_name = 'product/result.html'

    def get(self, request):
        query = request.GET.get('search')
        if not query:
            message = 'This product does not exist.'
            context = {'error': message}
        else:
            products = Product.objects.filter(name__icontains=query)
            if not products.exists():
                message = 'This product does not exist sorry.'
                context = {'error': message}
            else:
                context = {'products': products}

        return render(request, self.template_name, context)


class Substitutes(View):
    template_name = 'product/substitutes.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        substitutes = product.calculate_substitutes()
        context = {'product': product, 'substitutes': substitutes}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated:
            query = request.POST.get('product_id')
            product = Product.objects.get(id=query)
            user = User.objects.get(id=request.user.id)
            product.save_substitute(user)

            res = {'good_message': 'hello'}
        else:
            res = {'error_message': 'no connected'}

        return JsonResponse(res)


class ProductView(View):
    template_name = 'product/product.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        context = {'product': product}
        return render(request, self.template_name, context)
