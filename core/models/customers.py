from django.db import models
from datetime import date, datetime


def get_customer_id():
    today_date = str(date.today()).replace("-", "")
    time_now = str(datetime.now().strftime(
        "%H:%M:%S")).replace(":", "")
    cust_id = today_date + time_now
    return cust_id


# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(
        max_length=255, primary_key=True, default=get_customer_id, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='static/assets/uploads/customer_images/')
    account_number = models.CharField(max_length=255, unique=True)
    account_branch = models.CharField(max_length=255)
    account_branch_ifsc = models.CharField(max_length=255)
    account_balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
