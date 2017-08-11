from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from . import forms
from .models import Receipt
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import datetime
from django.db.models import Q
from django.db.models import Sum
import re
from paginator import ModelPagination
from django.conf import settings
# Create your views here.
@login_required
def home_page(request):
    return render(request,'home_page.html',{})
@login_required
def player_list(request):
    listUser = User.objects.all()
    args = {'listUser':listUser}
    return render(request,'player_list.html',args)
@login_required
def create_user(request):
    form = forms.CreateUserForm()
    if request.method == 'POST':
        frm_user = forms.CreateUserForm(request.POST)
        if frm_user.is_valid():
            frm_user.save()
            return redirect(player_list)
        else:
            return render(request,'create_user.html',{'form':form})
    return render(request,'create_user.html',{'form':form})
@login_required
def changePassword(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        frm_changepass = PasswordChangeForm(request.user,request.POST)
        if frm_changepass.is_valid():
            user = frm_changepass.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your account is updated new password')
            return redirect(player_list)
        else:
            return render(request,'change_password.html',{'form':form})
    return render(request,'change_password.html',{'form':form})
@login_required
def receipt(request):
    if request.method == 'GET':
        page_num = int(request.GET.get('page',1))
    else:
        page_num = 1
    _item_per_page = 10
    today = datetime.datetime.today()
    today.strftime('%B')
    month = today.month
    year = today.year
    page_list_receipt = Receipt.objects.filter(Q(date_receipt__year = year)&Q(date_receipt__month = month))
    pagination = ModelPagination(page_list_receipt,_item_per_page)
    list_receipt = pagination.page(page_num)
    items = map(lambda x: {
        'id_receipt': x.get('id_receipt'),
        'first_name': x.get('receipt_person__first_name'),
        'last_name': x.get('receipt_person__last_name'),
        'date_receipt': x.get('date_receipt'),
        'money': x.get('money'),
        'cashier': x.get('cashier'),
        'reason' : x.get('reason'),
    }, list_receipt.object_list.values('id_receipt', 'receipt_person__first_name','receipt_person__last_name', 'date_receipt', 'money', 'cashier','reason'))
    #return HttpResponse(items)
    listReceiptByYearAndMonth = Receipt.objects.filter(Q(date_receipt__year = year)&Q(date_receipt__month = month))
    listUserUnReceipt = User.objects.exclude(username__in=[item.receipt_person.username for item in listReceiptByYearAndMonth])
    sum_money = Receipt.objects.filter(Q(date_receipt__year = year)&Q(date_receipt__month = month)).aggregate(Sum('money'))
    args = {'list_receipt':items,'listUserUnReceipt':listUserUnReceipt,'sum_money_receipt':sum_money.get('money__sum'),'month':month,'years':year,'pagination':pagination,'current_page':list_receipt}
    return render(request,'receipts.html',args)
@login_required
def add_receipt(request):
    if request.method == 'POST':
        receiptObject = Receipt()
        receipt_person = request.POST['list_username']
        receiptObject.receipt_person = User.objects.get(username=receipt_person)
        receiptObject.cashier = request.user
        receiptObject.date_receipt = request.POST['date_receipt']
        receiptObject.money = int(request.POST['txtMoney'])
        receiptObject.reason = request.POST['areaReason']
        receiptObject.save()
        return redirect(receipt)
    return redirect(receipt)
@login_required
def redirect_edit_receipt(request):
    if request.method == 'POST':
        idReceipt = request.POST['txt_id_receipt']
        if idReceipt:
            objectReceipt = Receipt.objects.get(id_receipt=idReceipt)
            return render(request,'edit_receipt.html',{'objectReceipt':objectReceipt})
@login_required
def update_receipt(request):
    object_receipt = Receipt()
    if request.method == 'POST':
        try :
            id_receipt = request.POST['txt_id_receipt_update']
            object_receipt.id_receipt = int(id_receipt)
            object_receipt.receipt_person = User.objects.get(username=request.POST['txt_receipt_person'])
            object_receipt.date_receipt = datetime.datetime.strptime(request.POST['txt_date_receipt'],"%Y-%m-%d").date()
            object_receipt.money = int(request.POST['txt_money_receipt'])
            object_receipt.reason = request.POST['areaReason']
            object_receipt.cashier = request.user.username
            try:
                object_receipt.save()
                result = "Update Successfully..."
            except:
                result = "Update Failed..."
        except:
            result = "Some fields have value incorrect..."
        return render(request,'edit_receipt.html',{'result':result})
@login_required
def delete_receipt(request):
    if request.method == 'POST':
        id_receipt = request.POST['txt_id_receipt_delete']
        try:
            object_receipt = Receipt.objects.get(id_receipt=id_receipt)
            object_receipt.delete()
            result = "Delete Successfully:"+id_receipt
        except:
            result = "Delete Failed:"+id_receipt
        messages.add_message(request, messages.INFO, result)
        return redirect(receipt)
@login_required
def delete_selected_receipt(request):
    if request.method == 'POST':
        try:
            txt_value = request.POST['txtListReceipt']
            list_check = re.compile(":").split(txt_value)
            if txt_value:
                for item in list_check:
                    object_receipt = Receipt.objects.get(id_receipt=item)
                    object_receipt.delete()
                    messages.add_message(request, messages.SUCCESS, 'Delete Successfully:'+item)
        except:
            messages.add_message(request, messages.ERROR, 'Delete Failed...')
    return redirect(receipt)
@login_required
def search_receipt_follow_month_year(request):
    if request.method == 'POST':
        try:
            cbx_year = int(request.POST['selectYear'])
            cbx_month = int(request.POST['selectMonth'])
            if cbx_year and cbx_month:
                list_receipt = Receipt.objects.filter(Q(date_receipt__year = cbx_year)&Q(date_receipt__month = cbx_month))
                if not list_receipt:
                    messages.add_message(request, messages.INFO, 'Data is empty')
                today = datetime.datetime.today()
                today.strftime('%B')
                month = cbx_month
                year = cbx_year
                listReceiptByYearAndMonth = Receipt.objects.filter(Q(date_receipt__year = year)&Q(date_receipt__month = month))
                listUserUnReceipt = User.objects.exclude(username__in=[item.receipt_person.username for item in listReceiptByYearAndMonth])
                sum_money = Receipt.objects.filter(Q(date_receipt__year = year)&Q(date_receipt__month = month)).aggregate(Sum('money'))
                args = {'list_receipt':list_receipt,'listUserUnReceipt':listUserUnReceipt,'sum_money_receipt':sum_money.get('money__sum'),'month':month,'years':year}
                return render(request,'receipts.html',args)
        except:
            messages.add_message(request, messages.INFO, 'Data is empty')
    return redirect(receipt)
def test_dict(request):
    members = settings.MEMBERS
    return render(request,'test_dict.html',{'context':members})