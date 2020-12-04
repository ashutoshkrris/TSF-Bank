from django.contrib import admin
from .models.customers import Customer
from .models.transactions import Transaction


# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'account_number',
                    'account_branch', 'account_balance']


class AdminTransactions(admin.ModelAdmin):
    list_display = ['debited_from', 'credited_to', 'amount',
                    'transaction_id', 'transaction_date', 'transaction_status']


admin.site.register(Customer, AdminCustomer)
admin.site.register(Transaction, AdminTransactions)

admin.site.site_header = 'TSF Bank Admin Panel'
