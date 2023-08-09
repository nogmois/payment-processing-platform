from django.urls import path
from core import views
from core import transfer

urlpatterns = [
    path('', views.index, name='index'),

    # Transfers
    path('search-account/', transfer.search_users_account_number, name="search-account"),
    path('amount-transfer/<account_number>/', transfer.amountTransfer, name="amount-transfer"),

    # Request Money

    # Add Debit Card
]
