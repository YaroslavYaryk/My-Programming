from django.shortcuts import render
from .forms import TransactionForm
from django.db import transaction
from .models import Customer


def work_with_transaction(request):

    e = ""
    method = ""
    if request.method == "POST":
        form = TransactionForm(request.POST)
        method = "POST"
        try:
            if form.is_valid():
                payor = form.cleaned_data["payor"]
                payee = form.cleaned_data["payee"]
                amount = form.cleaned_data["amount"]

                with transaction.atomic():
                    payor = Customer.objects.select_for_update().get(name=payor)
                    payor.balance -= int(amount)
                    print("balance   -  ", payor.balance)
                    payor.save()

                    payee = Customer.objects.select_for_update().get(name=payee)
                    payee.balance += int(amount)
                    payee.save()

        except Exception as er:
            e = er
            print(e)

    else:
        form = TransactionForm()
    return render(
        request,
        "new_app/formm.html",
        context={"form": form, "error": e, "method": method},
    )
