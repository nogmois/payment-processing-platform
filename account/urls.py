from django.urls import path
from account import views

urlpatterns = [
    path('kyc-reg/', views.kyc_registration, name='kyc-reg'),
    path('', views.account, name='account'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
