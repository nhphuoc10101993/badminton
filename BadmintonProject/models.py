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