from django.urls import path, include
from django.contrib.auth.decorators import login_required
from  . import views

app_name = 'product'
urlpatterns = [
    path('search/', views.SearchProduct.as_view(), name='search'),
    path('product-<int:product_id>', views.ProductView.as_view(), name='product'),
]
