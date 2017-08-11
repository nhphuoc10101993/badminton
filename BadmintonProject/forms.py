from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Receipt
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
        }
    def save(self,commit=True):
        frm_user = super(CreateUserForm,self).save(commit=False)
        frm_user.username = self.cleaned_data['username']
        frm_user.email = self.cleaned_data['email']
        frm_user.first_name = self.cleaned_data['first_name']
        frm_user.last_name = self.cleaned_data['last_name']
        if commit:
            frm_user.save()
        return frm_user
class ReceiptForm(forms.Form):
    cashier = forms.CharField(max_length=30)
    receipt_person = forms.CharField(max_length=30)
    date_receipt = forms.DateField()
    reason = forms.TextInput()
    class Meta:
        model = Receipt()
        fields = {
            'cashier',
            'receipt_person',
            'date_receipt',
            'money',
            'reason',
        }

