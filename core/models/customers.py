from django.db import models
from datetime import date, datetime


# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    account_number = models.CharField(max_length=255)
    account_branch = models.CharField(max_length=255)
    account_branch_ifsc = models.CharField(max_length=255)
    account_balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_customer_id(self):
        self.today_date = str(date.today()).replace("-", "")
        self.time_now = str(datetime.now().strftime(
            "%H:%M:%S")).replace(":", "")
        self.cust_id = self.today_date + self.time_now
        return self.cust_id
