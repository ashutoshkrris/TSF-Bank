from django.http.response import HttpResponse
from django.shortcuts import render
from .models.customers import Customer
from .models.transactions import Transaction
from datetime import datetime, date


template_name = "transfer.html"


def transaction_id_generator():
    today_date = str(date.today()).replace("-", "")
    time_now = str(datetime.now().strftime(
        "%H:%M:%S")).replace(":", "")
    txn_id = "TSF"+today_date + time_now
    return txn_id

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def customers(request, query=None):
    if not query or query == None:
        data = Customer.objects.all()
        context = {"customers": data}
        return render(request, "customers.html", context)
    else:
        data = Customer.objects.get(account_number=query)
        context = {"customer": data}
        return render(request, "profile.html", context)


def transfer(request):
    if request.method == "POST":
        acnoself = request.POST["acnoself"]
        acno = request.POST["acno"]
        ifsc = request.POST["ifsc"]
        name = request.POST["name"]
        amount = request.POST["amount"]
        try:
            receiver = Customer.objects.get(account_number=acno)
            sender = Customer.objects.get(account_number=acnoself)
            amount = int(amount)
            if ifsc == receiver.account_branch_ifsc and name == receiver.name:
                if amount <= sender.account_balance:
                    print(sender.account_balance, receiver.account_balance)
                    sender.account_balance -= amount
                    receiver.account_balance += amount
                    print(sender.account_balance, receiver.account_balance)
                    sender.save()
                    receiver.save()
                    new_txn = Transaction(
                        debited_from=sender, credited_to=receiver, amount=amount, transaction_id=transaction_id_generator(), transaction_status="SUCCESS")
                    new_txn.save()
                    return render(request, template_name, {"message": "Transaction successful."})
                else:
                    return render(request, template_name, {"error": "Your account doesn't have sufficient balance."})
            else:
                return render(request, template_name, {"error": "Please enter correct details."})
        except Customer.DoesNotExist:
            return render(request, template_name, {"error": "Account Number does not match with any customer."})
    else:
        return render(request, template_name)


def sponsor(request):
    return render(request, "sponsor.html")


def contact(request):
    return render(request, "contact.html")
