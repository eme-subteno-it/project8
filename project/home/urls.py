""" All urls for the home application """
from django.urls import path
from  . import views


app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('legal-notices/', views.LegalNoticeView.as_view(), name="legal_notices")
]
