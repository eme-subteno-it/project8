from django.shortcuts import render
from django.views import View
from .models import Product, Category


class SearchProduct(View):
    template_name = 'product/result.html'

    def get(self, request):
        query = request.GET.get('search')
        context = {}

        if not query:
            context['error'] = 'This product does not exist.'
        else:
            products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            products = Category.objects.filter(name__icontains=query)

        if products:
            context = {
                'products': products,
            }

        return render(request, self.template_name, context)
