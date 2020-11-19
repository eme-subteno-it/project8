from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from django.http import JsonResponse


class SearchProduct(View):
    template_name = 'product/result.html'

    def get(self, request):
        query = request.GET.get('search')
        context = {}

        if not query:
            context['error'] = 'This product does not exist.'
        else:
            product = Product.objects.get(name__iexact=query)
            if not product:
                products = Product.objects.filter(name__icontains=query)
                if not products.exists():
                    products = Category.objects.filter(name__icontains=query)
                context = {'products': products}
                return render(request, self.template_name, context)
            else:
                substitutes = product.calculate_substitutes()
                context = {'product': product, 'substitutes': substitutes}

        return render(request, self.template_name, context)

    def post(self, request):
        if request.session:
            print(request.session)
            message = 'hello'
        else:
            message = 'no connected'

        return JsonResponse(message)


class SaveSubstitute(View):

    def get(self, request):
        pass


class ProductView(View):
    template_name = 'product/product.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        context = {'product': product}
        return render(request, self.template_name, context)
