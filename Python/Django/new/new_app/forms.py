from django import forms


class TransactionForm(forms.Form):

    payor = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    payee = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    amount = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
