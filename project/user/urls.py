from django.urls import path, include
from django.contrib.auth.decorators import login_required
from  . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.RegisterAccount.as_view(), name='register'),
    path('login/', views.LoginAccount.as_view(), name='login'),
    path('my/account/', login_required(views.MyAccount.as_view()), name='my_account'),
    path('my/substitutes/', login_required(views.MySubstitutes.as_view()), name='my_substitutes'),
    path('delete_substitute/', login_required(views.MySubstitutes.as_view()), name='delete_substitutes'),
    path('logout/', views.LogoutAccount.as_view(), name='logout')
]
