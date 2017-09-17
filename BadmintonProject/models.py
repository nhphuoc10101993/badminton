from django.db import models
from django.contrib.auth.models import User
import django.db.models.deletion
import datetime
class Receipt(models.Model):
    id_receipt = models.AutoField(primary_key=True)
    cashier = models.CharField(max_length=30)
    receipt_person = models.ForeignKey(User)
    date_receipt = models.DateField(default=datetime.datetime.today())
    money = models.IntegerField(default=0)
    reason = models.TextField()
class Expenses(models.Model):
    id_expense = models.AutoField(primary_key=True)
    expense_person = models.ForeignKey(User)
    date_expense = models.DateField(default=datetime.date.today())
    money = models.IntegerField(default=0)
    reason = models.TextField()